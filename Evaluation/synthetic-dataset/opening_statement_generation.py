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

def LLM_generate_openings_brief(context, model, num):
    """Generate brief opening statements with demographics according to the flowchart description."""
    
    prompt = ChatPromptTemplate.from_template(
        "Task: Generate {num} distinct sets of patient demographics and BRIEF opening statements according to the following flowchart.\n"
        "Flowchart: {context}\n"
        "Template for each set:\n"
        "Sex: Male/Female\n"  
        "Age: A number followed by a unit (e.g., 25 years, 1 month)\n"  
        "Opening Statement: A conversational statement (in quotes) that the patient would use to raise their concern via online triage.\n"
        "Rules: 1. Ensure diversity in age, sex, and opening statements across the sets. 2. Each opening statement should be no more than 25 words in length."
    )
    opening_chain = prompt | model | StrOutputParser()
    opening = opening_chain.invoke({"num": num, "context": context})
    return opening

def LLM_generate_openings_detailed(context, model, num):
    """Generate detailed opening statements with demographics according to the flowchart description."""
    
    prompt = ChatPromptTemplate.from_template(
        "Task: Generate {num} distinct sets of patient demographics and DESCRIPTIVE opening statements according to the following flowchart.\n"
        "Flowchart: {context}\n"
        "Template for each set:\n"
        "Sex: Male/Female\n"  
        "Age: A number followed by a unit (e.g., 25 years, 1 month)\n"  
        "Opening Statement: A conversational statement (in quotes) that the patient would use to raise their concern via online triage.\n"
        "Rules: 1. Ensure diversity in age, sex, and opening statements across the sets. 2. Include relevant context, details, or accompanying symptoms in the opening statements. 3. Each opening statement should be at least 50 words in length."
    )
    opening_chain = prompt | model | StrOutputParser()
    opening = opening_chain.invoke({"num": num, "context": context})
    return opening

def check_list_size_for_split_openings(answer_list, num):
    """Check if the size of the list matches the required number. If not, adjust accordingly."""
    
    if len(answer_list) == num:
        return answer_list
    else:
        print("The number of answers doesn't align with the requirement.")
        # padding
        print("length of answer list: ", len(answer_list))
        
        if len(answer_list) > num:
            # if more opening sets were generated
            for i in range(num, len(answer_list)):
                answer_list[num-1] = answer_list[num-1] + answer_list[i]
            answer_list = answer_list[:num]
        else:
            # if less opening setes were generated
            for i in range(len(answer_list), num):
                answer_list.append(None)
                
        return answer_list
    
def split_opening_responses_into_list(answers, num):
    """Split the opening responses into separate lists: sex, age, and opening statements."""
    
    sex_pattern = r"(?:\*\*Sex:\*\*|Sex:) (Male|Female)"
    age_pattern = r"(?:\*\*Age:\*\*|Age:)\s*(\d+(?:\.\d)?\s*(?:months?|years?|weeks?|days?))"
    opening_pattern = r'(?:\*\*Opening Statement:\*\*|Opening Statement:)\s*\n?\s*"(.*?)"'

    sex_list = []
    age_list = []
    opening_list = []

    sex_list = re.findall(sex_pattern, answers)
    age_list = re.findall(age_pattern, answers)
    opening_list = re.findall(opening_pattern, answers)

    sex_list = check_list_size_for_split_openings(sex_list, num)
    age_list = check_list_size_for_split_openings(age_list, num)
    opening_list = check_list_size_for_split_openings(opening_list, num)

    return sex_list, age_list, opening_list

def generate_openings_with_different_models(input_file, models, num, output_dir):
    """Generate opening statements using different LLM models."""
        
    for key, model in models.items():
        print("****** Model: {} *******".format(key))
        if glob.glob(os.path.join(output_dir, f"*{key}.csv")):
            continue
        #initialize output
        sex_list = []
        age_list = []
        opening_list = []
        flowchart = []
        pattern = []
        
        with open(input_file, 'r') as file:
            
            for idx, line in enumerate(file):
                print("{}: Generating for {}".format(idx, line.split(' - ')[2]))
                
                brief_openings = LLM_generate_openings_brief(line, model, num)
                sex_brief, age_brief, opening_brief = split_opening_responses_into_list(brief_openings, num)
                
                detailed_openings = LLM_generate_openings_detailed(line, model, num)
                sex_detailed, age_detailed, opening_detailed = split_opening_responses_into_list(detailed_openings, num)

                sex_list.extend(sex_brief)
                age_list.extend(age_brief)
                opening_list.extend(opening_brief)
                flowchart.extend([line.split(' - ')[2]]*num)
                pattern.extend(["Brief"]*num)

                sex_list.extend(sex_detailed)
                age_list.extend(age_detailed)
                opening_list.extend(opening_detailed)
                flowchart.extend([line.split(' - ')[2]]*num)
                pattern.extend(["Detailed"]*num)

        generated_oepnings = {"Flowchart": flowchart,
                                   "Pattern": pattern,
                                   "Sex": sex_list,
                                   "Age": age_list,
                                   "Opening": opening_list}
        df_generated_openings = pd.DataFrame(generated_oepnings)
        os.makedirs(output_dir, exist_ok=True)
        output_file_path = os.path.join(output_dir, f"evaluation_FR_generated_openings_{key}.csv")
        df_generated_openings.to_csv(output_file_path, encoding='utf-8')
        print("Finished Generating Openings with {}".format(key))
        
    print("***** Finished Generating Openings *****")

def fix_opening(file_folder, flowchart_description_file, models, num):
    """Fix the empty openings in the generated opening files."""
    
    file_list = glob.glob(os.path.join(file_folder, "*.csv"))
    failed = []
    
    for f in file_list:
        df = pd.read_csv(f, encoding='utf-8')
        if df['Opening'].isna().any() or df["Sex"].isna().any() or df["Age"].isna().any():
            print("***** Fix Opening File: {} ******".format(os.path.basename(f)))
            for i in range(int(len(df)/num)):
                df_temp = df.iloc[i*num : (i+1)*num]
                if df_temp["Opening"].isna().any() or df_temp["Sex"].isna().any() or df_temp["Age"].isna().any():
                    print(f"Fixing {df_temp.iloc[0]['Flowchart']}: {df_temp.iloc[0]['Pattern']}")
                    flowchart_name = df_temp.iloc[0]['Flowchart']
                    
                    with open(flowchart_description_file, 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if flowchart_name in line:
                                break
                        else:
                            raise ValueError(f"{flowchart_name} was not found in the flowchart description file!")

                    pattern = df_temp.iloc[0]['Pattern']
                    model = models[os.path.basename(f).split("evaluation_FR_generated_openings_")[1].split(".csv")[0]]
                    
                    if pattern == "Brief":
                        openings = LLM_generate_openings_brief(line, model, num)
                    else:
                        openings = LLM_generate_openings_detailed(line, model, num)
                        
                    sex_list, age_list, opening_list = split_opening_responses_into_list(openings, num)

                    j = 1
                    while None in opening_list or None in sex_list or None in age_list:
                        if j > 3:
                            failed.append((os.path.basename(f), flowchart_name, pattern))
                            print(openings)
                            break
                        print("regenerate")
                        if pattern == "Brief":
                            openings = LLM_generate_openings_brief(line, model, num)
                        else:
                            openings = LLM_generate_openings_detailed(line, model, num)
                        sex_list, age_list, opening_list = split_opening_responses_into_list(openings, num)
                        j = j + 1
                    
                    df.loc[i*num:((i+1)*num-1), "Opening"] = opening_list
                    df.loc[i*num:((i+1)*num-1), "Sex"] = sex_list
                    df.loc[i*num:((i+1)*num-1), "Age"] = age_list
                    
            os.makedirs(os.path.join(file_folder, "new"), exist_ok=True)
            df.to_csv(os.path.join(file_folder, "new", os.path.basename(f)), index=False)
            print("Successfully saved")
            
    print("**** Finished Fixing all the Opening files *****")
    print("Failed: ", failed)
    
def args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--flowchart_dir", type=str, default="../../Flowcharts")
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
    flowchart_description_file = os.path.join(flowchart_dir, "flowchart_descriptions.txt")
    output_openings_dir = os.path.join(output_dir, "generated-openings")

    # define models for evaluation
    utils.set_up_api_keys()

    # model for generation
    gpt4o_flex = utils.platform_selection("OPENAI", 0.5, "gpt-4o")
    gemini_lite_flex = utils.platform_selection("GOOGLE", 0.5, "gemini-2.0-flash-lite")
    claude_haiku_flex = utils.platform_selection("ANTHROPIC", 0.5, "claude-3-haiku-20240307")
    deepseek_chat_flex = utils.platform_selection("DEEPSEEK", 0.5, "deepseek-chat")

    # Generate opening statements
    print()
    print("***********************************")
    print("START GENERATION - OPENING STATEMENTS")
    num_of_openings = 10 # define the number of opening statements for each flowchart
    model_for_generation = {"gpt4o": gpt4o_flex, "deepseek_chat": deepseek_chat_flex, "gemini_lite": gemini_lite_flex, "claude_haiku": claude_haiku_flex} # 
    generate_openings_with_different_models(input_file=flowchart_description_file, models=model_for_generation, num=num_of_openings, output_dir=output_openings_dir)
    fix_opening(output_openings_dir, flowchart_description_file, model_for_generation, num_of_openings)
