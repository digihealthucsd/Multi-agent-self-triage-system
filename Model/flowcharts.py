import networkx as nx

# ten examples of the flowcharts from AMA
# for the complete version of flowcharts, please refer to American Medical Association Family Medical Guide, 4th Edition



def Diarrhea_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you had other episodes of diarrhea in the past few weeks?"
    flowchart['N2'] = "Do the attacks occur when you are under stress?"
    flowchart['A1'] = "See your doctor. Stress can often cause diarrhea. If you have episodes of cramping abdominal pain with alternating episodes of constipation and diarrhea, you may have irritable bowel syndrome."
    flowchart['N3'] = "Have you felt ill or have you been vomiting?"
    flowchart['A2'] = "You may have inflammation of the digestive tract."
    flowchart['N4'] = "Have you eaten food that may have spoiled, or do you think you may be allergic to a food you ate recently?"
    flowchart['A3'] = "Call your doctor if the symptoms last longer than 48 hours. You may have food poisoning, especially if other people who ate the same food have the same symptoms. Or you could have an allergy to food."
    flowchart['N5'] = "Is there blood or pus in your stools?"
    flowchart['A4'] = "See a doctor immediately. Blood or pus in stools could result from an inflammatory bowel disease."
    flowchart['N6'] = "Have you recently started taking any medication?"
    flowchart['A5'] = "See your doctor. Sensitivity to some drugs can cause diarrhea."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage and your diarrhea persists for more than 48 hours or recurs."
    flowchart['N7'] = "Do you have pain in the lower part of your abdomen?"
    flowchart['F1'] = "Abdominal Pain Flowchart" # change to abdominal pain flowchart
    
    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N7", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "A6", "No"),
        ("N7", "N5", "No"),
        ("N7", "F1", "Yes")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Coughing_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is the cough dry?"
    flowchart['N2'] = "Are you hoarse, or have you lost your voice?"
    flowchart['F1'] = "Hoarseness Or Loss Of Voice Flowchart" # change to hoarseness or loss of voice flowchart
    flowchart['N3'] = "Could you have inhaled a small object or piece of food (such as a peanut)?"
    flowchart['A1'] = "See your doctor if coughing fails to clear your lungs or continues for more than an hour."
    flowchart['N4'] = "Have you inhaled the fumes of an irritating chemical such as a cleaning fluid that contains ammonia?"
    flowchart['A2'] = "See your doctor. The fumes have probably irritated your lungs and caused the coughing."
    flowchart['N5'] = "Do you have a dry cough with no other symptoms?"
    flowchart['N6'] = "Is your cough deep, raspy, and persistent?"
    flowchart['A3'] = "See your doctor. You may have a form of asthma."
    flowchart['N7'] = "Are you currently taking any medication?"
    flowchart['A4'] = "Talk to your doctor. A dry cough is a side effect of some drugs."
    flowchart['N8'] = "Is your cough often worse when you are lying down or when you wake up in the morning?"
    flowchart['A5'] = "See a doctor immediately. You could have gastroesophageal reflux disease."
    flowchart['A6'] = "See a doctor immediately. A dry cough may be a symptom of a tumor."
    flowchart['N9'] = "Did your cough begin recently?"
    flowchart['N10'] = "Is your temperature 100°F or higher?"
    flowchart['N11'] = "Are you short of breath?"
    flowchart['A7'] = "See a doctor immediately. You may have pneumonia, acute bronchitis or influenza."
    flowchart['N12'] = "Does your cough sound like wheezing?"
    flowchart['A8'] = "See your doctor. You may have asthma."
    flowchart['N13'] = "Do you have a runny nose or a sore throat?"
    flowchart['A9'] = "You probably have a cold."
    flowchart['A10'] = "See your doctor. You may have a mild form of viral pneumonia."
    flowchart['N14'] = "Are you short of breath, even when you're relaxing?"
    flowchart['A11'] = "See a doctor immediately. You could have congestive heart failure."
    flowchart['N15'] = "Did your cough begin after you had the flu, or have you had similar episodes of persistent coughing in the past?"
    flowchart['A12'] = "See your doctor. You may have chronic bronchitis or a persistent, mild form of bronchitis that sometimes lingers after influenza."
    flowchart['N16'] = "Have you had the cough for several weeks or months, and is it getting worse?"
    flowchart['A13'] = "See a doctor immediately. You could have tuberculosis or lung cancer."
    flowchart['A14'] = "See your doctor if you are unable to make a decision from self-triage."

    edges_with_conditions = [
        ("N1", "N2", "Yes"), ("N1", "N9", "No"),
        ("N2", "F1", "Yes"), ("N2", "N3", "No"),
        ("N3", "A1", "Yes"), ("N3", "N4", "No"),
        ("N4", "A2", "Yes"), ("N4", "N5", "No"),
        ("N5", "N6", "Yes"), ("N5", "N9", "No"),
        ("N6", "A3", "Yes"), ("N6", "N7", "No"),  
        ("N7", "A4", "Yes"), ("N7", "N8", "No"),
        ("N8", "A5", "Yes"), ("N8", "A6", "No"),
        ("N9", "N10", "Yes"), ("N9", "N14", "No"),
        ("N10", "N11", "Yes"), ("N10", "N12", "No"),
        ("N11", "A7", "Yes"), ("N11", "A10","No"),
        ("N12", "A8", "Yes"), ("N12", "N13", "No"),
        ("N13", "A9", "Yes"), ("N13", "N14", "No"),
        ("N14", "A11", "Yes"), ("N14", "N15", "No"),
        ("N15", "A12", "Yes"), ("N15", "N16", "No"),
        ("N16", "A13", "Yes"), ("N16", "A14", "No")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G



def Headache_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your temperature 100°F or higher?"
    flowchart['N2'] = "Is the pain severe?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have meningitis, a life-threatening infection of the brain. Or you could have bleeding inside your brain."
    flowchart['N3'] = "Have you injured your head recently?"
    flowchart['N4'] = "Is it painful to bend your head forward, or does light hurt your eyes?"
    flowchart['A2'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have bleeding in your brain."
    flowchart['I1'] = "Headaches often occur with fevers."
    flowchart['F1'] = "Fever Flowchart" # change to fever flowchart
    flowchart['N5'] = "Do you feel unusually drowsy, or have you felt nauseous or been vomiting?"
    flowchart['A3'] = "See your doctor. A persistent headache is common after a head injury."
    flowchart['N6'] = "Have you felt nauseous or been vomiting?"
    flowchart['N7'] = "Do you have severe pain in and around one eye, or is your vision blurred?"
    flowchart['A4'] = "See a doctor immediately. You may have a migraine or a cluster headache. Or the pressure inside your eyeball may be increased, which can affect vision."
    flowchart['N8'] = "Do you also have any of the following symptoms: pain when you bend your head forward; drowsiness or confusion; fever?"
    flowchart['A5'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have meningitis, a life-threatening infection of the brain. Or you could have bleeding inside your brain."
    flowchart['N9'] = "Was the pain preceded by visual disturbances, and does bright light hurt your eyes?"
    flowchart['A6'] = "See your doctor. You may have a migraine, particularly if you also feel nauseous or are vomiting."
    flowchart['N10'] = "Have you had a similar headache on waking up several days in the past week?"
    flowchart['N11'] = "Do the headaches occur only after you have consumed a lot of alcohol the night before?"
    flowchart['A7'] = "You probably have a hangover."
    flowchart['N12'] = "Are you currently taking any medications?"
    flowchart['A8'] = "Talk to your doctor. Some drugs can cause headaches."
    flowchart['A9'] = "See a doctor immediately. Such headaches may be a symptom of anxiety, high blood pressure, or, in very rare cases, a brain tumor. They can also indicate carbon monoxide poisoning."
    flowchart['N13'] = "Do you or did you recently have a stuffy or runny nose?" 
    flowchart['N14'] = "Do you have sharp pain in and around one eye or on one side of your face that has recurred over several days?"
    flowchart['A10'] = "See your doctor. You may have cluster headaches."
    flowchart['N15'] = "Do you have dull pain and tenderness around the eyes and cheekbones that worsen when you bend forward?"
    flowchart['A11'] = "See your doctor. You may have a sinus infection."
    flowchart['A12'] = "Headaches are a common symptom of colds."
    flowchart['N16'] = "Are you feeling anxious or under stress, or are you having difficulty sleeping?"
    flowchart['A13'] = "See your doctor. Anxiety, stress, and lack of sleep often cause headaches."
    flowchart['N17'] = "Did the headache occur after you had been reading or doing close-up work such as sewing?"
    flowchart['A14'] = "Talk to your doctor. Strain on your neck muscles may have caused a tension headache. See your eye doctor if you wear glasses; you may need a new prescription."
    flowchart['N18'] = "Did any of the following occur within the 12 hours before your headache started: you were exposed to strong sunlight; you were in stuffy, smoky, or noisy surroundings; you drank more alcohol than usual; you missed a meal?"
    flowchart['A15'] = "These factors often bring on headaches."
    flowchart['A16'] = "See your doctor if you are unable to make a decision from self-triage and your headache persists overnight or if you develop other symptoms."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "N4", "Yes"),
        ("N2", "I1", "No"),
        ("I1", "F1", None),
        ("N3", "N5", "Yes"),
        ("N3", "N6", "No"),
        ("N4", "A1", "Yes"),
        ("N4", "F1", "No"),
        ("N5", "A3", "No"), 
        ("N5", "A2", "Yes"),
        ("N6", "N7", "Yes"), 
        ("N6", "N12", "No"),
        ("N7", "A4", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A5", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A6", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "N11", "Yes"),
        ("N10", "N12", "No"),
        ("N11", "A7", "Yes"),
        ("N11", "A9", "No"),
        ("N12", "A8", "Yes"),  
        ("N12", "N13", "No"),
        ("N13", "N14", "Yes"), 
        ("N13", "N16", "No"),
        ("N14", "A10", "Yes"),
        ("N14", "N15", "No"),
        ("N15", "A11", "Yes"),
        ("N15", "A12", "No"),
        ("N16", "A13", "Yes"),
        ("N16", "N17", "No"),
        ("N17", "A14", "Yes"),
        ("N17", "N18", "No"),
        ("N18", "A15", "Yes"),
        ("N18", "A16", "No")
    ]
    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Chest_Pain_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is the pain pressing or crushing, or does it radiate out from your chest to other parts of your body (such as your breastbone, the upper part of your abdomen, or your jaw, neck, or arms)?"
    flowchart['N2'] = "Is this the first time you have had this type of chest pain?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may be having a heart attack."
    flowchart['N3'] = "Is the pain similar to that of a previous heart attack?"
    flowchart['A2'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may be having a heart attack, although your chest pain could be angina caused by heart disease."
    flowchart['N4'] = "Are you short of breath?"
    flowchart['N5'] = "Have you recently had surgery, or has an injury or illness kept you in bed?"
    flowchart['A3'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have a blood clot in a lung."
    flowchart['N6'] = "Are you coughing, and is your temperature 100°F or higher?"
    flowchart['A4'] = "See a doctor immediately. You may have acute bronchitis or pneumonia."
    flowchart['A5'] = "See a doctor immediately. You may have a collapsed lung."
    flowchart['N7'] = "Is the pain worse when you bend over or lie down?"
    flowchart['A6'] = "See your doctor. You may have gastroesophageal reflux disease or indigestion."
    flowchart['N8'] = "Is the pain worse when you swallow?"
    flowchart['F1'] = "Difficulty Swallowing Flowchart" # change to difficulty swallowing flowchart
    flowchart['N9'] = "Is the pain on one side only?"
    flowchart['N10'] = "Have you recently had chest surgery or a chest injury, or have you been coughing severely?"
    flowchart['A7'] = "See your doctor. You may have a strained muscle or a broken rib."
    flowchart['N11'] = "Is the pain unaffected by breathing but accompanied by a burning feeling on the skin?"
    flowchart['A8'] = "See your doctor. You may have shingles."
    flowchart['A9'] = "See your doctor if you are unable to make a decision from self-triage."

    
    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N4", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A1", "Yes"),
        ("N3", "A2", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N7", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "A5", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "F1", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "N10", "Yes"),
        ("N10", "A7", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A8", "Yes"),
        ("N11", "A9", "No"),
        ("N9", "A9", "No")
    ]

    # Create a directed graph
    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    # Add edges to the graph
    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Difficulty_Breathing_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did your breathing difficulty begin within the past few days?"
    flowchart['N2'] = "Do you have chest pain?"
    flowchart['N3'] = "Is the pain crushing, or does it radiate from the breastbone or upper abdomen to your jaw, neck, or arms?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could be having a heart attact."
    flowchart['N4'] = "Is the pain worse when you inhale?"
    flowchart['A2'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have a blood clot in a lung, a collapsed lung, or pleurisy."
    flowchart['A3'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. If the pain persists after you rest for 5 minutes, you could be having a heart attack. However, you could also be having an attack of angina, a symptom of heart disease."
    flowchart['N5'] = "Is your temperature 100°F or above, or are you coughing up greenish yellow or rust-colored phlegm?"
    flowchart['A4'] = "See a doctor immediately. You could have pneumonia or acute bronchitis."
    flowchart['N6'] = "Have you been wheezing?"
    flowchart['F1'] = "Wheezing Flowchart" # change to wheezing flowchart
    flowchart['N7'] = "Do you feel light-headed, or are your hands and feet numb and tingling?"
    flowchart['A5'] = "See your doctor. Your problem is probably hyperventilation resulting from anxiety."
    flowchart['N8'] = "Has your breathing become increasingly difficult in the past weeks or months?"
    flowchart['N9'] = "Do you cough up thick gray or greenish yellow mucus most days?"
    flowchart['N10'] = "Do you work in a dusty atmosphere (such as a mine or quarry)?"
    flowchart['A6'] = "You could have a lung disease caused by long-term exposure to dust."
    flowchart['A7'] = "See your doctor. You probably have a lung disease such as chronic bronchitis, emphysema, or pneumonia."
    flowchart['N11'] = "Do your ankles look unusually puffy, or does pressing on them with your fingers leave an indentation?"
    flowchart['A8'] = "See your doctor. You may have congestive heart failure."
    flowchart['N12'] = "Do you have new pets or new carpeting, has your carpet or upholstery been cleaned recently, or have you been inhaling the fumes of any cleaning agents?"
    flowchart['A9'] = "See your doctor. You may be having an allergic reaction to the new pet or reacting to toxic fumes."
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage."

    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "N3", "Yes"),
        ("N3", "A1", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "A3", "No"),
        ("N2", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "F1", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N8", "No"),
        ("N1", "N8", "No"),
        ("N8", "N9", "Yes"),
        ("N9", "N10", "Yes"),
        ("N10", "A6", "Yes"),
        ("N10", "A7", "No"),
        ("N9", "N11", "No"),
        ("N11", "A8", "Yes"),
        ("N11", "N12", "No"),
        ("N12", "A9", "Yes"),
        ("N12", "A10", "No"),
        ("N8", "A10", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())


    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Pelvic_Pain_In_Women_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have vaginal bleeding between periods?"
    flowchart['F1'] = "Irregular Vaginal Bleeding Flowchart" # change to irregular vaginal bleeding flowchart
    flowchart['N2'] = "Do you have a vaginal discharge between periods that is unusually heavy or that has an unpleasant odor, or is your temperature 100°F or higher?"
    flowchart['A1'] = "See a doctor immediately. You may have an infection of the uterus, fallopian tubes, ovaries, or surrounding tissues."
    flowchart['N3'] = "Are you urinating more often than usual, or is urination painful?"
    flowchart['A2'] = "See your doctor. Your bladder may have become inflamed as a result of infection."
    flowchart['N4'] = "Did the pain start just before or during a period?"
    flowchart['F2'] = "Painful Periods Flowchart" # change to painful periods flowchart
    flowchart['N5'] = "Are you constipated, or have you been passing more gas than usual?"
    flowchart['A3'] = "See your doctor if the pain persists for more than 3 hours. Your intestines may have been affected by a recent change in your diet, or you may have an intestinal disorder such as irritable bowel syndrome."
    flowchart['A4'] = "See your doctor if you are unable to make a decision from self-triage."

   
    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "F2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "A4", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G



def Abdominal_Pain_Flowchart():
    flowchart = {}
    
    flowchart['N1'] = "Have you had similar episodes of pain that come and go?"
    flowchart['N2'] = "Is the pain severe?"
    flowchart['F1'] = "Recurring Abdominal Pain Flowchart" # change to recurring abdominal pain flowchart
    flowchart['N3'] = "Do you have one or more of the following symptoms: vomiting; swollen or tender abdomen; temperature over 100°F?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have a life-threatening condition such as an intestinal obstruction or appendictis."
    flowchart['N4'] = "Do you have diarrhea?"
    flowchart['A2'] = "See your doctor. You may have food poisoning, gastroenteritis, or inflammatory bowel disease."
    flowchart['N5'] = "Did the pain begin in the small of your back and move to the groin?"
    flowchart['N6'] = "Is your temperature 100°F or higher?"
    flowchart['A3'] = "See your doctor. You may have a kidney infection."
    flowchart['A4'] = "See your doctor. You may have a kidney disorder such as kidney stones."
    flowchart['N7'] = "Is the pain in your lower abdomen?"
    flowchart['N8'] = "Are you a woman of childbearing age?"
    flowchart['F2'] = "Pelvic Pain In Women Flowchart" # change to pelvic pain in women flowchart
    flowchart['N9'] = "Have you been constipated, or have you passed more gas than usual within the past 24 hours?"
    flowchart['A5'] = "See your doctor if the pain persists for more than 3 hours. Your intestines are probably reacting to a change in your diet."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."
    flowchart['N10'] = "Does the pain spread around the edge of your rib cage on your right side?"
    flowchart['A7'] = "See your doctor. You may have a gallbladder disorder such as gallstones or cholecystitis."
    flowchart['N11'] = "Do you have burning pain on one side only, and does your skin feel tender in the area of the pain?"
    flowchart['A8'] = "See your doctor. You may have shingles."
    flowchart['N12'] = "Did you drink a lot of alcohol or eat rich or spicy food before the pain began?"
    flowchart['A9'] = "See your doctor if the pain persists for more than 24 hours. Some foods can upset the stomach, and alcohol can cause inflammation of the stomach lining."
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage."

    edges_with_conditions = [("N1", "N2", "No"),
                            ("N1", "F1", "Yes"),
                            ("N2", "N3", "Yes"),
                            ("N3", "A1", "Yes"),
                            ("N3", "N4", "No"),
                            ("N2", "N4", "No"),
                            ("N4", "A2", "Yes"),
                            ("N4", "N5", "No"),
                            ("N5", "N6", "Yes"),
                            ("N6", "A3", "Yes"),
                            ("N6", "A4", "No"),
                            ("N5", "N7", "No"),
                            ("N7", "N8", "Yes"),
                            ("N8", "F2", "Yes"),
                            ("N8", "N9", "No"),
                            ("N9", "A5", "Yes"),
                            ("N9", "A6", "No"),
                            ("N7", "N10", "No"),
                            ("N10", "A7", "Yes"),
                            ("N10", "N11", "No"),
                            ("N11", "A8", "Yes"),
                            ("N11", "N12", "No"),
                            ("N12", "A9", "Yes"),
                            ("N12", "A10", "No")]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    # Add edges to the graph
    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G



def Difficulty_Sleeping_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you often have difficulty falling asleep at night?"
    flowchart['N2'] = "Have you been feeling tense during the day?"
    flowchart['A1'] = "You may be experiencing too much stress."
    flowchart['N3'] = "Do you wake up during the night or very early in the morning and find it difficult to fall asleep again?"
    flowchart['N4'] = "When you wake up, do you often brood about your problems or feel worthless?"
    flowchart['A2'] = "See your doctor. You may be anxious or depressed."
    flowchart['N5'] = "Do you often wake up during the night feeling short of breath?"
    flowchart['A3'] = "See a doctor immediately. Some lung disorders or heart disorders such as congestive heart failure can make you short of breath when you lie down."
    flowchart['N6'] = "Are you over 60?"
    flowchart['A4'] = "Some people find it harder to sleep as they get older."
    flowchart['N7'] = "Are you pregnant?"
    flowchart['A5'] = "Difficulty sleeping is common during pregnancy, especially in the weeks before delivery."
    flowchart['N8'] = "Have you had more coffee, tea, cola, or other caffeine-containing beverages than usual?"
    flowchart['A6'] = "Caffeine is a stimulant that can cause sleeplessness. Avoid or reduce your intake of caffeine, especially in the late afternoon and evening."
    flowchart['N9'] = "Did you eat a lot late in the day, or drink a lot of alcohol?"
    flowchart['A7'] = "Try eating a lighter meal earlier in the evening or reduce your alcohol intake to a moderate level."
    flowchart['N10'] = "Have you recently stopped taking or reduced the dose of a tranquilizer or other sleep medication you have been taking?"
    flowchart['A8'] = "Talk to your doctor. If you have been using tranquilizers or sleep medication, suddenly stopping or reducing the dose can interfere with sleep and cause other problems. Your doctor can help you gradually and safely reduce the dose."
    flowchart['N11'] = "Do you get little or no exercise on most days?"
    flowchart['A9'] = "You may not be tired enough to fall asleep easily. Try exercising during the day, but not right before bedtime."
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage."
    

    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "N4", "Yes"),
        ("N3", "N5", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A6", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A7", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A8", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A9", "Yes"),
        ("N11", "A10", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Overweight_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you been overweight most of your life?"
    flowchart['N2'] = "Are both of your parents overweight?"
    flowchart['A1'] = "A tendency to be overweight runs in some families, usually as a result of learned eating habits. Talk to your doctor about losing weight."
    flowchart['N3'] = "Did you gain weight after you quit smoking?"
    flowchart['A2'] = "You are probably overweight because you consume more calories than your body burns."
    flowchart['A3'] = "Weight gain after quitting smoking averages about 5 to 10 pounds and usually results from a combination of changes in metabolism and overeating to compensate for not smoking."
    flowchart['N4'] = "Are you a woman?"
    flowchart['N5'] = "Did you become overweight after pregnancy?"
    flowchart['A4'] = "Many women gain too much weight during pregnancy and have difficulty losing it afterward."
    flowchart['N6'] = "Did you gain weight when you were feeling depressed, or have you been taking medication for depression?"
    flowchart['A5'] = "See your doctor. Many people overeat when they are depressed, and some antidepressants can cause weight gain."
    flowchart['N7'] = "Did you gain weight after changing from a physically strenuous job to a job in which you are less active?"
    flowchart['A6'] = "You probably burned more calories in your previous job than you do now. Make an effort to eat less and exercise more."
    flowchart['N8'] = "Have you had any of the following symptoms since you began to gain weight: frequently feeling cold; thinning or brittle hair; dry skin?"
    flowchart['A7'] = "See your doctor. You may have an underactive thyroid gland."
    flowchart['N9'] = "Have you been taking corticosteroid drugs for an inflammatory condition such as rheumatoid arthritis?"
    flowchart['A8'] = "Talk to your doctor. Oral corticosteroid medications can cause weight gain."
    flowchart['N10'] = "Are you over 40?"
    flowchart['A9'] = "In many cases, weight gain after age 40 results from getting less exercise. Try to stay active."
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage. Your excess weight probably results from eating too much and exercising too little. Ask your doctor to recommend a diet and exercise program that is appropriate for you."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "A2", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N6", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A8", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A9", "Yes"),
        ("N10", "A10", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def General_Skin_Problems_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does the skin problem mainly affect the skin on your face?"
    flowchart['F1'] = "Facial Skin Problems Flowchart" # change to facial skin problems flowchart
    flowchart['N2'] = "Do you have a red rash?"
    flowchart['N3'] = "Is your temperature 100°F or higher?"
    flowchart['F2'] = "Rash With Fever Flowchart" # change to facial skin problems flowchart
    flowchart['N4'] = "Does the rash itch?"
    flowchart['F3'] = "Itchy Spots And Rashes Flowchart" # change to itchy spots and rashes flowchart
    flowchart['N5'] = "Does the problem affect only the skin on your feet?"
    flowchart['F4'] = "Foot Problems Flowchart" # change to foot problems flowchart
    flowchart['N6'] = "Do you have one or more raised spots or lumps on your skin?"
    flowchart['F5'] = "Raised Spots And Lumps Flowchart" # change to raised spots and lumps flowchart
    flowchart['N7'] = "Does your skin itch but look normal?"
    flowchart['F6'] = "Itching Without A Rash Flowchart" # change to itching without a rash flowchart
    flowchart['N8'] = "Are you currently taking any medication?"
    flowchart['A1'] = "See your doctor. Some drugs can cause rashes in susceptible people. Your doctor may need to adjust the dosage of your medication or prescribe a different drug."
    flowchart['N9'] = "Are you over age 12?"
    flowchart['N10'] = "Do you have a new mole, or has an existing mole changed in appearance?"
    flowchart['A2'] = "See a doctor immediately. You could have skin cancer."
    flowchart['N11'] = "Do some areas of your skin look much paler or darker than usual?"
    flowchart['A3'] = "See your doctor. You could have a skin pigment disorder."
    flowchart['N12'] = "Do you have one or more red patches covered with white or silvery scales?"
    flowchart['A4'] = "See your doctor. You may have psoriasis."
    flowchart['N13'] = "Do you have a blistering rash on one side of your body in an area that was painful over the past 2 to 4 days?"
    flowchart['A5'] = "See your doctor. You could have shingles."
    flowchart['N14'] = "Do you have several oval, red, flaky patches on your chest, back, or abdomen?"
    flowchart['A6'] = "See your doctor. You may have a rash called pityriasis rosea."
    flowchart['A7'] = "See your doctor if you are unable to make a decision from self-triage."
    



    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "N5", "No"),
        ("N3", "F2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "F3", "Yes"),
        ("N4", "N8", "No"), 
        ("N5", "F4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "F5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "F6", "Yes"),
        ("N7", "N9", "No"),
        ("N8", "N12", "No"),  
        ("N8", "A1", "Yes"), 
        ("N9", "N10", "Yes"), 
        ("N9", "N11", "No"),
        ("N10", "A2", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A3", "Yes"),
        ("N11", "N12", "No"),
        ("N12", "A4", "Yes"),
        ("N12", "N13", "No"),
        ("N13", "A5", "Yes"),
        ("N13", "N14", "No"),
        ("N14", "A6", "Yes"), 
        ("N14", "A7", "No")

    ]



    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


