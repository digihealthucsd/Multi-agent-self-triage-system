import pandas as pd
import os
import numpy as np
import glob
<<<<<<< HEAD
=======
import matplotlib.pyplot as plt
>>>>>>> e945b45bb8c81334b3db2069277cab1f8f062918
from collections import defaultdict

def convert_model_names_for_plot(model_list):
    """Convert model names to a more readable format for plotting."""
    
    converted_list = []
    for model in model_list:
        parts = model.split("_")
        formatted = " ".join(part.capitalize() for part in parts)
        if formatted.lower().startswith("gpt"):
            formatted = formatted.replace("Gpt", "GPT", 1)
        elif formatted.lower().startswith("deepseek"):
            formatted = formatted.replace("Deepseek", "DeepSeek", 1)
        converted_list.append(formatted)
    return converted_list

def get_row_inaccuracy(row):
    """Determine the accuracy of a row based on the pattern and its criteria."""
    
    if row['Pattern'] in ["conclusive and minimalistic", "conclusive and descriptive", "vague or partially conclusive"]:
        return row['isUncertain'] == "No" and row['Answer'] != row['actualAnswer']
    elif row['Pattern'] == "inconclusive":
        return row['isUncertain'] == "No" and row['isAnswered'] == "Yes"
    elif row['Pattern'] == "irrelevant":
        return row['isOnTopic'] == "Yes"
    else:
        return False

def get_model_overall_accuracy(input_dir, model):
    """Calculate overall accuracy across all flowcharts for a given model."""
    
    flowchart_accuracies = []
    
    flowchart_files = glob.glob(os.path.join(input_dir, '*.csv'))

    for file in flowchart_files:
        df = pd.read_csv(file)
        df['is_correct'] = df.apply(lambda row: not get_row_inaccuracy(row), axis=1)
        flowchart_accuracies.append(df['is_correct'].mean())
    
    overall_accuracy = np.mean(flowchart_accuracies)
    print(f"Overall accuracy for {model}: {overall_accuracy}")
    return overall_accuracy * 100

<<<<<<< HEAD
def calculate_flowchart_navigation_overall_accuracy(input_dir, model_list):
    """Calculate overall accuracy for flowchart navigation across specified models."""
=======
def calculate_decision_overall_accuracy(input_dir, model_list):
    """Calculate overall accuracy for decision agent unit test across specified models."""

    print("Plotting overall accuracy for unit test (decision agent)...")
>>>>>>> e945b45bb8c81334b3db2069277cab1f8f062918
    
    accuracies = {}
    
    for model in model_list:
        model_folder = os.path.join(input_dir, model)
        model_accuracy = get_model_overall_accuracy(model_folder, model)
        accuracies[model] = model_accuracy
    
    print("Overall accuracies:", accuracies)
        
<<<<<<< HEAD
def calculate_flowchart_navigation_pattern_accuracy(input_dir, model):
=======
def calculate_decision_model_pattern_accuracy(input_dir, model):
>>>>>>> e945b45bb8c81334b3db2069277cab1f8f062918
    """Calculate the accuracy for each pattern in each flowchart for a given model, based on pattern criteria."""
    
    flowchart_files = glob.glob(os.path.join(input_dir, '*.csv'))

    pattern_counts = defaultdict(lambda: defaultdict(int))
    pattern_totals = defaultdict(int)

    for file in flowchart_files:
        df = pd.read_csv(file)  
        for _, row in df.iterrows():
            pattern = row['Pattern']
            pattern_totals[pattern] += 1
            if pattern in ["conclusive and minimalistic", "conclusive and descriptive", "vague or partially conclusive"]:
                if row['isUncertain'] == "No" and row['Answer'] == row['actualAnswer']:
                    pattern_counts[pattern]['certain_correct'] += 1
                elif row['isUncertain'] == "No" and row['Answer'] != row['actualAnswer']:
                    pattern_counts[pattern]['certain_incorrect'] += 1
                elif row['isUncertain'] == "Yes" and row['Answer'] == row['actualAnswer']:
                    pattern_counts[pattern]['uncertain_correct'] += 1
                elif row['isUncertain'] == "Yes" and row['Answer'] != row['actualAnswer']:
                    pattern_counts[pattern]['uncertain_incorrect'] += 1
            elif pattern == "inconclusive":
                if row['isUncertain'] == "Yes" and row['isAnswered'] == "Yes":
                    pattern_counts[pattern]['uncertain_answered'] += 1
                elif row['isUncertain'] == "Yes" and row['isAnswered'] == "No":
                    pattern_counts[pattern]['uncertain_not_answered'] += 1
                elif row['isUncertain'] == "No" and row['isAnswered'] == "Yes":
                    pattern_counts[pattern]['certain_answered'] += 1
                elif row['isUncertain'] == "No" and row['isAnswered'] == "No":
                    pattern_counts[pattern]['certain_not_answered'] += 1
            elif pattern == "irrelevant":
                if row['isOnTopic'] == "Yes":
                    pattern_counts[pattern]['on_topic'] += 1
                elif row['isOnTopic'] == "No":
                    pattern_counts[pattern]['off_topic'] += 1
        
    pattern_accuracies = {}
    for pattern, counts in pattern_counts.items():
        total = pattern_totals[pattern]
        correct = 0
        if pattern in ["conclusive and minimalistic", "conclusive and descriptive", "vague or partially conclusive"]:
            correct = counts['certain_correct'] + counts['uncertain_correct'] + counts['uncertain_incorrect']
        elif pattern == "inconclusive":
            correct = counts['certain_not_answered'] + counts['uncertain_not_answered'] + counts['uncertain_answered']
        elif pattern == "irrelevant":
            correct = counts['off_topic']
        accuracy = (correct / total) * 100 if total > 0 else 0
        pattern_accuracies[pattern] = accuracy
    
    print(f"Overall pattern accuracies for {model}: {pattern_accuracies}")

def calculate_decision_pattern_accuracy(input_dir, model_list):
    """Calculate pattern accuracies for each model."""
    print("=====================================")
<<<<<<< HEAD
    print("Calculating pattern accuracy for flowchart navigation...")
    
    for i in range(len(model_list)):
        model_folder = os.path.join(input_dir, model_list[i])
        calculate_flowchart_navigation_model_pattern_accuracy(model_folder, model_list[i])        
=======
    print("Calculating pattern accuracy for unit test (decision agent)...")
    
    for i in range(len(model_list)):
        model_folder = os.path.join(input_dir, model_list[i])
        calculate_decision_model_pattern_accuracy(model_folder, model_list[i])        
>>>>>>> e945b45bb8c81334b3db2069277cab1f8f062918
        
if __name__ == "__main__":
    current_dir = os.getcwd()
    results_folder = os.path.join(current_dir, "results")

<<<<<<< HEAD
    model_list = ["gpt4o", "claude_haiku", "gemini_lite", "deepseek_chat"]
    
    calculate_flowchart_navigation_overall_accuracy(results_folder, model_list)
    calculate_flowchart_navigation_pattern_accuracy(results_folder, model_list)
=======
    model_list = ["gpt4o", "claude_haiku", "gemini_lite", "deepseek_chat"] #
    
    calculate_decision_overall_accuracy(results_folder, model_list)
    calculate_decision_pattern_accuracy(results_folder, model_list)
>>>>>>> e945b45bb8c81334b3db2069277cab1f8f062918
