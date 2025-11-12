import os
import argparse
import gradio as gr

import system_implementation as triagemd
import Utils.utils as utils

def UI_gradio(rag_file, llm, output_file=None):
    """Gradio-based user interface for TriageMD."""

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
                    nonlocal first_interaction, retrieved
                    nonlocal flowchart, graph, current_node, current_path, conversation
                    nonlocal num_of_off_topic, num_of_uncertain, opening

                    conversation.append("Patient: " + message)

                    if first_interaction:
                        first_interaction = False
                        opening = message
                        first_message = f"Patient's demographics: {info_gathered}; Patient's concern: {message}"
                        # RAG - retrieve the flowchart based on the first message
                        flowchart_choice = triagemd.retrieval_agent(rag_file, first_message, llm, 5)
                        flowchart_choice = utils.parse_rag_output(flowchart_choice)
                        # 3 special flowcharts
                        if flowchart_choice in ["Pelvic Pain In Women Flowchart", "Confusion In Older People Flowchart", "Lack Of Bladder Control In Older People Flowchart"]:
                            flowchart_choice = utils.nested_flowchart(flowchart_choice)
                        # fetch the corresponding flowchart
                        flowchart_result = utils.get_flowchart(flowchart_choice)
                        # unpack flowchart_result
                        if isinstance(flowchart_result, tuple):
                            print("Current Flowchart: ", flowchart_choice)
                            flowchart, graph = flowchart_result
                            retrieved = True
                        else:
                            # no relevant flowchart found
                            print("No Flowchart Retrieved: ", flowchart_choice)
                            first_interaction = True
                            history_langchain_format = utils.format_conversation_history(conversation)
                            answer = triagemd.chat_agent(message, triagemd.chat_agent_prompt_mapping()[1], "Sorry, I am not authorized to help with this condition. Please consult a healthcare professional for personalized triage.", llm, history_langchain_format)
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
                        current_node, flowchart, graph, current_path, prompt_type, num_of_off_topic, num_of_uncertain = triagemd.determine_next_step(flowchart, graph, conversation, current_node, current_path, llm, num_of_off_topic, num_of_uncertain)
                        print("current step for chat_agent: ", flowchart[current_node])

                        # reset num of off topic and num of not answered if node changed
                        if current_node != temp_node:
                            num_of_off_topic = 0
                            num_of_uncertain = 0
                        # avoid opening being classified as off topic
                        if len(conversation) == 1 and conversation[0].split("Patient: ")[1] == opening:
                            num_of_off_topic = 0

                        history_langchain_format = utils.format_conversation_history(conversation)
                        # if receiving inconclusive or irrelevant answers for more than 3 times, trigger "go to see a doctor"
                        if num_of_uncertain > 3 or num_of_off_topic > 3:
                            answer = triagemd.chat_agent(message, triagemd.chat_agent_prompt_mapping()[1], "Sorry, I can't proceed due to the lack of information. Please consult a healthcare professional directly.", llm, history_langchain_format)
                        else:
                            answer = triagemd.chat_agent(message, triagemd.chat_agent_prompt_mapping()[prompt_type], flowchart[current_node], llm, history_langchain_format)
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

def args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--flowchart_dir", type=str, default="./Flowcharts")
    parser.add_argument("--platform", type=str, default="OPENAI")
    parser.add_argument("--model", type=str, default="gpt-4o-mini") #"gpt-4-0125-preview" "gpt-4o-mini"
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--log", type=str, default="study_log.txt")

    args, unknown = parser.parse_known_args()
    return args

if __name__ == "__main__":
    
    args = args()
    flowchart_dir = args.flowchart_dir
    platform = args.platform
    model = args.model
    temperature = args.temperature
    output_file = args.log

    utils.set_up_api_keys()
    llm = utils.platform_selection(platform, temperature, model)

    flowchart_description_file = os.path.join(flowchart_dir, "flowchart_descriptions.txt")
    UI_gradio(flowchart_description_file, llm)