import pandas as pd
import numpy as np
import json
import system_implementation
import argparse
import networkx as nx
import os
import re
import ast
import glob 
import random
import time
from pydantic import BaseModel, Field
from typing import List, Dict
from sklearn.metrics import roc_curve, auc
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.messages import AIMessage, HumanMessage
from langchain.output_parsers import ResponseSchema, StructuredOutputParser, PydanticOutputParser
from pydantic import BaseModel
import google.generativeai as genai

def set_up_api_keys():
    openai_api_key = "YOUR_API_KEY"
    os.environ["OPENAI_API_KEY"] = openai_api_key
    gemini_api_key = "YOUR_API_KEY"
    genai.configure(api_key=gemini_api_key)
    anthropic_api_key = "YOUR_API_KEY"
    os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key
    deepseek_api_key = "YOUR_API_KEY"
    os.environ["DEEPSEEK_API_KEY"] = deepseek_api_key


def flowchart_categories():
    # divide 100 flowcharts into 10 categories
    general_medicine = ["Feeling Generally Ill Flowchart", "Unexplained Weight Loss Flowchart", "Overweight Flowchart", "Fever Flowchart", "Fever In Young Children Flowchart", "Fever In Children Flowchart", "Excessive Sweating Flowchart", "Slow Weight Gain In Young Children Flowchart"]
    neurology = ["Feeling Faint And Fainting Flowchart", "Dizziness Flowchart", "Headache Flowchart", "Numbness Or Tingling Flowchart", "Twitching And Trembling Flowchart", "Pain In The Face Flowchart", "Confusion Flowchart", "Confusion In Older People Flowchart", "Impaired Memory Flowchart", "Difficulty Speaking Flowchart"]
    mental_behavioral_health = ["Disturbing Thoughts Or Feelings Flowchart", "Unusual Behavior Flowchart", "Depression Flowchart", "Anxiety Flowchart", "Hallucinations Flowchart", "Nightmares Flowchart", "Difficulty Sleeping Flowchart", "Waking At Night In Children Flowchart", "Crying In Infants Flowchart"]
    dermatology = ["Hair Loss Flowchart", "General Skin Problems Flowchart", "Facial Skin Problems Flowchart", "Itchy Spots And Rashes Flowchart", "Itching Without A Rash Flowchart", "Rash With Fever Flowchart", "Raised Spots And Lumps Flowchart", "Abnormal Hair Growth In Women Flowchart", "Skin Problems In Young Children Flowchart", "Itching In Children Flowchart", "Swellings In Children Flowchart", "Swellings Under The Skin Flowchart"]
    eye_ent_oral_health = ["Painful Eye Flowchart", "Disturbed Or Impaired Vision Flowchart", "Earache Flowchart", "Noises In The Ear Flowchart", "Hearing Loss Flowchart", "Runny Nose Flowchart", "Sore Throat Flowchart", "Hoarseness Or Loss Of Voice Flowchart", "Toothache Flowchart", "Difficulty Swallowing Flowchart", "Sore Mouth Or Tongue Flowchart", "Bad Breath Flowchart"]
    pulmonology_cardiology = ["Coughing Flowchart", "Coughing Up Blood Flowchart", "Wheezing Flowchart", "Difficulty Breathing Flowchart", "Palpitations Flowchart", "Coughing In Children Flowchart", "Chest Pain Flowchart"]
    urology = ["Abnormally Frequent Urination Flowchart", "Abnormal Looking Urine Flowchart", "Painful Urination Flowchart", "Lack Of Bladder Control Flowchart", "Lack Of Bladder Control In Older People Flowchart"]
    gastroenterology = ["Vomiting Flowchart", "Recurring Vomiting Flowchart", "Abdominal Pain Flowchart", "Recurring Abdominal Pain Flowchart", "Swollen Abdomen Flowchart", "Gas And Belching Flowchart", "Diarrhea Flowchart", "Constipation Flowchart", "Abnormal Looking Stools Flowchart", "Vomiting In Infants Flowchart", "Diarrhea In Infants Flowchart", "Abdominal Pain In Children Flowchart"]
    musculoskeletal_system = ["Backache Flowchart", "Cramp Flowchart", "Painful Or Stiff Neck Flowchart", "Painful Arm Or Hand Flowchart", "Painful Leg Flowchart", "Painful Knee Flowchart", "Painful Shoulder Flowchart", "Painful Ankles Flowchart", "Swollen Ankles Flowchart", "Foot Problems Flowchart", "Limping In Children Flowchart"]
    reproductive_health = ["Painful Or Enlarged Testicles Flowchart", "Painful Intercourse In Men Flowchart", "Infertility In Men Flowchart", "Infertility In Women Flowchart", "Absent Periods Flowchart", "Heavy Periods Flowchart", "Painful Periods Flowchart", "Pelvic Pain In Women Flowchart", "Irregular Vaginal Bleeding Flowchart", "Abnormal Vaginal Discharge Flowchart", "Vaginal Irritation Flowchart", "Painful Intercourse In Women Flowchart", "Pain Or Lumps In The Breast Flowchart", "Breast Problems In New Mothers Flowchart"]

    flowchart_category_dict = {"General_Medicine": general_medicine, "Neurology": neurology, "Mental_and_Behavioral_Health": mental_behavioral_health, "Dermatology": dermatology, "Eye_Ear_Nose_Throat_and_Oral_Health": eye_ent_oral_health, "Pulmonology_and_Cardiology": pulmonology_cardiology, "Urology": urology, "Gastroenterology": gastroenterology, "Musculoskeletal_System": musculoskeletal_system, "Reproductive_Health": reproductive_health}

    return flowchart_category_dict


def get_flowchart_list(input_file):
    flowchart_list = pd.read_csv(input_file)['Flowchart'].unique()
    if len(flowchart_list) != 100:
        raise ValueError("Double check the flowchart list!")
    return flowchart_list


def check_list_size_for_split_openings(answer_list, num):
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
    # split the answers
    # assume the answers have the following patterns
    sex_pattern = r"(?:\*\*Sex:\*\*|Sex:) (Male|Female)"
    age_pattern = r"(?:\*\*Age:\*\*|Age:)\s*(\d+(?:\.\d)?\s*(?:months?|years?|weeks?|days?))"
    opening_pattern = r'(?:\*\*Opening Statement:\*\*|Opening Statement:)\s*\n?\s*"(.*?)"'

    sex_list = []
    age_list = []
    opening_list = []

    sex_list = re.findall(sex_pattern, answers)
    age_list = re.findall(age_pattern, answers)
    opening_list = re.findall(opening_pattern, answers)

    # chekc the size of each list
    sex_list = check_list_size_for_split_openings(sex_list, num)
    age_list = check_list_size_for_split_openings(age_list, num)
    opening_list = check_list_size_for_split_openings(opening_list, num)

    return sex_list, age_list, opening_list


def LLM_generate_openings_brief(context, model, num):
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


def generate_openings_with_different_models(input_file, models, num, output_dir):
    # generate openings together with demographics using the list of models
    
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
                # print(brief_openings)
                sex_brief, age_brief, opening_brief = split_opening_responses_into_list(brief_openings, num)
                detailed_openings = LLM_generate_openings_detailed(line, model, num)
                # print(detailed_openings)
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
    # Fix the empty rows in the generated opening files
    file_list = glob.glob(os.path.join(file_folder, "*.csv"))
    failed = []
    for f in file_list:
        df = pd.read_csv(f, encoding='utf-8')
        # if there is empty row in df
        if df['Opening'].isna().any() or df["Sex"].isna().any() or df["Age"].isna().any():
            print("***** Fix Opening File: {} ******".format(os.path.basename(f)))
            for i in range(int(len(df)/num)):
                df_temp = df.iloc[i*num : (i+1)*num]
                if df_temp["Opening"].isna().any() or df_temp["Sex"].isna().any() or df_temp["Age"].isna().any():
                    print(f"Fixing {df_temp.iloc[0]['Flowchart']}: {df_temp.iloc[0]['Pattern']}")
                    flowchart_name = df_temp.iloc[0]['Flowchart']
                    # find the line for the corresponding flowchart in the flowchart description file
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
                    # print(openings)
                    sex_list, age_list, opening_list = split_opening_responses_into_list(openings, num)

                    j = 1
                    while None in opening_list or None in sex_list or None in age_list:
                        # if regenerate for more than 3 times
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


def topic_file_valid(topic_files, selection):
    selection_files = [file for file in topic_files if selection in file]
    
    if len(selection_files) == 0:
        print("No file found for ", selection)
        return False
    if os.path.getsize(selection_files[0]) == 0:
        print("File is empty for ", selection)
        return False
    
    return True


def top_n_retrieved(retriever_output, label, n):
    if any(label in item['content'] for item in retriever_output) == False:
        return 0
    else:
        # label in retriever_output
        for i in range(n):
            current = retriever_output[i]
            if label in current['content']:
                return i+1


def FR_include(df, rag_file, model, top_n, i, output_dir, split=True):
    # Test a subset of the generated openings that their corresponding flowcharts are in the database
    # The label should be the corresponding flowcharts
    accuracy = []
    answer = []
    retrieved_output = []
    top_n_accuracy = []
    
    for idx, row in df.iterrows():
        print("Processing opening: ", idx)
        label = row['Flowchart']
        opening = f"Patient's demographics: sex - {row['Sex']}, age - {row['Age']}; Patient's concern: {row['Opening']}"
        rag_output, retriever_output = systemB_vanilla.RAG_call(rag_file, opening, model, top_n, split, True)
        output = systemB_vanilla.parse_rag_output(rag_output)
        answer.append(output)
        retrieved_output.append(retriever_output)
        # check accuracy
        if label in output:
            accuracy.append(1)
        else:
            accuracy.append(0)
        top_n_accuracy.append(top_n_retrieved(retriever_output, label, top_n))
    
    df['Answer'] = answer
    df['Accuracy'] = accuracy
    df['Retrieved_output'] = retrieved_output
    df['Top_n'] = top_n_accuracy
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, f"evaluation_FR_include_result_{i}.csv"), index=False)

def FR_exclude(df, rag_file, model, top_n, i, output_dir):
    # Test a subset of the generated openings that their corresponding flowcharts are not in the database
    # The label should be "no flowchart available"
    accuracy = []
    answer = []
    retrieved_output = []

    for idx, row in df.iterrows():
        print("Processing opening: ", idx)
        label = "no flowchart available"
        opening = f"Patient's demographics: sex - {row['Sex']}, age - {row['Age']}; Patient's concern: {row['Opening']}"
        rag_output, retriever_output = systemB_vanilla.RAG_call(rag_file, opening, model, top_n, True)
        output = systemB_vanilla.parse_rag_output(rag_output)
        answer.append(output)
        retrieved_output.append(retriever_output)
        # check accuracy
        if label in output:
            accuracy.append(1)
        else:
            accuracy.append(0)
    
    df['Answer'] = answer
    df['Accuracy'] = accuracy
    df['Retrieved_output'] = retrieved_output
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, f"evaluation_FR_exclude_result_{i}.csv"), index=False)


def FR_full(df_openings, RAG_file, model, top_n, output_dir, split=True):
    
    if split:
        print("********** Test All the Openings ****************")
        FR_include(df_openings, RAG_file, model, top_n, "full", output_dir)
    else: 
        print("******** Test Baseline for RAG *********")
        FR_include(df_openings, RAG_file, model, top_n, "baseline", output_dir, split)
    print("********** Finished Testing all the Openings ***************")


def FR_select_one_topic(RAG_file, df_openings, num, model, top_n, output_dir):
    # Only the flowcharts under the selected topic in the flowchart database
    # Test the openings for flowchart retrieval
    print("******** Select one topic ********")
    flowchart_categories_dict = flowchart_categories()
    for key, value in flowchart_categories_dict.items():
        print("Topic: ", key) 
        if glob.glob(os.path.join(output_dir, f"*{key}.csv")): # "*include*{key}.csv"
            continue
        # Create temporary rag file
        with open(RAG_file, 'r') as file:
            lines = file.readlines()
        # Extract the lines under the current topic
        extracted_lines = []
        for line in lines:
            if len(line.split(" - ")) >= 3:
                if line.split(" - ")[2].strip() in value:
                    extracted_lines.append(line)
        if len(extracted_lines) != len(value):
            raise ValueError("Failed to create temporary rag file!")
        # save the temporary rag file
        os.makedirs(output_dir, exist_ok=True)
        RAG_file_temp = os.path.join(output_dir, f"RAG_file_temp_{key}.txt")
        with open(RAG_file_temp, 'w') as file:
            file.writelines(extracted_lines)
        
        df_include = df_openings[df_openings['Flowchart'].isin(value)]
        df_exclude = df_openings[~df_openings['Flowchart'].isin(value)]
        if len(df_include) != (len(value)*2*num) or len(df_exclude) != ((100-len(value))*2*num):
            raise ValueError("Double check the temporary RAG file!")
        
        print("Start FR_include")
        FR_include(df_include, RAG_file_temp, model, top_n, key, output_dir)
        print(f"Successfully finished FR_include - {key}")
        print("Start FR_exclude")
        FR_exclude(df_exclude, RAG_file_temp, model, top_n, key, output_dir)
        print(f"Successfully finished FR_exclude - {key}")
    print("******* Finished Select-one-topic Evaluation ********")


def FR_leave_one_topic_out(RAG_file, df_openings, num, model, top_n, output_dir):
    # Remove the flowcharts under the selected topic from the flowchart database
    # Test the openings for flowchart retrieval
    print("******** Leave one topic out **********")
    flowchart_category_dict = flowchart_categories()
    for key, value in flowchart_category_dict.items():
        print("Topic: ", key)
        # if glob.glob(os.path.join(output_dir, f"*{key}*.csv")):
        #     continue
        topic_files = glob.glob(os.path.join(output_dir, f"*{key}*.csv"))
        include_file_valid = topic_file_valid(topic_files, "include")
        exclude_file_valid = topic_file_valid(topic_files, "exclude")
        if include_file_valid and exclude_file_valid:
            continue
        # Create temp rag file
        with open(RAG_file, 'r') as file: 
            lines = file.readlines()
        # Exclude the lines under the current topic
        extracted_lines = []
        for line in lines: 
            if len(line.split(" - ")) >= 3:
                if line.split(" - ")[2].strip() not in value:
                    extracted_lines.append(line)
        if len(extracted_lines) != (100 - len(value)):
            raise ValueError("Failed to create temporary rag file!")
        # Save the temporary rag file
        os.makedirs(output_dir, exist_ok=True)
        RAG_file_temp = os.path.join(output_dir, f"RAG_file_temp_{key}.txt")
        with open(RAG_file_temp, 'w') as file:
            file.writelines(extracted_lines)
        
        df_include = df_openings[~df_openings['Flowchart'].isin(value)]
        df_exclude = df_openings[df_openings['Flowchart'].isin(value)]

        if len(df_exclude) != (len(value)*2*num) or len(df_include) != ((100 - len(value))*2*num):
            raise ValueError("Double check the temporary RAG file!")
        
        if not exclude_file_valid:
            print("Start FR_exclude")
            FR_exclude(df_exclude, RAG_file_temp, model, top_n, key, output_dir)
            print(f"Successfully finished FR_exclude - {key}")
        if not include_file_valid:
            print("Start FR_include")
            FR_include(df_include, RAG_file_temp, model, top_n, key, output_dir)
            print(f"Successfully finished FR_include - {key}")
    print("********* Finished Leave-one-topic-out Evaluation *********")


def check_FR_completion(input_dir, task):

    # whether the folder for FR results with opening generated by the specific model exists
    if os.path.exists(input_dir) and os.path.isdir(input_dir):
        if task == "full":
            if glob.glob(os.path.join(input_dir, "*full.csv")): 
                return True
        else:
            # task is either "select_one_topic" or "leave_one_topic_out"
            if os.path.isdir(os.path.join(input_dir, task)):
            # whether the folder has the correct number of csv files
            # correct number : 20
                if len(glob.glob(os.path.join(input_dir, task, "evaluation_FR*.csv"))) == 20:
                    return True
    return False


def RAG_with_filtered_retrieved_output(retrieved_output, query, llm):
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
    return conversation


def evaluation_FR_thresholding(input_dir, model_list, method, model):
    # decide the best threshold for similarity search based on the ROC result
    # implement the thresholding rag
    best_threshold_dict = {}
    for model_name in model_list:
        print(f"****** FR Thresholding for {model_name} ******")
        model_folder = os.path.join(input_dir, model_name)
        roc_filepath = os.path.join(model_folder, "ROC_analysis_for_similarity_score_leave_one_topic_out.csv")
        # find the best threshold
        df_roc = pd.read_csv(roc_filepath)
        # compute the Youden's J for each row
        df_roc["Youden_J"] = df_roc["TPR"] - df_roc["FPR"]
        if method == 'average':
            agg = df_roc.groupby('Threshold')['Youden_J'].mean().reset_index()
        elif method == 'minimum':
            agg = df_roc.groupby('Threshold')['Youden_J'].min().reset_index()
        else:
            raise ValueError("Method must be 'average' or 'minimum'!")
        # best threshold with max aggregated J
        best_idx = agg['Youden_J'].idxmax()
        best_threshold = agg.loc[best_idx, 'Threshold']
        best_threshold_dict[model_name] = best_threshold
        # thresholding RAG
        df_full = pd.read_csv(os.path.join(model_folder, "evaluation_FR_include_result_full.csv"))
        df_full["Retrieved_output"] = df_full["Retrieved_output"].apply(safe_json_parser)
        # initialize output
        answer = []
        accuracy = []
        top_n_accuracy = []
        thresholded_retrieved_output = []

        for idx, row in df_full.iterrows():
            print("Processing opening: ", idx)
            retrieved_output = row["Retrieved_output"]
            label = row["Flowchart"]
            filtered_retrieved_output = [{"content": item["content"], "score": item["score"]} for item in retrieved_output if item["score"] < best_threshold] 
            thresholded_retrieved_output.append(filtered_retrieved_output)
            # print("num of filtered retrieved output: ", len(filtered_retrieved_output))
            opening = f"Patient's demographics: sex - {row['Sex']}, age - {row['Age']}; Patient's concern: {row['Opening']}"           
            rag_output = RAG_with_filtered_retrieved_output(filtered_retrieved_output, opening, model)
            output = systemB_vanilla.parse_rag_output(rag_output)
            # print("answer", output)
            answer.append(output)
            # check accuracy
            if label in output:
                accuracy.append(1)
            else:
                accuracy.append(0)
            # print("accuracy", accuracy)
            top_n_accuracy.append(top_n_retrieved(filtered_retrieved_output, label, len(filtered_retrieved_output)))

        df_full["Retrieved_output_with_thresholding"] = thresholded_retrieved_output
        df_full["Top_n_with_thresholding"] = top_n_accuracy
        df_full["Answer_with_thresholding"] = answer
        df_full["Accuracy_with_thresholding"] = accuracy
        df_full.to_csv(os.path.join(model_folder, "evaluation_FR_include_result_full_with_thresholding.csv"), index=False)

    print("********** Finished Testing all the Openings ***************")
    print("Best threshold: ", best_threshold_dict)
    

def evaluation_FR(opening_file_dir, RAG_file, num, model, output_dir):
    top_n = 10
    opening_files = glob.glob(os.path.join(opening_file_dir, "*.csv"))
    for file in opening_files:
        df_openings = pd.read_csv(file)
        model_used_for_generation = os.path.basename(file).split("evaluation_FR_generated_openings_")[1].split(".csv")[0]
        print("Current model for opening generation: ", model_used_for_generation)
        # # 100 flowcharts in the database
        # if not check_FR_completion(os.path.join(output_dir, model_used_for_generation), "full"):
        #     FR_full(df_openings=df_openings, RAG_file=RAG_file, model=model, top_n=top_n, output_dir=os.path.join(output_dir, model_used_for_generation))

        # # baseline for rag
        # if not check_FR_completion(os.path.join(output_dir, model_used_for_generation), "baseline"):
        #     FR_full(df_openings=df_openings, RAG_file=RAG_file, model=model, top_n=top_n, output_dir=os.path.join(output_dir, model_used_for_generation), split=False)

        # # select one topic
        # if not check_FR_completion(os.path.join(output_dir, model_used_for_generation), "select_one_topic"):
        #     FR_select_one_topic(RAG_file=RAG_file, df_openings=df_openings, num=num, model=model, top_n=top_n, output_dir=os.path.join(output_dir, model_used_for_generation, "select_one_topic"))
        
        # leave one topic out
        # if not check_FR_completion(os.path.join(output_dir, model_used_for_generation), "leave_one_topic_out"):
        #     FR_leave_one_topic_out(RAG_file=RAG_file, df_openings=df_openings, num=num, model=model, top_n=top_n, output_dir=os.path.join(output_dir, model_used_for_generation, "leave_one_topic_out"))


def safe_json_parser(text):
    try:
        # if valid JSON 
        return json.loads(text)
    except json.JSONDecodeError:
        # If JSON parsing fails, assume it's using single quotes and convert
        if 'np.float32(' in text:
            text = re.sub(r'np\.float32\(([^)]+)\)', r'\1', text)
        return ast.literal_eval(text)

    
def FR_ROC_analysis_for_similarity_score(input_dir, output_dir, output_str):
    # threshold: similarity score from retriever
    # generate ROC curve
    # TP: when the flowchart is in the database, it passed the similarity threshold and got retrieved.
    # TF: when the flowcharts is not in the database, none of the flowcharts passed the similarity threshold, so none of them got retrieved, the system returned “sorry i can’t help”
    # FP: when the flowchart is not in the database, but any of the flowcharts passed the similarity threshold and got retrieved, so the system returned a flowchart name while it should be “sorry i can’t help”
    # FN: when the flowchart is in the database, but the flowchart didn’t pass the threshold score and didn’t get retrieved while it should be
    
    flowchart_topic_list = list(flowchart_categories().keys())
    thresholds = np.linspace(0.1, 1.0, num=50)

    # initialize the output
    output_TP = []
    output_FP = []
    output_TN = []
    output_FN = []
    output_TPR = []
    output_FPR = []
    output_threshold = []
    output_topic = []

    for i, t in enumerate(thresholds):
        print("\nComputing for threshold: ", i)
        for topic in flowchart_topic_list:
            print(topic)
            # intialize
            tp = 0
            fp = 0
            tn = 0
            fn = 0

            include_file_name = f"evaluation_FR_include_result_{topic}.csv"
            exclude_file_name = f"evaluation_FR_exclude_result_{topic}.csv"
            df_include = pd.read_csv(os.path.join(input_dir, include_file_name))
            df_exclude = pd.read_csv(os.path.join(input_dir, exclude_file_name))
            # parse json
            df_include["Retrieved_output"] = df_include["Retrieved_output"].apply(safe_json_parser)
            df_exclude["Retrieved_output"] = df_exclude["Retrieved_output"].apply(safe_json_parser)

            for idx, row in df_include.iterrows():
                retrieved_output = row["Retrieved_output"]
                filtered_retrieved_output = [{"content": item["content"], "score": item["score"]} for item in retrieved_output if item["score"] < t]            
                label = row['Flowchart']
                if any(label in item["content"] for item in filtered_retrieved_output):
                    tp = tp + 1
                else:
                    fn = fn + 1
            for idx, row in df_exclude.iterrows():
                retrieved_output = row["Retrieved_output"]
                filtered_retrieved_output = [{"content": item["content"], "score": item["score"]} for item in retrieved_output if item["score"] < t]  
                if len(filtered_retrieved_output) == 0:
                    tn = tn + 1
                else:
                    fp = fp + 1

            output_threshold.append(t)
            output_topic.append(topic)
            output_TP.append(tp)
            output_FP.append(fp)
            output_TN.append(tn)
            output_FN.append(fn)
            output_TPR.append(tp/(tp+fn))
            output_FPR.append(fp/(fp+tn))
    output_csv = {"Threshold": output_threshold,
                  "Topic": output_topic,
                  "TP": output_TP,
                  "FP": output_FP,
                  "TN": output_TN,
                  "FN": output_FN,
                  "TPR": output_TPR,
                  "FPR": output_FPR}
    df_output = pd.DataFrame(output_csv)
    os.makedirs(output_dir, exist_ok=True)
    df_output.to_csv(os.path.join(output_dir, f"ROC_analysis_for_similarity_score_{output_str}.csv"))


def evaluation_FR_ROC(input_dir, model_list):
    for model in model_list:
        print(f"******* ROC Analysis for {model} ******")
        model_folder = os.path.join(input_dir, model)
        select_one_topic_folder = os.path.join(model_folder, "select_one_topic")
        leave_one_topic_out_folder = os.path.join(model_folder, "leave_one_topic_out")
        # select one topic
        if not os.path.exists(os.path.join(model_folder, "ROC_analysis_for_similarity_score_select_one_topic.csv")):
            print("Select One Topic: ")
            FR_ROC_analysis_for_similarity_score(select_one_topic_folder, model_folder, "select_one_topic")
        # leave one topic out
        if not os.path.exists(os.path.join(model_folder, "ROC_analysis_for_similarity_score_leave_one_topic_out.csv")):
            print("Leave One Topic Out:")
            FR_ROC_analysis_for_similarity_score(leave_one_topic_out_folder, model_folder, "leave_one_topic_out")


def patterns_with_definitions():
    pattern_dict = {"conclusive and minimalistic": "clearly answer the question without additional reasoning, details, or repetition of the question.",
                    "conclusive and descriptive": "clearly answer the question and provide additional details, context, or elaboration to support the answer.",
                    "vague or partially conclusive": "lean towards an answer but include uncertainty or hedge the statement with ambiguous language.",
                    "inconclusive": "remain uncertain due to a lack of sufficient information, neither confirming nor denying the question.",
                    "irrelevant": "completely unrelated to the question but still make basic conversational sense."
                    }
    return pattern_dict


def split_user_responses(answers, num):
    # split the responses into a list
    # find all the responses starting with a number and a dot
    responses = re.findall(r'\d+\.\s*(.*?)(?=\n\d+\.|\Z)', answers.strip(), re.DOTALL) 
    output = [response.strip() for response in responses]
    if len(responses) == num:
        return output
    else:
        print("The number of responses doesn't meet the requirement: ", len(output))
        # zero padding
        if len(output) > num:
            for i in range(num, len(output)):
                output[num-1] = output[num-1] + output[i]
            output = output[:num]
        elif len(output) < num:
            for i in range(len(output), num):
                output.append(None)
        return output
    

def check_user_response_completion(input_dir):
    # check if the user response generation is completed
    if os.path.exists(input_dir) and os.path.isdir(input_dir):
        if len(glob.glob(os.path.join(input_dir, "user_responses*.csv"))) == 100:
            return True
    return False


def LLM_generate_user_responses(context, model, answer, num, pattern, definition):
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


def generate_user_response_with_different_models(flowchart_list, model_dict, n, output_dir):
    # iterate through all N nodes from all the flowcharts
    # generate user responses with different models and different patterns
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
            flowchart_result = systemB_vanilla.get_flowchart(f)
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
    # fix the empty rows in the generated user response files
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
    

def check_accuracy_for_decision_agent(pattern, result_dict, answer):
    # check the accuracy for decision agent
    # for each pattern
    if pattern == "conclusive and minimalistic":
        if result_dict["isOnTopic"] == "Yes" and result_dict["isAnswered"] == "Yes" and result_dict["isUncertain"] == "No" and result_dict["actualAnswer"] == answer:
            return 1
        else:
            return 0
    elif pattern == "conclusive and descriptive":
        if result_dict["isOnTopic"] == "Yes" and result_dict["isAnswered"] == "Yes" and result_dict["isUncertain"] == "No" and result_dict["actualAnswer"] == answer:
            return 1
        else:
            return 0
    elif pattern == "vague or partially conclusive":
        if result_dict["isOnTopic"] == "Yes" and result_dict["isAnswered"] == "Yes" and result_dict["isUncertain"] == "Yes" and result_dict["actualAnswer"] == answer:
            return 1
        else:
            return 0
    elif pattern == "inconclusive":
        if result_dict["isOnTopic"] == "Yes" and result_dict["isAnswered"] == "No":
            return 1
        else:
            return 0
    elif pattern == "irrelevant":
        # pattern is irrelevant
        if result_dict["isOnTopic"] == "No":
            return 1
        else:
            return 0
    else:
        raise ValueError("Unknown pattern: {}".format(pattern))


def unit_test_decision_agent(user_response_file, model, output_file):
    # test the performance of the decision agent

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
        pattern = row["Pattern"]
        answer = row["Answer"]

        # get result from decision agent
        result = systemB_vanilla.LLM_internal(query=[node_content, user_response], protocol=node_content, model=model, parse=False)
        # parse the result
        result_is_ontopic.append(result["isOnTopic"])
        result_is_answered.append(result["isAnswered"])
        result_is_uncertain.append(result["isUncertain"])
        result_actual_answer.append(result["actualAnswer"])
        # check accuracy
        accuracy.append(check_accuracy_for_decision_agent(pattern, result, answer))
    # save the result
    df_response["isOnTopic"] = result_is_ontopic
    df_response["isAnswered"] = result_is_answered
    df_response["isUncertain"] = result_is_uncertain
    df_response["actualAnswer"] = result_actual_answer
    df_response["Accuracy"] = accuracy
    df_response.to_csv(output_file, index=False)
    print("Successfully saved: ", output_file)


def evaluation_FF_unit_test_decision_agent(input_dir, model_list, llm, output_dir):
    for model_name in model_list:
        print(f"******* Decision Agent Unit Test for {model_name} ******")
        model_folder = os.path.join(input_dir, model_name)
        user_response_files = glob.glob(os.path.join(model_folder, "user_responses*.csv"))
        for file in user_response_files:
            print("Processing file: ", os.path.basename(file).split("user_responses_")[1])
            output_model_dir = os.path.join(output_dir, model_name)
            os.makedirs(output_model_dir, exist_ok=True)
            output_file = os.path.join(output_model_dir, os.path.basename(file).split("user_responses_")[1])
            # check if the file already exists
            if os.path.exists(output_file):
                continue
            unit_test_decision_agent(user_response_file=file, model=llm, output_file=output_file)
    print("******** Finished Unit Test for Decision Agent **********")


def LLM_critic(protocol, response, model, type, chat_history):
    response_schemas = [
        ResponseSchema(name="followedInstruction", description="'Yes' if the response follows the instruction, otherwise 'No'.")
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

    prompt = ChatPromptTemplate.from_template(
        "Role: You are an experienced doctor overseeing a triage nurse.\n"
        "Task: Based on the triage instruction, nurse's response, and chat history, determine if the response follows the instruction. {format_instructions}\n"
        "Chat history: {chat_history}\n"
        "Nurse's response: {response}\n"
        "Triage instruction: {type}: {protocol}"
    ).partial(format_instructions=output_parser.get_format_instructions())

    critic_chain = prompt | model | output_parser
    critic = critic_chain.invoke({"protocol": protocol, "response": response, "type": type, "chat_history": chat_history})
    return critic


def handle_end_node(protocol):
    if "self-triage" in protocol:
        # if the protocol contains "self-triage" which means the flowchart couldn't help with it, chat agent would reframe it
        protocol = protocol.replace("if you are unable to make a decision from self-triage", "if you have concerns")
    return protocol


def unit_test_chat_agent(user_response_file, model, output_file, critic_model):
    df_response = pd.read_csv(user_response_file, encoding="latin-1")
    flowchart_name = os.path.splitext(os.path.basename(user_response_file))[0].split('_', 2)[-1]
    # get flowchart
    flowchart_result = systemB_vanilla.get_flowchart(flowchart_name)
    if isinstance(flowchart_result, tuple):
        flowchart, graph = flowchart_result
    else:
        raise ValueError("Refered to a flowchart - {}, but failed to get it!".format(flowchart_name))
    # initialize output
    accuracy = []
    result_next_node = []
    result_next_node_content = []
    result_prompt_type = []
    result_response = []
    result_followedInstruction = []

    for idx, row in df_response.iterrows():
        # if the user response is empty, skip
        if pd.isna(row["User_response"]):
            result_next_node.append("N/A")
            result_next_node_content.append("N/A")
            result_prompt_type.append("N/A")
            result_response.append("N/A")
            result_followedInstruction.append("N/A")
            accuracy.append("N/A")
            continue
        print("Processing user response: ", idx)
        # current protocol
        current_node = row["Node"]
        node_content = row["Node_content"]
        user_response = row["User_response"]
        condition = row["Answer"]
        # calculate next node protocol and get prompt type
        if condition in ["Yes", "No"]: # Get next node
            prompt_type = 1
            next_node = systemB_vanilla.get_next_step(graph, current_node, condition)
        elif condition == 'off-topic':
            prompt_type = 2
            next_node = current_node
        elif condition == 'not answered':
            prompt_type = 3
            next_node = current_node
        else:
            raise ValueError("Unknown condition: {}".format(condition))
        # print("next_node: ", next_node)
        if next_node.startswith("F"):  # link to another flowchart
            new_flowchart_name = flowchart[next_node]
            # print("Next node is a flowchart: ", new_flowchart_name)
            new_flowchart = systemB_vanilla.get_flowchart(new_flowchart_name)
            if isinstance(new_flowchart, tuple):
                new_flowchart_dict, new_graph = new_flowchart
                next_node_protocol = new_flowchart_dict["N1"]
            else:
                raise ValueError("Referred to a flowchart - {}, but failed to get it!".format(new_flowchart_name))
        else:  
            # continue in the same flowchart
            next_node_protocol = flowchart[next_node]

        # get the chat agent result
        conversation = [AIMessage(content=node_content), HumanMessage(content=user_response)] # format the chat history
        result = systemB_vanilla.LLM_external(query=user_response, prompt=systemB_vanilla.LLM_external_prompt_mapping()[prompt_type], protocol=next_node_protocol, model=model, chat_history=conversation)
        result_response.append(result)
        result_next_node.append(next_node)
        result_next_node_content.append(next_node_protocol)
        result_prompt_type.append(prompt_type)
        # check if the chat agent followed the protocol
        chat_history = ["Nurse: " + node_content + " Patient: " + user_response] # format the chat history
        # handle the end node
        next_node_protocol = handle_end_node(next_node_protocol)
        critic = LLM_critic(protocol=next_node_protocol, response=result, model=critic_model, type=systemB_vanilla.LLM_external_prompt_mapping()[prompt_type], chat_history=chat_history)
        result_followedInstruction.append(critic["followedInstruction"])
        # get accuracy
        if critic["followedInstruction"] == "Yes":
            accuracy.append(1)
        else:
            accuracy.append(0)
    df_response["Next_node"] = result_next_node
    df_response["Next_node_protocol"] = result_next_node_content
    df_response["Prompt_type"] = result_prompt_type
    df_response["Chat_agent_response"] = result_response
    df_response["followedInstruction"] = result_followedInstruction
    df_response["Accuracy"] = accuracy
    df_response.to_csv(output_file, index=False)
    print("Successfully saved: ", output_file)


def evaluation_FF_unit_test_chat_agent(input_dir, model_list, llm, critic_llm, output_dir):
    # test the performance of the chat agent
    for model_name in model_list:
        print(f"******* Chat Agent Unit Test for {model_name} ******")
        model_folder = os.path.join(input_dir, model_name)
        user_response_files = glob.glob(os.path.join(model_folder, "user_responses*.csv"))
        for file in user_response_files:
            print("Processing file: ", os.path.basename(file).split("user_responses_")[1])
            output_model_dir = os.path.join(output_dir, model_name)
            os.makedirs(output_model_dir, exist_ok=True)
            output_file = os.path.join(output_model_dir, os.path.basename(file).split("user_responses_")[1])
            # check if the file already exists
            if os.path.exists(output_file):
                continue
            unit_test_chat_agent(user_response_file=file, model=llm, output_file=output_file, critic_model=critic_llm)
    print("******** Finished Unit Test for Chat Agent **********")


def find_all_paths(flowchart_list):
    # find all the paths in the flowcharts
    path_dict = {}
    for flowchart in flowchart_list:
        flowchart_result = systemB_vanilla.get_flowchart(flowchart)
        if isinstance(flowchart_result, tuple):
            flowchart_dict, graph = flowchart_result
        else:
            raise ValueError("Referred to a flowchart - {}, but failed to get it!".format(flowchart))
        # find all the paths in the flowchart
        # print("Finding all paths in flowchart: ", flowchart)
        all_paths = []
        for node in graph.nodes():
            if len(list(graph.successors(node))) == 0:
                paths = list(nx.all_simple_paths(graph, source="N1", target=node))
                all_paths.extend(paths)
        # print(all_paths)
        # print("Total paths found: ", len(all_paths))
        path_dict[flowchart] = all_paths
            
    return path_dict


def get_condition(path, graph):
    # get the condition list for the path
    output = []
    for i in range(len(path)-1):
        current_node = path[i]
        next_node = path[i+1]
        output.append(graph[current_node][next_node]["condition"])
    return output


def LLM_patient_adult(question, conversation_history, model, answer, conversation_pattern, pattern_definition):
    
    system_prompt = (
        "Your role: You are a patient who is trying to triage your symptoms through online triage interface.\n"
        "Your task: Reply {answer} to nurse's question based on the conversation.\n"
        "Rules: 1. The response should reflect natural and everyday language, as patients would phrase their answer conversationally with a triage nurse online.\n"
        "2. The response style should be {conversation_pattern}: {pattern_definition}\n"
    )
    patient_agent_prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"), # nurse
            ("system", system_prompt),
        ]
    )
    patient_agent_chain = patient_agent_prompt | model | StrOutputParser()
    patient_agent = patient_agent_chain.invoke({"input": question, "answer": answer, "conversation_pattern": conversation_pattern, "pattern_definition": pattern_definition, "chat_history": conversation_history})
    return patient_agent
        

def LLM_patient_child(question, conversation_history, model, answer, conversation_pattern, pattern_definition):

    system_prompt = (
        "Your role: You are a parent who is trying to triage your child's symptoms through online triage interface.\n"
        "Your task: Reply {answer} to nurse's question based on the conversation.\n"
        "Rules: 1. The response should reflect natural and everyday language, as parents would phrase their answer conversationally with a triage nurse online.\n"
        "2. The response style should be {conversation_pattern}: {pattern_definition}"
    )
    patient_agent_prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"), # nurse
            ("system", system_prompt),
        ]
    )
    patient_agent_chain = patient_agent_prompt | model | StrOutputParser()
    patient_agent = patient_agent_chain.invoke({ "input": question, "answer": answer, "conversation_pattern": conversation_pattern, "pattern_definition": pattern_definition, "chat_history": conversation_history})
    return patient_agent


def generate_response_and_question_pair(adult, triage_question, conversation, triage_model, patient_model, condition, response_pattern, pattern_definition, flowchart, graph, current_node, current_path):
    qr_dict = {}
    qr_dict["Question"] = triage_question
    qr_dict["Pattern"] = response_pattern
    # generate the patient response
    history_langchain_format = systemB_vanilla.format_conversation_history(conversation)
    if adult:
        patient_response = LLM_patient_adult(triage_question, history_langchain_format, patient_model, condition, response_pattern, pattern_definition)
    else:
        patient_response = LLM_patient_child(triage_question, history_langchain_format, patient_model, condition, response_pattern, pattern_definition)
    print("Patient: ", patient_response)
    qr_dict["Patient_response"] = patient_response
    
    # update conversation
    conversation.append("Patient: " + patient_response)
    # decide the next step
    current_step, flowchart, _, current_path, prompt_type, _, _ = systemB_vanilla.flowchart_following(flowchart=flowchart, graph=graph, prompt=conversation, current_node=current_node, current_path=current_path, model=triage_model)
    print("protocol sent to LLM_external: ", flowchart[current_step])
    history_langchain_format = systemB_vanilla.format_conversation_history(conversation)
    # generate the triage question
    triage_question = systemB_vanilla.LLM_external(query=patient_response, prompt=systemB_vanilla.LLM_external_prompt_mapping()[prompt_type], protocol=flowchart[current_step], model=triage_model, chat_history=history_langchain_format)
    print("TriageMD: ", triage_question)
    # update conversation
    conversation.append("TriageMD: " + triage_question)
    qr_dict["Next_question"] = triage_question
    qr_dict["Protocol"] = flowchart[current_step]
    
    return qr_dict, triage_question, flowchart, current_step, current_path, conversation


def classify_tone(flowchart_description):
    # decide if the patient is above 12 years old
    
    age_range = flowchart_description.split(" - ")[0]
    print("age range: ", age_range)
    if age_range in ["0-6 months", "0-2 years", "0-5 years", "0-12 years", "2-12 years"]:
        adult = False
    else:
        adult = True
    return adult


def compute_num_of_n_nodes(selected_paths):
    # compute the number of N nodes in the selected paths
    output = 0
    for flowchart, path in selected_paths:
        for node in path:
            if node.startswith("N"):
                output += 1
    print("Total number of N nodes in selected paths: ", output)
    return output


def calculate_weight_for_patterns(num_of_n_node, pattern_weights):
    raw_counts = {k: v * num_of_n_node for k, v in pattern_weights.items()}
    int_counts = {k: int(v) for k, v in raw_counts.items()}
    remainder = num_of_n_node - sum(int_counts.values())
    if remainder > 0:
        # distribute the remainder
        # sort keys by the size of their decimal parts
        decimal_parts = sorted(raw_counts.items(), key=lambda item: item[1] - int(item[1]), reverse=True)
        # distribute the remainder to the keys with the largest decimal parts
        for i in range(remainder):
            int_counts[decimal_parts[i][0]] += 1
    return int_counts


def pick_response_pattern(actual_counts, target_ratios):
    total_counts_so_far = sum(actual_counts.values()) or 1
    print("total counts: ", total_counts_so_far)
    expected_counts = {k: target_ratios[k]*total_counts_so_far for k in target_ratios}
    print("expected counts: ", expected_counts)
    # reweight based on how much room is left for each pattern
    reweighted = {k: max(0.0001, expected_counts[k] - actual_counts.get(k,0)) for k in target_ratios} 
    print("reweighted: ", reweighted)

    total_weight = sum(reweighted.values())
    normalized_weights = {k: reweighted[k]/total_weight for k in reweighted}
    print("normalized weights: ", normalized_weights)
    # use weights to select the next pattern
    selected_pattern = random.choices(list(normalized_weights.keys()), list(normalized_weights.values()), k=1)[0]
    # update the weights
    actual_counts[selected_pattern] += 1
    print("selected pattern: ", selected_pattern)
    print("updated actual counts: ", actual_counts)

    return selected_pattern


def get_flowchart_description(input_file, flowchart_name):
    # get the flowchart description from the file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if flowchart_name in line:
            return line
    raise ValueError("Flowchart description for {} not found in {}".format(flowchart_name, input_file))


def generate_opening_for_conversations(flowchart_description, patient_model):
    generated_opening = LLM_generate_openings_brief(flowchart_description, patient_model, 1)
    sex_list, age_list, opening_list = split_opening_responses_into_list(generated_opening, 1)
    # one opening
    while len(sex_list) != 1 or len(age_list) != 1 or len(opening_list) != 1:
        print("Regenerating opening for flowchart: ", flowchart_description.split("-")[2])
        generated_opening = LLM_generate_openings_brief(flowchart_description, patient_model, 1)
        sex_list, age_list, opening_list = split_opening_responses_into_list(generated_opening, 1)
    # character
    sex = sex_list[0]
    age = age_list[0]
    opening = opening_list[0]

    return sex, age, opening


def generate_conversations(flowchart_list, flowchart_description_file, pattern_weights, triage_model, patient_model, output_file):
    # find all the paths 
    path_dict = find_all_paths(flowchart_list)
    # random sample 100 paths
    selected_paths = random.sample([(flowchart, path) for flowchart, paths in path_dict.items() for path in paths], 100)
    
    # output
    output_flowchart_name = []
    output_path = []
    output_path_label = []
    output_path_accuracy = []
    output_conversation = []
    output_qr_pair = []

    # generate conversations for selected paths
    for p in selected_paths:
        flowchart_name, path = p
        print("Processing flowchart: ", flowchart_name, " - Path: ", path)
        # get flowchart
        flowchart, graph = systemB_vanilla.get_flowchart(flowchart_name)
        # get flowchart description
        flowchart_description = get_flowchart_description(flowchart_description_file, flowchart_name)
        # get the condition list for the path
        condition_list = get_condition(path, graph)

        # conversation begins
        _, _, opening = generate_opening_for_conversations(flowchart_description, patient_model)
        adult = classify_tone(flowchart_description)
        print("opening statement: ", opening)
        # N1
        triage_question = systemB_vanilla.LLM_external(query=opening, prompt=systemB_vanilla.LLM_external_prompt_mapping()[1], protocol=flowchart["N1"], model=triage_model, chat_history=[])
        print("N1 question: ", triage_question)
        # initialization
        conversation = ["Patient: " + opening, "TriageMD: " + triage_question]
        current_node = "N1" 
        current_path = [current_node]
        qr_pairs = []

        j = 0
        while 0 <= j < len(condition_list):
            print("j: ", j)
            # select a response pattern
            response_pattern = random.choices(list(pattern_weights.keys()), list(pattern_weights.values()), k=1)[0]
            print("selected pattern: ", response_pattern)
            pattern_definition = patterns_with_definitions()[response_pattern]
            # generate patient response and triage question pairs
            if response_pattern in ["conclusive and minimalistic", "conclusive and descriptive", "vague or partially conclusive"]:
                condition = condition_list[j]
            else:
                condition = ""
            print("condition: ", condition)
            qr_dict, triage_question, flowchart_n, current_node, current_path, conversation = generate_response_and_question_pair(adult, triage_question, conversation, triage_model, patient_model, condition, response_pattern, pattern_definition, flowchart, graph, current_node, current_path)
            print("conversation history: ", conversation)
            # if ends up at another flowchart
            if flowchart_n != flowchart:
                current_path = current_path[:-1]
                current_node = current_path[-1] # the F node
                j = j + 1
            # go to the next step
            if response_pattern in ["conclusive and minimalistic", "conclusive and descriptive"]:
                j = j + 1
            qr_pairs.append(qr_dict)

        print("actual path: ", current_path)
        output_flowchart_name.append(flowchart_name)
        output_path_label.append(path)
        output_path.append(current_path)
        output_conversation.append(conversation)
        if current_path == path:
            output_path_accuracy.append(1)
        else:
            output_path_accuracy.append(0)
        print("ACCURACY: ", output_path_accuracy[-1])
        output_qr_pair.append(qr_pairs)

    output = {"Path label": output_path_label,
              "Path": output_path,
              "Accuracy": output_path_accuracy,
              "Conversation": output_conversation,
              "Question_and_response_pair": output_qr_pair}
    
    df_output = pd.DataFrame(output)
    df_output.to_csv(output_file)


def evaluation_have_conversations(flowchart_list, flowchart_description_file, pattern_weights, model, patient_model_list, output_dir):
    # evaluate the conversations
    for patient_model_name, patient_model in patient_model_list.items():
        print(f"******* Conversations for {patient_model_name} ******")
        output_model_dir = os.path.join(output_dir, patient_model_name)
        os.makedirs(output_model_dir, exist_ok=True)
        output_file = os.path.join(output_model_dir, "conversations.csv")
        if os.path.exists(output_file):
            continue
        generate_conversations(flowchart_list, flowchart_description_file, pattern_weights, model, patient_model, output_file)
    print("******** Finished Evaluation - Conversations **********")


def args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--flowchart_dir", type=str, default="../Flowcharts/from_book/Preprocess_AMA")
    parser.add_argument("--platform", type=str, default="OPENAI")
    parser.add_argument("--system_model", type=str, default="gpt-4o-mini")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--output_dir", type=str, default="../Evaluation")

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
    output_openings_dir = os.path.join(output_dir, "openings")
    FR_output_dir = os.path.join(output_dir, "FR_result")
    FF_output_dir = os.path.join(output_dir, "FF_result")
    FF_user_response_dir = os.path.join(FF_output_dir, "user_response")
    FF_unit_test_dir = os.path.join(FF_output_dir, "unit_test")
    conversation_dir = os.path.join(output_dir, "conversation")

    # define models for evaluation
    set_up_api_keys()

    # model for the system
    llm = systemB_vanilla.platform_selection(platform, temperature, model) # system 
    gpt4o = systemB_vanilla.platform_selection("OPENAI", temperature, "gpt-4o")
    gpt4o_flex = systemB_vanilla.platform_selection("OPENAI", 0.5, "gpt-4o")
    gpt4o_mini = systemB_vanilla.platform_selection("OPENAI", temperature, "gpt-4o-mini")
    gpt41_mini = systemB_vanilla.platform_selection("OPENAI", temperature, "gpt-4.1-mini")
    gemini_lite = systemB_vanilla.platform_selection("GOOGLE", temperature, "gemini-2.0-flash-lite")
    gemini_lite_flex = systemB_vanilla.platform_selection("GOOGLE", 0.5, "gemini-2.0-flash-lite")
    claude_haiku = systemB_vanilla.platform_selection("ANTHROPIC", temperature, "claude-3-haiku-20240307")
    claude_haiku_flex = systemB_vanilla.platform_selection("ANTHROPIC", 0.5, "claude-3-haiku-20240307")
    deepseek_chat = systemB_vanilla.platform_selection("DEEPSEEK", temperature, "deepseek-chat")
    deepseek_chat_flex = systemB_vanilla.platform_selection("DEEPSEEK", 0.5, "deepseek-chat")

    # Evaluation
    print()
    print("***********************************")
    print("START EVALUATION - FLOWCHART RETRIEVAL")
    num_of_openings = 10
    model_for_generation = {"gpt4o": gpt4o_flex} # , "deepseek_chat": deepseek_chat_flex, "gemini_lite": gemini_lite_flex, "claude_haiku": claude_haiku_flex
    # generate_openings_with_different_models(input_file=flowchart_description_eva_file, models=model_for_generation, num=num_of_openings, output_dir=output_openings_dir)
    # fix_opening(output_openings_dir, flowchart_description_eva_file, model_for_generation, num_of_openings)
    # evaluation_FR(opening_file_dir=output_openings_dir, RAG_file=flowchart_description_eva_file, model=llm, num=num_of_openings, output_dir=os.path.join(FR_output_dir, "gpt4o-mini"))
    # evaluation_FR_ROC(input_dir=os.path.join(FR_output_dir, "gpt4o-mini"), model_list=list(model_for_generation.keys()))
    # evaluation_FR_thresholding(input_dir=os.path.join(FR_output_dir, "gpt4o-mini"), model_list=list(model_for_generation.keys()), method="average", model=llm)

    print("START EVALUATION - FLOWCHART FOLLOWING")
    flowchart_list = get_flowchart_list(os.path.join(output_openings_dir, "evaluation_FR_generated_openings_gpt4o.csv"))
    num_of_user_responses = 5
    # generate user responses
    # generate_user_response_with_different_models(flowchart_list=flowchart_list, model_dict=model_for_generation, n=num_of_user_responses, output_dir=FF_user_response_dir)
    # fix_user_response(file_folder=FF_user_response_dir, models=model_for_generation, num=num_of_user_responses)
    # evaluation_FF_unit_test_decision_agent(input_dir=FF_user_response_dir, model_list=list(model_for_generation.keys()), llm=llm, output_dir=os.path.join(FF_unit_test_dir, "decision_agent"))
    # evaluation_FF_unit_test_chat_agent(input_dir=FF_user_response_dir, model_list=list(model_for_generation.keys()), llm=llm, critic_llm=gpt41_mini, output_dir=os.path.join(FF_unit_test_dir, "chat_agent"))
    
    print("START EVALUATION - CONVERSATION")
    pattern_weights = {"conclusive and minimalistic": 0.4, "conclusive and descriptive": 0.25, "vague or partially conclusive": 0.2, "inconclusive": 0.1, "irrelevant": 0.05}
    evaluation_have_conversations(flowchart_list=flowchart_list, flowchart_description_file=flowchart_description_eva_file, pattern_weights=pattern_weights, model=llm, patient_model_list=model_for_generation, output_dir=conversation_dir)
