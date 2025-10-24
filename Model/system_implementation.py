import os
import re
import argparse
import gradio as gr

from langchain_openai import ChatOpenAI
import vertexai
from langchain_google_vertexai import ChatVertexAI
from langchain_anthropic import ChatAnthropic
from langchain_deepseek import ChatDeepSeek
from langchain_community.document_loaders import TextLoader
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

import flowcharts


def args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--flowchart_dir", type=str, default="../Flowcharts/from_book/Preprocess_AMA")
    parser.add_argument("--platform", type=str, default="OPENAI")
    parser.add_argument("--model", type=str, default="gpt-4o-mini") #"gpt-4-0125-preview" "gpt-4o-mini"
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--log", type=str, default="study_log.txt")

    args, unknown = parser.parse_known_args()
    return args

def platform_selection(platform, temp, model):
    if platform == "OPENAI":
        llm = ChatOpenAI(temperature=temp, model=model)
    elif platform == "GOOGLE":
        vertexai.init(project="triagemd-454205", location="us-central1")
        llm = ChatVertexAI(temperature=temp, model=model)
    elif platform == "ANTHROPIC":
        llm = ChatAnthropic(temperature=temp, max_tokens=2048, model=model)
    elif platform == "DEEPSEEK":
        llm = ChatDeepSeek(temperature=temp, model=model)
    else:
        raise Exception("The system only supports three platforms: OpenAI, Google Vertex AI, Anthropic and DeepSeek.")
    
    return llm

def parse_rag_output(answer):
    answer_lower = re.sub(r'[\W_]+', '', answer.lower())
    flowchart_name = re.search(r'[A-Za-z ]+Flowchart', answer)
    if "noflowchartavailable" in answer_lower:
        return "no flowchart available"
    elif flowchart_name:
        return flowchart_name.group(0)
    else:
        return f"Not a valid RAG output: {answer}"

def get_flowchart(answer):
    if "no flowchart available" in answer:
        return "no authorization to answer"
    elif "Not a valid RAG output" in answer:
        return answer
    answer = answer.strip().replace(" ", "_")
    func_obj = getattr(flowcharts, answer, None)
    # print(func_obj)
    if func_obj is None:
        return f"{answer} not found"
    flowchart, graph = func_obj()
    return flowchart, graph
    
def nested_flowchart(flowchart):
    remap_dict = {"Pelvic Pain In Women Flowchart": "Abdominal Pain Flowchart",
                  "Confusion In Older People Flowchart": "Confusion Flowchart", 
                  "Lack Of Bladder Control In Older People Flowchart": "Lack Of Bladder Control Flowchart"}
    return remap_dict[flowchart]

def create_retriever(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.split('\n')
    data = []
    for line in lines:
        content = line.strip()
        if content: 
            data.append(Document(page_content=content))

    vectorstore = FAISS.from_documents(documents=data, embedding=OpenAIEmbeddings())
    return vectorstore

def RAG_call(filepath, query, llm, k, split=True, retrieve=False):
    # whether include similarity search
    if split:
        vectorstore = create_retriever(filepath)
        retrieved_with_score = vectorstore.similarity_search_with_score(query, k)
        retrieved_output = []
        for doc, score in retrieved_with_score:
            retrieved_output.append({
                "content": doc.page_content,
                "score": score
            })
    else:
        loader = TextLoader(file_path=filepath, encoding="utf-8") 
        retrieved_output = loader.load()
    
    system_prompt = (
        """Your role: You are an assistant supporting an Emergency Department nurse in patient triage.
        Your task: Based on the patient's input, identify and return only the name of the appropriate flowchart to use from the provided context.
        If there is no relevant flowchart, return: "no flowchart available".
        \n\n
        {context}
        \n\n"""
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    rag_chain = prompt | llm | StrOutputParser()
    conversation = rag_chain.invoke({"context": retrieved_output, "input": query})
    if retrieve:
        return conversation, retrieved_output
    
    return conversation


def parse_LLM_internal_output(input_dict):
    if input_dict['isOnTopic'] == "No":
        return "off-topic"
    if input_dict['isUncertain'] == "Yes":
        return "uncertain"
    elif input_dict['isUncertain'] == "No":
        if input_dict['actualAnswer'] == "Yes":
            return "Yes"
        elif input_dict['actualAnswer'] == "No":
            return "No"
        else: 
            return "not answered"
    else:
        raise ValueError(f"Wrong output from LLM_internal: {input_dict}")
    

# LLM for internal decision making
def LLM_internal(query, protocol, model, parse=True):
    # structured output 
    response_schemas = [
        ResponseSchema(name="isOnTopic", description="'Yes' if the response is relevant to the question, otherwise 'No'."),
        ResponseSchema(name="isAnswered", description="'Yes' if the response provides a yes or no answer, otherwise 'No'."),
        ResponseSchema(name="actualAnswer", description="'Yes' if the patient answers the question affirmatively, 'No' if the patient answers negatively."),
        ResponseSchema(name="isUncertain", description="'Yes' if the response expresses uncertainty (e.g., 'maybe', 'not sure', 'probably'), otherwise 'No'.")
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

    system_prompt = (
        "Your role: You are a decision making assistant supporting an Emergency Department nurse in patient triage."
        "Your task: Based on the patient input, decide whether the patient provided an answer to the question from the triage protocol below."
        "{format_instructions}"
        "Triage protocol: {context}"
    )
    judge_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    ).partial(format_instructions=output_parser.get_format_instructions())

    judge_chain = judge_prompt | model | output_parser
    judge = judge_chain.invoke({"input": query, "context": protocol})
    # print(judge)
    if parse:
        output = parse_LLM_internal_output(judge)
        return output
    else:
        return judge


def LLM_external_prompt_mapping():
    prompt = {1: "Convey this to the patient",
              2: "Patient's response is off-topic, ask this again",
              3: "Patient's indicates uncertainty, try confirming this"}
    return prompt

def LLM_external(query, prompt, protocol, model, chat_history):
    system_prompt = (
        "Your role: You are a nurse responsible for online triage in the Emergency Department."
        "Your task: {prompt}: {context}"
        "Rules: 1. Your response must fully adhere to the provided context, no additional information is allowed."
        "2. Be concise and empathetic, avoid excessive repetition."
    )
    chatbot_prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
            ("system", system_prompt),
        ]
    )

    chatbot_chain = chatbot_prompt | model | StrOutputParser()
    chat = chatbot_chain.invoke({"input": query, "prompt": prompt, "context": protocol, "chat_history": chat_history}) 
    return chat

def format_conversation_history(conversation):
    history_langchain_format = []
    # format the conversation history to meet langchain requirement
    for text in conversation:
        # print("text: ", text)
        if "Patient: " in text:
            # print("human message: ", text)
            patient = text.split("Patient: ")[1]
            history_langchain_format.append(HumanMessage(content=patient))
        elif "TriageMD: " in text: 
            triagemd = text.split("TriageMD: ")[1]
            # print("triagemd message: ", text)
            history_langchain_format.append(AIMessage(content=triagemd))
        else:
            raise ValueError("Incorrect Format in Conversation")
    return history_langchain_format

def get_next_step(graph, current_step, answer):
    # check all outgoing edges from the current node
    for _, next_node, edge_data in graph.out_edges(current_step, data=True):
        # if the edge condition matches the given condition
        if edge_data.get("condition") == answer:
            return next_node
    # return none if no matching condition is found
    return None

def flowchart_following(flowchart, graph, prompt, current_node, current_path, model, num_of_off_topic=0, num_of_uncertain=0):
    # default prompt type is 1
    prompt_type = 1
    if current_node in flowchart:
        print("current_node: ", current_node)
        
        if current_node.startswith("N"):
            # print(prompt)
            # print(flowchart[current_node])
            decision = LLM_internal(prompt, flowchart[current_node], model)
            print("while 1, first decision: ", decision)
            while decision not in ["Yes", "No", "off-topic", "uncertain", "not answered"]:
                # rerun the LLM_internal
                decision = LLM_internal(prompt, flowchart[current_node], model)
                print("in while 1, decision: ", decision)
            if decision in ["Yes", "No"]:
                next_node = get_next_step(graph, current_node, decision)
                if next_node.startswith("F"):
                    new_flowchart = flowchart[next_node]
                    current_path.append(next_node)
                    print(f"switch to {new_flowchart}")
                    flowchart_result = get_flowchart(new_flowchart)
                    # unpack flowchart_result
                    if isinstance(flowchart_result, tuple):
                        flowchart, graph = flowchart_result
                    else:
                        raise ValueError(f"Referred to {new_flowchart}, but did not implement")
                    current_node = "N1"
                    current_path.append(current_node)
                else:
                    current_path.append(next_node)
                    current_node = next_node
            elif decision == "off-topic":
                prompt_type = 2
                num_of_off_topic = num_of_off_topic + 1
            elif decision == "uncertain":
                prompt_type = 3
                num_of_uncertain = num_of_uncertain + 1
        if current_node.startswith("I"):
            next_node = get_next_step(graph, current_node, None)
            new_flowchart = flowchart[next_node]
            current_path.append(next_node)
            print(f"switch to {new_flowchart}")
            flowchart_result = get_flowchart(new_flowchart)
            if isinstance(flowchart_result, tuple):
                flowchart, graph = flowchart_result
            else:
                raise ValueError(f"Referred to {new_flowchart}, but did not implement")
            current_node = "N1"
            current_path.append(current_node)
            
    return current_node, flowchart, graph, current_path, prompt_type, num_of_off_topic, num_of_uncertain


def UI_gradio(rag_file, llm, output_file=None):

    info_gathered = ""

    def info_gathering(a0, a1, a2):
        # a0 - name, a1 - sex, a2 - age
        nonlocal info_gathered

        welcome_message = f"Welcome {a0}! Thank you for sharing the information. How can I help you today?"
        info_gathered = f"Sex - {a1}, Age - {a2}"
        chat_history = [(None, welcome_message)]
        return gr.update(visible=True), gr.update(visible=False), gr.update(value=chat_history)
    
    with gr.Blocks() as demo:
        gr.Markdown(
            """
            # TriageMD - Your Virtual Assistant for Medical Inquiries
            """
        )
        with gr.Row():
            with gr.Column(visible=True) as pre_collect:
                q0_name = gr.Textbox(label="Please enter your name: ")
                q1_sex = gr.Radio(choices=["Female", "Male", "Prefer not to say"], label="Please select your sex: ")
                q2_age = gr.Textbox(label="Please enter your age: ")
                start_button = gr.Button("Start Chat")
            
            with gr.Column(visible=False) as chat_window:
                print("************* Start Interaction ************")
                chatbot = gr.Chatbot(label="TriageMD", height=600)
                user_input = gr.Textbox(show_label=False, placeholder="Type a message...")

                # initialize nonlocal variables
                # system flags: first_interaction, retrieved, num_of_off_topic, num_of_uncertain
                first_interaction = True
                retrieved = False
                flowchart = None
                graph = None
                current_node = "N1"
                current_path= [current_node]
                conversation = []
                num_of_off_topic = 0
                num_of_uncertain = 0
                opening = ""

                def respond(chat_history, message):
                    # print("user message: ", message)
                    nonlocal first_interaction, retrieved
                    nonlocal flowchart, graph, current_node, current_path, conversation
                    nonlocal num_of_off_topic, num_of_uncertain, opening

                    conversation.append("Patient: " + message)

                    if first_interaction:
                        first_interaction = False
                        opening = message
                        first_message = f"Patient's demographics: {info_gathered}; Patient's concern: {message}"
                        # print("first message: ", first_message)
                        # RAG - retrieve the flowchart based on the first message
                        flowchart_choice = RAG_call(rag_file, first_message, llm, 5)
                        # print(flowchart_choice)
                        flowchart_choice = parse_rag_output(flowchart_choice)
                        # 3 special flowcharts
                        if flowchart_choice in ["Pelvic Pain In Women Flowchart", "Confusion In Older People Flowchart", "Lack Of Bladder Control In Older People Flowchart"]:
                            flowchart_choice = nested_flowchart(flowchart_choice)
                        # fetch the corresponding flowchart
                        flowchart_result = get_flowchart(flowchart_choice)
                        # unpack flowchart_result
                        if isinstance(flowchart_result, tuple):
                            print("Current Flowchart: ", flowchart_choice)
                            flowchart, graph = flowchart_result
                            retrieved = True
                        else:
                            # no relevant flowchart found
                            print("No Flowchart Retrieved: ", flowchart_choice)
                            first_interaction = True
                            history_langchain_format = format_conversation_history(conversation)
                            answer = LLM_external(message, LLM_external_prompt_mapping()[1], "Sorry, I am not authorized to help with this condition. Please consult a healthcare professional for personalized triage.", llm, history_langchain_format)
                            conversation.append("TriageMD: " + answer)
                            chat_history.append((message, answer))
                            if output_file:
                                with open(output_file, 'a') as log_file:
                                    log_file.write("Patient: " + "\n" + message + "\n")
                                    log_file.write("TriageMD: " + "\n" + answer + "\n")
                    if retrieved:
                        # flowchart following
                        print("conversation: ", conversation)
                        temp_node = current_node
                        temp_flowchart = flowchart
                        current_node, flowchart, graph, current_path, prompt_type, num_of_off_topic, num_of_uncertain = flowchart_following(flowchart, graph, conversation, current_node, current_path, llm, num_of_off_topic, num_of_uncertain)
                        print("current step for LLM_external: ", flowchart[current_node])

                        # reset num of off topic and num of not answered if node changed
                        if current_node != temp_node:
                            num_of_off_topic = 0
                            num_of_uncertain = 0
                        # avoid opening being classified as off topic
                        if len(conversation) == 1 and conversation[0].split("Patient: ")[1] == opening:
                            # print("opening: ", opening)
                            num_of_off_topic = 0

                        history_langchain_format = format_conversation_history(conversation)
                        # if receiving inconclusive or irrelevant answers for more than 3 times, trigger "go to see a doctor"
                        if num_of_uncertain > 3 or num_of_off_topic > 3:
                            answer = LLM_external(message, LLM_external_prompt_mapping()[1], "Sorry, I can't proceed due to the lack of information. Please consult a healthcare professional directly.", llm, history_langchain_format)
                        else:
                            answer = LLM_external(message, LLM_external_prompt_mapping()[prompt_type], flowchart[current_node], llm, history_langchain_format)
                        # print("LLM_external output: ", answer)
                        chat_history.append((message, answer))
                        conversation.append("TriageMD: " + answer)
                        # only keep the conversation history for the current node
                        if current_node != temp_node or flowchart != temp_flowchart:
                            conversation = [conversation[-1]]

                        print("current path: ", current_path)

                        # save the conversation log
                        if output_file:
                            with open(output_file, 'a') as log_file:
                                log_file.write("Patient: " + "\n" + message + "\n")
                                log_file.write("TriageMD: " + "\n" + answer + "\n")

                    return chat_history, ""
                    
                user_input.submit(respond, [chatbot, user_input], [chatbot, user_input])
        
        start_button.click(fn=info_gathering, inputs=[q0_name, q1_sex, q2_age], outputs=[chat_window, pre_collect, chatbot])

    demo.launch(share=True)
    


if __name__ == "__main__":
    
    args = args()
    flowchart_dir = args.flowchart_dir
    platform = args.platform
    model = args.model
    temperature = args.temperature
    output_file = args.log

    api_key = "YOUR_API_KEY"
    os.environ["OPENAI_API_KEY"] = api_key
    llm = platform_selection(platform, temperature, model)

    flowchart_description_file = os.path.join(flowchart_dir, "flowchart_descriptions.txt")
    UI_gradio(flowchart_description_file, llm)