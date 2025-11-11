import os, sys
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Utils.utils as utils

def create_retriever(filepath):
    """Create a FAISS retriever from the given text file, which is used for the retrieval agent."""
    
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

def retrieval_agent(filepath, query, llm, k, split=True, retrieve=False):
    """Retrieval agent to retrieve relevant flowcharts based on the patient input."""
    
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

def parse_decision_agent_output(input_obj):
    """Parse the output from the decision agent into final decisions."""
    
    # Handle both Pydantic object and dict
    if hasattr(input_obj, 'isOnTopic'):
        # Pydantic object
        if input_obj.isOnTopic == "No":
            return "off-topic"
        if input_obj.isUncertain == "Yes":
            return "uncertain"
        elif input_obj.isUncertain == "No":
            if input_obj.actualAnswer == "Yes":
                return "Yes"
            elif input_obj.actualAnswer == "No":
                return "No"
            else: 
                return "not answered"
        else:
            raise ValueError(f"Wrong output from decision_agent: {input_obj}")
    else:
        # Dict (backward compatibility)
        if input_obj['isOnTopic'] == "No":
            return "off-topic"
        if input_obj['isUncertain'] == "Yes":
            return "uncertain"
        elif input_obj['isUncertain'] == "No":
            if input_obj['actualAnswer'] == "Yes":
                return "Yes"
            elif input_obj['actualAnswer'] == "No":
                return "No"
            else: 
                return "not answered"
        else:
            raise ValueError(f"Wrong output from decision_agent: {input_obj}")
    
class DecisionOutput(BaseModel):
    isOnTopic: str = Field(description="'Yes' if the response is relevant to the question, otherwise 'No'.")
    isAnswered: str = Field(description="'Yes' if the response provides a yes or no answer, otherwise 'No'.")
    actualAnswer: str = Field(description="'Yes' if the patient answers affirmatively, 'No' if the patient answers negatively.")
    isUncertain: str = Field(description="'Yes' if the response expresses uncertainty (e.g., 'maybe', 'not sure', 'probably'), otherwise 'No'.")

def decision_agent(query, protocol, model, parse=True):
    """Decision agent to determine the next step based on the patient response and the current protocol question."""
    
    output_parser = PydanticOutputParser(pydantic_object=DecisionOutput)

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
    if parse:
        output = parse_decision_agent_output(judge)
        return output
    else:
        return judge
    
def chat_agent_prompt_mapping():
    """Mapping for chat agent prompts based on different scenarios."""
    prompt = {1: "Convey this to the patient",
              2: "Patient's response is off-topic, ask this again",
              3: "Patient's indicates uncertainty, try confirming this"}
    return prompt

def chat_agent(query, prompt, protocol, model, chat_history):
    """Chat agent to generate responses based on the patient input, prompt type, and current protocol question."""
    
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

def determine_next_step(flowchart, graph, prompt, current_node, current_path, model, num_of_off_topic=0, num_of_uncertain=0):
    """Determine the next step in the flowchart based on the patient response and current node."""
    
    prompt_type = 1 # default prompt type is 1
    if current_node in flowchart:
        print("current_node: ", current_node)

        # for question nodes
        if current_node.startswith("N"):
            decision = decision_agent(prompt, flowchart[current_node], model)
            print("while 1, first decision: ", decision)
            while decision not in ["Yes", "No", "off-topic", "uncertain", "not answered"]:
                # rerun the decision_agent
                decision = decision_agent(prompt, flowchart[current_node], model)
                print("in while 1, decision: ", decision)
            if decision in ["Yes", "No"]:
                next_node = utils.get_next_step(graph, current_node, decision)
                if next_node.startswith("F"):
                    new_flowchart = flowchart[next_node]
                    current_path.append(next_node)
                    print(f"switch to {new_flowchart}")
                    flowchart_result = utils.get_flowchart(new_flowchart)
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
        # for information nodes
        if current_node.startswith("I"):
            next_node = utils.get_next_step(graph, current_node, None)
            new_flowchart = flowchart[next_node]
            current_path.append(next_node)
            print(f"switch to {new_flowchart}")
            flowchart_result = utils.get_flowchart(new_flowchart)
            if isinstance(flowchart_result, tuple):
                flowchart, graph = flowchart_result
            else:
                raise ValueError(f"Referred to {new_flowchart}, but did not implement")
            current_node = "N1"
            current_path.append(current_node)
            
    return current_node, flowchart, graph, current_path, prompt_type, num_of_off_topic, num_of_uncertain