import pandas as pd
import argparse
from pathlib import Path
import os, sys
import re
import glob 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.utils as utils

def patterns_with_definitions():
    """Define patterns with their definitions."""
    
    pattern_dict = {"conclusive and minimalistic": "clearly answer the question without additional reasoning, details, or repetition of the question.",
                    "conclusive and descriptive": "clearly answer the question and provide additional details, context, or elaboration to support the answer.",
                    "vague or partially conclusive": "lean towards an answer but include uncertainty or hedge the statement with ambiguous language.",
                    "inconclusive": "remain uncertain due to a lack of sufficient information, neither confirming nor denying the question.",
                    "irrelevant": "completely unrelated to the question but still make basic conversational sense."
                    }
    return pattern_dict

def check_user_response_completion(input_dir):
    """Check if the user response generation is completed."""
    
    if os.path.exists(input_dir) and os.path.isdir(input_dir):
        if len(glob.glob(os.path.join(input_dir, "user_responses*.csv"))) == 100:
            return True
    return False

def LLM_generate_user_responses(context, model, answer, num, pattern, definition):
    """Generate user responses using LLM."""
    
    prompt = ChatPromptTemplate.from_template(
        "Task: Provide {num} distinct ways to respond {answer} to the following question.\n"
        "Question: {context}\n"
        "Rules: 1. Responses should reflect natural and everyday language, as patients would phrase their answers conversationally with a triage nurse online."
        "2. Responses should be {pattern}: {definition}"
    )
    generation_chain = prompt | model | StrOutputParser()
    generation = generation_chain.invoke({"num": num, "answer": answer, "context": context, "pattern": pattern, "definition": definition})
    return generation

def LLM_generate_user_responses_claude(context, model, answer, num, pattern, definition):
    """Generate user responses using Claude."""
    
    system_prompt = (
        "Role: You are an assistant for a medical fiction author who is creating a character seeking help through an online triage system."
    )
    user_prompt = (
        "Task: Provide {num} distinct ways to respond {answer} to the following question.\n"
        "Question: {context}\n"
        "Rules: In order to reflect the natural variety of real-world triage interactions, the responses should be {pattern}: {definition}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", user_prompt),
        ]
    )
    generation_chain = prompt | model | StrOutputParser()
    generation = generation_chain.invoke({"num": num, "answer": answer, "context": context, "pattern": pattern, "definition": definition})
    return generation

def split_user_responses(answers, num):
    """Split the generated user responses into a list."""

    responses = re.findall(r'\d+\.\s*(.*?)(?=\n\d+\.|\Z)', answers.strip(), re.DOTALL) 
    output = [response.strip() for response in responses]
    if len(responses) == num:
        return output
    else:
        print("The number of responses doesn't meet the requirement: ", len(output))
        if len(output) > num:
            for i in range(num, len(output)):
                output[num-1] = output[num-1] + output[i]
            output = output[:num]
        elif len(output) < num:
            for i in range(len(output), num):
                output.append(None)
        return output
    
def generate_user_response_with_different_models(flowchart_list, model_dict, n, output_dir):
    """Generate user responses for all N nodes from all the flowcharts using different models and patterns."""
    
    pattern_dict = patterns_with_definitions()
    for model_name, model in model_dict.items():
        print("****** Model: {} *******".format(model_name))
        if check_user_response_completion(os.path.join(output_dir, model_name)):
            continue
        output_model_dir = os.path.join(output_dir, model_name)
        os.makedirs(output_model_dir, exist_ok=True)
        for f in flowchart_list:
            print("****** Flowchart: {} *******".format(f))
            if glob.glob(os.path.join(output_model_dir, f"*{f.replace(' ', '_')}.csv")):
                continue
            # initialize output
            output_flowchart = []
            output_node = []
            output_node_input = []
            output_user_response = []
            output_pattern = []
            output_answer = []
            # get flowchart
            flowchart_result = utils.get_flowchart(f)
            if isinstance(flowchart_result, tuple):
                flowchart, graph = flowchart_result
            else:
                raise ValueError("Refered to a flowchart - {}, but failed to get it!".format(f))
            for node in [key for key in flowchart if key.startswith("N")]:
                # YES
                # conclusive and minimalistic
                user_response_YES = LLM_generate_user_responses(context=flowchart[node], model=model, answer="YES", num=n, pattern="conclusive and minimalistic", definition=pattern_dict["conclusive and minimalistic"])
                user_response_YES = split_user_responses(user_response_YES, n)
                output_user_response.extend(user_response_YES)
                output_answer.extend(["Yes"]*n)
                output_pattern.extend(["conclusive and minimalistic"]*n)
                output_flowchart.extend([f]*n)
                output_node.extend([node]*n)
                output_node_input.extend([flowchart[node]]*n)
                # conclusive and descriptive
                user_response_YES = LLM_generate_user_responses(context=flowchart[node], model=model, answer="YES", num=n, pattern="conclusive and descriptive", definition=pattern_dict["conclusive and descriptive"])
                user_response_YES = split_user_responses(user_response_YES, n)
                output_user_response.extend(user_response_YES)
                output_answer.extend(["Yes"]*n)
                output_pattern.extend(["conclusive and descriptive"]*n)
                output_flowchart.extend([f]*n)
                output_node.extend([node]*n)
                output_node_input.extend([flowchart[node]]*n)
                # vague or partially conclusive
                user_response_YES = LLM_generate_user_responses(context=flowchart[node], model=model, answer="YES", num=n, pattern="vague or partially conclusive", definition=pattern_dict["vague or partially conclusive"])
                user_response_YES = split_user_responses(user_response_YES, n)
                output_user_response.extend(user_response_YES)
                output_answer.extend(["Yes"]*n)
                output_pattern.extend(["vague or partially conclusive"]*n)
                output_flowchart.extend([f]*n)
                output_node.extend([node]*n)
                output_node_input.extend([flowchart[node]]*n)
                # NO
                # conclusive and minimalistic
                user_response_NO = LLM_generate_user_responses(context=flowchart[node], model=model, answer="NO", num=n, pattern="conclusive and minimalistic", definition=pattern_dict["conclusive and minimalistic"])
                user_response_NO = split_user_responses(user_response_NO, n)
                output_user_response.extend(user_response_NO)
                output_answer.extend(['No']*n)
                output_pattern.extend(["conclusive and minimalistic"]*n)
                output_flowchart.extend([f]*n)
                output_node.extend([node]*n)
                output_node_input.extend([flowchart[node]]*n)
                # conclusive and descriptive
                user_response_NO = LLM_generate_user_responses(context=flowchart[node], model=model, answer="NO", num=n, pattern="conclusive and descriptive", definition=pattern_dict["conclusive and descriptive"])
                user_response_NO = split_user_responses(user_response_NO, n)
                output_user_response.extend(user_response_NO)
                output_answer.extend(['No']*n)
                output_pattern.extend(["conclusive and descriptive"]*n)
                output_flowchart.extend([f]*n)
                output_node.extend([node]*n)
                output_node_input.extend([flowchart[node]]*n)
                # vague
                user_response_NO = LLM_generate_user_responses(context=flowchart[node], model=model, answer="NO", num=n, pattern="vague or partially conclusive", definition=pattern_dict["vague or partially conclusive"])
                user_response_NO = split_user_responses(user_response_NO, n)
                output_user_response.extend(user_response_NO)
                output_answer.extend(['No']*n)
                output_pattern.extend(["vague or partially conclusive"]*n)
                output_flowchart.extend([f]*n)
                output_node.extend([node]*n)
                output_node_input.extend([flowchart[node]]*n)
                # inconclusive
                user_response_uncertain = LLM_generate_user_responses(context=flowchart[node], model=model, answer="", num=n, pattern="inconclusive", definition=pattern_dict["inconclusive"])
                user_response_uncertain = split_user_responses(user_response_uncertain, n)
                output_user_response.extend(user_response_uncertain)
                output_answer.extend(["not answered"]*n)
                output_pattern.extend(["inconclusive"]*n)
                output_flowchart.extend([f]*n)
                output_node.extend([node]*n)
                output_node_input.extend([flowchart[node]]*n)
                # irrelevant
                user_response_irrelevant = LLM_generate_user_responses(context=flowchart[node], model=model, answer="", num=n, pattern="irrelevant", definition=pattern_dict["irrelevant"])
                user_response_irrelevant = split_user_responses(user_response_irrelevant, n)
                output_user_response.extend(user_response_irrelevant)
                output_answer.extend(["off-topic"]*n)
                output_pattern.extend(["irrelevant"]*n)
                output_flowchart.extend([f]*n)
                output_node.extend([node]*n)
                output_node_input.extend([flowchart[node]]*n)
            # save the output
            output_file = os.path.join(output_model_dir, f"user_responses_{f.replace(' ', '_')}.csv")
            df_output = pd.DataFrame({"Flowchart": output_flowchart,
                                   "Node": output_node,
                                   "Node_content": output_node_input,
                                   "Pattern": output_pattern,
                                   "Answer": output_answer,
                                   "User_response": output_user_response})
            df_output.to_csv(output_file, index=False)
            print("Successfully saved: ", output_file)
    print("******** Finished Generating User Responses **********")

def fix_user_response(file_folder, models, num):
    """Fix the user responses that are not generated properly."""

    answer_dict = {"Yes": "YES", "No": "NO", "not answered": "", "off-topic": ""}
    final_failed_dict = {}

    for model_name, model in models.items():
        file_list = glob.glob(os.path.join(file_folder, model_name, "*.csv"))
        for file in file_list:
            df = pd.read_csv(file)
            if df["User_response"].isna().any():
                print(f"*** Fix the user response: {model_name} - {os.path.basename(file)}")
                # initialize failed list
                failed = []
                for i in range(int(len(df)/num)):
                    # check if the user response is empty
                    df_temp = df.iloc[i*num : (i+1)*num]
                    if df_temp["User_response"].isna().any():
                        print(f"Fixing {df_temp.iloc[0]['Node']} - pattern: {df_temp.iloc[0]['Pattern']} - {df_temp.iloc[0]['Node_content']}")
                        pattern = df_temp.iloc[0]["Pattern"]
                        definition = patterns_with_definitions()[pattern]
                        node_content = df_temp.iloc[0]["Node_content"]
                        answer = answer_dict[df_temp.iloc[0]["Answer"]]
                        # generate user response
                        if model_name == "claude_haiku":
                            print("claude prompt")
                            user_responses = LLM_generate_user_responses_claude(context=node_content, model=model, answer=answer, num=num, pattern=pattern, definition=definition)
                        else:
                            user_responses = LLM_generate_user_responses(context=node_content, model=model, answer=answer, num=num, pattern=pattern, definition=definition)
                        print("user_responses: ", user_responses)
                        user_responses = split_user_responses(user_responses, num)
                        j = 0
                        while None in user_responses:
                            # if regenerate for more than 3 times, break
                            if j > 2:
                                print(user_responses)
                                failed.append((os.path.basename(file), df_temp.iloc[0]["Node"]))
                                break
                            print("regenerate")
                            user_responses = LLM_generate_user_responses(context=node_content, model=model, answer=answer, num=num, pattern=pattern, definition=definition)
                            user_responses = split_user_responses(user_responses, num)
                            j = j + 1
                        # update the user response
                        df.loc[i*num:((i+1)*num-1), "User_response"] = user_responses
                # save the updated file
                df.to_csv(file, index=False)
                print("Successfully saved: ", file)
                if len(failed) > 0:
                    final_failed_dict[model_name] = failed
                    print("Failed:", failed)
    print("******** Finished Fixing User Responses **********")
    print("Final failed dict: ", final_failed_dict)
    
def args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--flowchart_dir", type=str, default="../Flowcharts")
    parser.add_argument("--platform", type=str, default="OPENAI")
    parser.add_argument("--system_model", type=str, default="gpt-4o-mini")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--output_dir", type=str, default=str(Path(__file__).parent.resolve()))

    args, _ = parser.parse_known_args()
    return args

if __name__ == "__main__":
    args = args()
    flowchart_dir = args.flowchart_dir
    platform = args.platform
    model = args.system_model
    temperature = args.temperature
    output_dir = args.output_dir

    # set file paths
    flowchart_description_eva_file = os.path.join(flowchart_dir, "flowchart_descriptions.txt")
    responses_dir = os.path.join(output_dir, "generated-responses")

    # define models for evaluation
    utils.set_up_api_keys()

    # model for the system
    llm = utils.platform_selection(platform, temperature, model) # system 
    gpt4o = utils.platform_selection("OPENAI", temperature, "gpt-4o")
    gpt4o_flex = utils.platform_selection("OPENAI", 0.5, "gpt-4o")
    gpt4o_mini = utils.platform_selection("OPENAI", temperature, "gpt-4o-mini")
    gpt41_mini = utils.platform_selection("OPENAI", temperature, "gpt-4.1-mini")
    gemini_lite = utils.platform_selection("GOOGLE", temperature, "gemini-2.0-flash-lite")
    gemini_lite_flex = utils.platform_selection("GOOGLE", 0.5, "gemini-2.0-flash-lite")
    claude_haiku = utils.platform_selection("ANTHROPIC", temperature, "claude-3-haiku-20240307")
    claude_haiku_flex = utils.platform_selection("ANTHROPIC", 0.5, "claude-3-haiku-20240307")
    deepseek_chat = utils.platform_selection("DEEPSEEK", temperature, "deepseek-chat")
    deepseek_chat_flex = utils.platform_selection("DEEPSEEK", 0.5, "deepseek-chat")

    # Evaluation
    print()
    print("***********************************")
    print("START EVALUATION - FLOWCHART FOLLOWING")
    model_for_generation = {"gpt4o": gpt4o_flex}
    flowchart_list = utils.get_flowchart_list()
    num_of_user_responses = 5
    # generate user responses
    generate_user_response_with_different_models(flowchart_list=flowchart_list, model_dict=model_for_generation, n=num_of_user_responses, output_dir=responses_dir)
    fix_user_response(file_folder=responses_dir, models=model_for_generation, num=num_of_user_responses)