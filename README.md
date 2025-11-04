# Multi-agent Self-triage System with Medical Flowcharts
An open-source, multi-agent conversational self-triage system that guides LLMs using clinically validated medical flowcharts to provide transparent, auditable, and patient-friendly recommendations.

## Overview
Online health resources and large language models (LLMs) are increasingly used as a first point of contact for medical decision-making, yet their reliability in healthcare remains limited by low accuracy, lack of transparency, and susceptibility to unverified information.

This project introduces a conversational self-triage system that guides LLMs with 100 clinically validated flowcharts from the American Medical Association, providing a structured and auditable framework for patient decision support. The system uses a multi-agent framework:
- Retrieval agent: identifies the most relevant flowchart
- Decision agent: navigates the selected flowchart given user responses
- Chat agent: delivers patient-friendly guidance and next steps

> This software is for research and educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.

## Table of Contents
- [Overview](#overview)
- [Flowcharts](#flowcharts)
- [Setup](#setup)
- [Usage](#usage)
- [Demo](#demo)
- [Citation](#citation)
- [Contact](#contact)

## Flowcharts
The flowcharts used in this work are from [American Medical Association Family Medical Guide, 4th Edition](https://www.google.com/books/edition/American_Medical_Association_Family_Medi/LIDuEAAAQBAJ?hl=en&gbpv=0). The flowcharts cover a wide range of symptoms and demographic groups. We preprocessed them into 100 self-triage flowcharts.

- `Flowcharts/AMA_flowchart_description_preprocessed.csv` lists the targeted demographic group and description of each flowchart.
- `Flowcharts/flowchart_descriptions.txt` is a text version of the flowchart description used for retrieval.
- `Flowcharts/flowcharts.py` contains an example of a preprocessed graph-represented flowchart (Feeling Generally Ill Flowchart).

To access all flowcharts in full detail, obtain the original volume from the publisher. And we describe the flowchart preprocess in the Method section.


## Setup
To get started locally:
1. Create and activate a virtual environment (e.g., conda or venv).
2. Install dependencies:
   - Run: `python -m pip install -r requirements.txt`
3. Obtain API keys for model providers
   - For example, create an OpenAI API key [here](https://platform.openai.com/api-keys).
4. Configure your API key(s) in `Utils/utils.py` by adding them to the `set_up_api_keys()` function.


## Usage
- `System`: contains the scripts for multi-agent system implementation and a user interface demo.
- `Evaluation`: contains the scripts and result examples for the evaluation tasks
    - `synthetic-dataset`: contains the scripts for generating synthetic data (both opening statements and patient responses) with four different models. We also provide generated data samples for Feeling Generally Ill Flowchart.
    - `flowchart-retrieval`: contains the script for testing flowchart retrieval performance, as well as the example results for Feeling Generally Ill Flowchart.
    - `flowchart-navigation`: contains the script for testing flowchart navigation performance, as well as the example results for Feeling Generally Ill Flowchart.


## Demo
You can interact with the system through a web-based user interface for conversational self-triage.

**To run the demo:**
1. Run: `python System/user_interface.py`
2. The script will display two URLs:
   - First URL: for local use (localhost)
   - Second URL: for public access (if using a service like ngrok)

**Note:** Currently, `Flowcharts/flowcharts.py` only contains the Feeling Generally Ill Flowchart. To query about other symptoms, you'll need to add more flowcharts to the file.

## Citation
If you use this repository in academic work, please consider citing it. 

## Contact
If you have any questions, feel free to contact us via email at nyjliu@ucsd.edu or open a GitHub Issue.
