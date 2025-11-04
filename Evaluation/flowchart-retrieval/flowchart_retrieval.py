import pandas as pd
import argparse
import os, sys
import glob

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import System.system_implementation as triagemd
import Utils.utils as utils

def check_FR_completion(input_dir, task):
    """ Check whether the evaluation for flowchart retrieval has been completed."""
    
    if os.path.exists(input_dir) and os.path.isdir(input_dir):
        if task == "full":
            if glob.glob(os.path.join(input_dir, "*full.csv")): 
                return True
        else:
            if os.path.isdir(os.path.join(input_dir, task)):
                if len(glob.glob(os.path.join(input_dir, task, "evaluation_FR*.csv"))) == 20:
                    return True
                
    return False

def FR_full(df_openings, RAG_file, model, top_n, output_dir, split=True):
    """ Test all the generated openings for flowchart retrieval."""
    
    if split:
        print("********** Test All the Openings ****************")
        FR_include(df_openings, RAG_file, model, top_n, "full", output_dir)
    else: 
        print("******** Test Baseline for RAG *********")
        # LLM only, without RAG
        FR_include(df_openings, RAG_file, model, top_n, "baseline", output_dir, split)
    print("********** Finished Testing all the Openings ***************")

def FR_include(df, rag_file, model, top_n, i, output_dir, split=True):
    """ Test all the generated openings for flowchart retrieval."""
    
    accuracy = []
    answer = []
    retrieved_output = []
    top_n_accuracy = []
    
    for idx, row in df.iterrows():
        print("Processing opening: ", idx)
        label = row['Flowchart']
        opening = f"Patient's demographics: sex - {row['Sex']}, age - {row['Age']}; Patient's concern: {row['Opening']}"
        rag_output, retriever_output = triagemd.retrieval_agent(rag_file, opening, model, top_n, split, True)
        output = utils.parse_rag_output(rag_output)
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
    if split:
        df['Retrieved_output'] = retrieved_output # similarity search results
        df['Top_n'] = top_n_accuracy
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, f"evaluation_FR_include_result_{i}.csv"), index=False)

def evaluation_FR(opening_file_dir, RAG_file, model, output_dir):
    """ Evaluation for flowchart retrieval."""
    
    top_n = 10
    opening_files = glob.glob(os.path.join(opening_file_dir, "*.csv"))
    for file in opening_files:
        df_openings = pd.read_csv(file)
        model_used_for_generation = os.path.basename(file).split("evaluation_FR_generated_openings_")[1].split(".csv")[0]
        print("Current model for opening generation: ", model_used_for_generation)

        if not check_FR_completion(os.path.join(output_dir, model_used_for_generation), "full"):
            FR_full(df_openings=df_openings, RAG_file=RAG_file, model=model, top_n=top_n, output_dir=os.path.join(output_dir, model_used_for_generation))

        if not check_FR_completion(os.path.join(output_dir, model_used_for_generation), "baseline"):
            FR_full(df_openings=df_openings, RAG_file=RAG_file, model=model, top_n=top_n, output_dir=os.path.join(output_dir, model_used_for_generation), split=False)

def top_n_retrieved(retriever_output, label, n):
    """ Check whether the correct flowchart is in the top n retrieved results."""
    
    if any(label in item['content'] for item in retriever_output) == False:
        return 0
    else:
        for i in range(n):
            current = retriever_output[i]
            if label in current['content']:
                return i+1

def args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--flowchart_dir", type=str, default="../../Flowcharts")
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
    flowchart_description_file = os.path.join(flowchart_dir, "flowchart_descriptions.txt")
    synthetic_dataset_dir = os.path.join(output_dir, "synthetic-dataset")
    openings_dir = os.path.join(synthetic_dataset_dir, "generated-openings")
    retrieval_dir = os.path.join(output_dir, "flowchart-retrieval")
    results_dir = os.path.join(retrieval_dir, "results")

    # define models for evaluation
    utils.set_up_api_keys()

    # model for the system
    llm = utils.platform_selection(platform, temperature, model) # system 

    # Evaluation
    print()
    print("***********************************")
    print("START EVALUATION - FLOWCHART RETRIEVAL")
    evaluation_FR(opening_file_dir=openings_dir, RAG_file=flowchart_description_file, model=llm, output_dir=results_dir)