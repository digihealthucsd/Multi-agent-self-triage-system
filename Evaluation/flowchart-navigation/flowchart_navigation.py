import pandas as pd
import argparse
import os, sys
import glob

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.utils as utils
import System.system_implementation as triagemd

def unit_test_decision_agent(user_response_file, model, output_file):
    """Run decision agent on user responses and save the results."""

    df_response = pd.read_csv(user_response_file, encoding="latin-1")
    accuracy = []
    result_is_ontopic = []
    result_is_answered = []
    result_is_uncertain = []
    result_actual_answer = []
    for idx, row in df_response.iterrows():
        # if the user response is empty, skip
        if pd.isna(row["User_response"]):
            result_is_ontopic.append("N/A")
            result_is_answered.append("N/A")
            result_is_uncertain.append("N/A")
            result_actual_answer.append("N/A")
            accuracy.append("N/A")
            continue
        print("Processing user response: ", idx)
        user_response = row["User_response"]
        node_content = row["Node_content"]

        result = triagemd.decision_agent(query=[node_content, user_response], protocol=node_content, model=model, parse=False)

        result_is_ontopic.append(result["isOnTopic"])
        result_is_answered.append(result["isAnswered"])
        result_is_uncertain.append(result["isUncertain"])
        result_actual_answer.append(result["actualAnswer"])

    # save the result
    df_response["isOnTopic"] = result_is_ontopic
    df_response["isAnswered"] = result_is_answered
    df_response["isUncertain"] = result_is_uncertain
    df_response["actualAnswer"] = result_actual_answer
    df_response.to_csv(output_file, index=False)
    print("Successfully saved: ", output_file)

def evaluation_FF_unit_test_decision_agent(input_dir, model_list, llm, output_dir):
    """Evaluate decision agent unit test for multiple models."""
    
    for model_name in model_list:
        print(f"******* Decision Agent Unit Test for {model_name} ******")
        model_folder = os.path.join(input_dir, model_name)
        user_response_files = glob.glob(os.path.join(model_folder, "user_responses*.csv"))
        for file in user_response_files:
            print("Processing file: ", os.path.basename(file).split("user_responses_")[1])
            output_model_dir = os.path.join(output_dir, model_name)
            os.makedirs(output_model_dir, exist_ok=True)
            output_file = os.path.join(output_model_dir, os.path.basename(file).split("user_responses_")[1])
            if os.path.exists(output_file):
                continue
            unit_test_decision_agent(user_response_file=file, model=llm, output_file=output_file)
    print("******** Finished Unit Test for Decision Agent **********")

def args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--flowchart_dir", type=str, default="../Flowcharts")
    parser.add_argument("--platform", type=str, default="OPENAI")
    parser.add_argument("--system_model", type=str, default="gpt-4o-mini")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--output_dir", type=str, default="../")

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
    synthetic_dataset_dir = os.path.join(output_dir, "synthetic-dataset")
    user_responses_dir = os.path.join(synthetic_dataset_dir, "generated-responses")
    flowchart_navigation_folder = os.path.join(output_dir, "flowchart-navigation")
    results_folder = os.path.join(flowchart_navigation_folder, "results")

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
    num_of_user_responses = 5
    model_for_generation = {"gpt4o": gpt4o_flex, "deepseek_chat": deepseek_chat_flex, "gemini_lite": gemini_lite_flex, "claude_haiku": claude_haiku_flex}
    
    evaluation_FF_unit_test_decision_agent(input_dir=user_responses_dir, model_list=list(model_for_generation.keys()), llm=llm, output_dir=results_folder)