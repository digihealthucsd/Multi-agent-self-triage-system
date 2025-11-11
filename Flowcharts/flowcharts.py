import networkx as nx

def Limping_In_Children_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does your child seem healthy otherwise?"
    flowchart['N2'] = "Could your child have strained or injured a leg, foot, or hip?"
    flowchart['N3'] = "Can your child walk barefoot without limping?" 
    flowchart['A1'] = "Your child's shoes or socks may be uncomfortable or may not fit well, or a nail or other sharp object may be poking through the sole of the shoe."
    flowchart['N4'] = "Does your child have a small patch of thickened skin on the sole of his or her foot?"
    flowchart['A2'] = "Your child may have a plantar wart, especially if the skin patch causes discomfort when he or she walks on the foot."
    flowchart['N5'] = "Is the injury painful, or is the leg or foot swollen or at an odd angle?"
    flowchart['A3'] = "Take your child to the doctor immediately. Your child may have a severe sprain or fracture."
    flowchart['A4'] = "Take your child to the doctor if your child continues to limp for more than 48 hours after the suspected injury. He or she may have a minor sprain or a bruised leg, foot, or hip." 
    flowchart['N6'] = "Does your child have a sore spot on the sole of his or her foot that hurts when touched?"
    flowchart['A5'] = "Your child may have a splinter."
    flowchart['N7'] = "Has your child just learned to walk, and does he or she seem to be unaware of the limp?"
    flowchart['A6'] = "Take your child to the doctor. Your child may have a disorder of the nervous system or a problem with his or her bones or joints."
    flowchart['N8'] = "Does your child have pain, swelling, or redness around the knees, ankles, or hips, and do those joints feel warm?"
    flowchart['A7'] = "Take your child to the doctor. Your child may have a serious disorder such as rheumatic fever or juvenile rheumatoid arthritis."
    flowchart['N9'] = "Does your child have a fever and a painful, tender area over any bone in the leg or foot?"
    flowchart['A8'] = "Take your child to the doctor immediately. Your child may have a bone infection such as osteomyelitis."
    flowchart['A9'] = "Take your child to the doctor if you are unable to make a decision from self-triage and your child's limp does not improve significantly after resting for 48 hours."
     
    edges_with_conditions = [
        ("N1", "N8", "No"),
        ("N1", "N2", "Yes"),
        ("N2", "N5", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A1", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "N6", "No"),  
        ("N5", "A3", "Yes"),
        ("N5", "A4", "No"),  
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A8", "Yes"),
        ("N9", "A9", "No")]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



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
    G.add_nodes_from(flowchart.keys())

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
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G





def Facial_Skin_Problems_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have an itchy, red, flaky rash?"
    flowchart['A1'] = "See your doctor. You may have contact dermatitis or seborrheic dermatitis."
    flowchart['N2'] = "Do you have one or more of the following symptoms: blackheads; raised spots on the skin with white or yellow centers; painful red lumps under the skin?"
    flowchart['A2'] = "See your doctor. You probably have acne."
    flowchart['N3'] = "Does your face become flushed when you're under stress or after you drink alcohol or eat spicy foods?"
    flowchart['A3'] = "See your doctor. You may have rosacea."
    flowchart['N4'] = "Do you have sore areas around your mouth that are red and rough or blistered?"
    flowchart['A4'] = "Talk to your doctor. You probably have cold sores."
    flowchart['N5'] = "Do you have a blistering rash on one side of your face in an area that was painful over the past 2 to 4 days?"
    flowchart['A5'] = "See your doctor. You may have shingles."
    flowchart['N6'] = "Do you have blisters that burst and form a crust that looks like brown sugar?" 
    flowchart['A6'] = "See your doctor. You may have impetigo."
    flowchart['N7'] = "Are you over 35?"
    flowchart['N8'] = "Do you have rough red patches on your forehead or cheeks?"
    flowchart['A7'] = "See your doctor. You may have actinic keratoses, which can form from repeated exposure to sunlight."
    flowchart['N9'] = "Do you have a dark lump or patch on your face, or has a mole changed in any way?"
    flowchart['A8'] = "See a doctor immediately. If you are past puberty, there is a slight possibility that you have skin cancer. However, you probably have a harmless skin pigment disorder."
    flowchart['N10'] = "Have you had an open sore on your face or lip for more than 3 weeks?"
    flowchart['A9'] = "See a doctor immediately. You may have a form of skin cancer."
    flowchart['N11'] = "Do you have a firm, slow-growing lump on your face?"
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage."



    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A5", "Yes"),
        ("N5", "N6", "No"), 
        ("N6", "A6", "Yes"),
        ("N6", "N7", "No"), 
        ("N7", "N8", "Yes"),
        ("N7", "N9", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "N9", "No"), 
        ("N9", "A8", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A9", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A9", "Yes"),
        ("N11", "A10", "No")

    ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Vomiting_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you been having episodes of vomiting for a week or longer?"
    flowchart['F1'] = "Recurring Vomiting Flowchart" # change to recurring vomiting flowchart
    flowchart['N2'] = "Do you have severe abdominal pain that has lasted at least 1 hour and has not been relieved by vomiting?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You probably have a serious abdominal condition such as peritonitis or an intestinal obstruction."
    flowchart['N3'] = "Have you vomited blood, or black or dark brown matter that looks like coffee grounds (partially digested blood)?"
    flowchart['A2'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You probably have internal bleeding, possibly from a peptic ulcer or another condition in the digestive tract."
    flowchart['N4'] = "Do you have diarrhea?"
    flowchart['A3'] = "See your doctor. You may have an infection of the digestive tract."
    flowchart['N5'] = "Did you eat a lot of rich food in the past few hours or drink a lot of alcohol?"
    flowchart['A4'] = "You probably have indigestion."
    flowchart['N6'] = "Have you eaten food that may have spoiled?"
    flowchart['A5'] = "See your doctor. You may have food poisoning, especially if someone who ate the same food has the same symptoms."
    flowchart['N7'] = "Are you currently taking any medication?"
    flowchart['A6'] = "Talk to your doctor. Some drugs can cause vomiting."
    flowchart['N8'] = "Do you have severe pain in or around one eye, and is your vision blurred?"
    flowchart['A7'] = "See an eye doctor immediately. You could have acute glaucoma."
    flowchart['N9'] = "Do you have a headache?"
    flowchart['N10'] = "Before vomiting, did you feel so dizzy that the room seemed to be spinning?"
    flowchart['A8'] = "See your doctor. You may have a disorder of the inner ear such as labyrinthitis or meniere's disease."
    flowchart['N11'] = "Do the whites of your eyes and your skin look yellow?"
    flowchart['A9'] = "See your doctor. You may have a disorder of the liver or gallbladder."
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage and your vomiting persists for more than 24 hours."
    flowchart['N12'] = "Did you injure your head within the past 24 hours?"
    flowchart['A11'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have a brain injury."
    flowchart['N13'] = "Do you have one or more of the following symptoms: pain when you bend your head forward; sensitivity of eyes to bright light; drowsiness or confusion; fever?"
    flowchart['A12'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have meningitis or a subarachnoid hemorrhage."
    flowchart['F2'] = "Headache Flowchart" # change to headache flowchart

    edges_with_conditions = [("N1", "F1", "Yes"),
                             ("N1", "N2", "No"),
                             ("N2", "A1", "Yes"),
                             ("N2", "N3", "No"),
                             ("N3", "A2", "Yes"),
                             ("N3", "N4", "No"),
                             ("N4", "A3", "Yes"),
                             ("N4", "N5", "No"),
                             ("N5", "A4", "Yes"), 
                             ("N5", "N6", "No"),
                             ("N6", "A5", "Yes"),
                             ("N6", "N7", "No"),
                             ("N7", "A6", "Yes"),
                             ("N7", "N8", "No"),
                             ("N8", "A7", "Yes"),
                             ("N8", "N9", "No"),
                             ("N9", "N12", "Yes"),
                             ("N9", "N10", "No"),
                             ("N10", "A8", "Yes"),
                             ("N10", "N11", "No"),
                             ("N11", "A9", "Yes"),
                             ("N11", "A10", "No"),
                             ("N12", "A11", "Yes"),
                             ("N12", "N13", "No"),
                             ("N13", "A12", "Yes"),
                             ("N13", "F2", "No")
                    
                             ] 


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Unusual_Behavior_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does the person seem confused about time, places, or events?"
    flowchart['F1'] = "Confusion Flowchart" # change to confusion flowchart
    flowchart['N2'] = "Does the person seem unusually withdrawn?"
    flowchart['A1'] = "Talk to the person's doctor. Withdrawal can be a sign of depression or schizophrenia."
    flowchart['N3'] = "Does the person behave normally most of the time and behave strangely only for brief, intermittent periods?"
    flowchart['N4'] = "Could the person be abusing alcohol or other drugs?"
    flowchart['A2'] = "Talk to the person's doctor. Abusing alcohol or other drugs can cause unpredictable mood swings."
    flowchart['N5'] = "Does the person seem preoccupied with a single idea or activity?"
    flowchart['A3'] = "Talk to the person's doctor. Such behavior may be a sign of depression or obsessive-compulsive disorder."
    flowchart['N6'] = "Does the person seem unusually restless and unable to relax or concentrate on his or her usual activities?"
    flowchart['A4'] = "Talk to the person's doctor. Such behavior may be a sign of anxiety, depression, or bipolar disorder."
    flowchart['A5'] = "Take the person to a doctor immediately if you are unable to make a decision from self-triage. There is a chance that a brain tumor could be causing the person's unusual behavior."


    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "N4", "Yes"),
        ("N3", "N5", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "A5", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Itching_Without_A_Rash_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is the itching around the anus only?"
    flowchart['N2'] = "Is the itching more severe at night?"
    flowchart['A1'] = "See your doctor if you have young children or work with young children. You could have pinworms."
    flowchart['N3'] = "Have you had any bleeding from the anus, or are bowel movements painful?"
    flowchart['A2'] = "See your doctor. You could have hemorrhoids or an anal fissure, but there is also a slight possibility of colon cancer."
    flowchart['N4'] = "Have you recently had severe diarrhea?"
    flowchart['A3'] = "See your doctor if the itching continues. Itching around the anus is common after severe diarrhea and usually stops in a day or two."
    flowchart['N5'] = "Are you a woman, and is the itching confined to the genital area?"
    flowchart['F1'] = "Vaginal Irritation Flowchart"  # change to vaginal irritation flowchart
    flowchart['N6'] = "Do the whites of your eyes look yellow?"
    flowchart['A4'] = "See a doctor immediately. You may have jaundice caused by a liver disorder."
    flowchart['N7'] = "Is your skin very dry?"
    flowchart['N8'] = "Is the itching relieved by applying a soothing cream to the itchy areas?"
    flowchart['A5'] = "Dry skin often itches."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."



    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N5", "No"), 
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),  
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "F1", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "N8", "Yes"),
        ("N7", "A6", "No"),
        ("N8", "A5", "Yes"),
        ("N8", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Nightmares_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you been feeling unusually tense or worried?"
    flowchart['A1'] = "See your doctor if the nightmares persist. Your nightmares are probably caused by anxiety."
    flowchart['N2'] = "Do you have nightmares only occasionally?"
    flowchart['A2'] = "Most people have occasional nightmares."
    flowchart['N3'] = "Did the nightmares begin after a traumatic event (such as a traffic accident or a death in your family)?"
    flowchart['A3'] = "See your doctor if the nightmares persist. Nightmares often follow such experiences and usually stop within a few weeks."
    flowchart['N4'] = "Do you have a physical illness such as a viral infection?"
    flowchart['A4'] = "Vivid dreams are common during illness, especially when a person has a fever."
    flowchart['N5'] = "Have you recently stopped taking sleep medication?"
    flowchart['A5'] = "See your doctor about stopping your medication gradually and safely. Stopping sleep medication too quickly is a common cause of nightmares. Your dreams should return to normal in a few days."
    flowchart['N6'] = "Have you recently been drinking more alcohol than usual, or have you recently stopped drinking?"
    flowchart['A6'] = "See your doctor. Drinking large quantities of alcohol or suddenly stopping drinking after drinking for a long time can disturb sleep patterns and cause nightmares."
    flowchart['N7'] = "Are you currently taking any medication?"
    flowchart['A7'] = "Talk to your doctor. Some drugs can cause nightmares."
    flowchart['A8'] = "See your doctor if you are unable to make a decision from self-triage and your nightmares persist."



    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),  
        ("N4", "N5", "No"), 
        ("N5", "A5", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A6", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A7", "Yes"),
        ("N7", "A8", "No")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Confusion_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did you become confused suddenly during the past few hours?"
    flowchart['N2'] = "Did you injure your head recently (within the past few days)?"
    flowchart['A1'] = "See a doctor immediately. Some degree of confusion after an injury is not unusual, but anyone with a head injury must be examined by a doctor to determine the extent of the injury and check for any bleeding inside the skull."
    flowchart['N3'] = "Is your temperature 104°F or higher?"
    flowchart['A2'] = "See a doctor immediately. A high fever often causes some degree of confusion. Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department if your confusion is severe. You could have meningitis or encephalitis."
    flowchart['N4'] = "Do you have a heart or lung disease or diabetes?"
    flowchart['A3'] = "See a doctor immediately. Confusion associated with any of these disorders can indicate a serious health problem."
    flowchart['N5'] = "Have you had any of the following symptoms since the confusion started: dizziness; weakness in your arms or legs; numbness or tingling in any part of your body; blurred vision; difficulty speaking; abnormal movements of the body or face?"
    flowchart['A4'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have had a stroke or a transient ischemic attack. Or you may have epilepsy."
    flowchart['N6'] = "Were you drinking alcohol or taking other drugs before you became confused?"
    flowchart['A5'] = "Talk to your doctor. Alcohol and other drugs can sometimes cause confusion."
    flowchart['N7'] = "Are you over 65?"
    flowchart['F1'] = "Confusion In Older People Flowchart" # change to confusion in older people flowchart
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."
    


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N6", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),  
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "F1", "Yes"),
        ("N7", "A6", "No")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Recurring_Vomiting_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Are you a woman of childbearing age, and do you vomit at about the same time on most days?"
    flowchart['A1'] = "See your doctor. You may be pregnant; this type of vomiting is common early in pregnancy."
    flowchart['N2'] = "Do you usually vomit within a few hours after drinking alcohol?"
    flowchart['A2'] = "See your doctor. Alcohol can cause inflammation of the stomach lining, especially if you drink a lot of alcohol."
    flowchart['N3'] = "Do you have burning pain in your chest or upper abdomen when you bend over or lie down?"
    flowchart['A3'] = "See your doctor. You may have gastroesophageal reflux disease."
    flowchart['N4'] = "Do you have abdominal pain or tenderness an hour or two after meals?"
    flowchart['N5'] = "Is the pain or tenderness in the center of your upper abdomen, and is the pain relieved by vomiting?"
    flowchart['A4'] = "See your doctor. You may have a peptic ulcer."
    flowchart['N6'] = "Have you lost your appetite?"
    flowchart['N7'] = "Do the whites of your eyes and your skin look yellow?"
    flowchart['A5'] = "See your doctor. You may have a disorder of the liver or gallbladder."
    
    flowchart['N8'] = "Is the pain mainly in the upper right part of your abdomen?"
    flowchart['N9'] = "Is your temperature 100°F or higher?"
    flowchart['A6'] = "See your doctor. You may have an inflamed gallbladder."
    flowchart['F1'] = "Abdominal Pain Flowchart" # change to abdominal pain flowchart
    flowchart['A7'] = "See your doctor. You could have gallstones, indigestion, or irritable bowel syndrome."
    flowchart['N10'] = "Do you have abdominal pain that is sometimes relieved by vomiting?"
    flowchart['A8'] = "See a doctor immediately. You could have a peptic ulcer or cancer of the stomach."
    flowchart['N11'] = "Are you currently taking any medication?"
    flowchart['A9'] = "Talk to your doctor. Some drugs can cause vomiting."
    flowchart['N12'] = "Do you have frequent headaches?"
    flowchart['N13'] = "Do you vomit suddenly (without feeling nauseous first), and do your headaches occur mainly in the morning?"
    flowchart['A10'] = "See a doctor immediately. You could have a subdural hemorrhage."
    flowchart['A11'] = "See your doctor if you are unable to make a decision from self-triage."
    


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N6", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N8", "No"), 
        ("N6", "N7", "Yes"),
        ("N6", "N11", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N10", "No"),
        ("N8", "F1", "No"), 
        ("N8", "N9", "Yes"), 
        ("N9", "A6", "Yes"),
        ("N9", "A7", "No"),
        ("N10", "A8", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A9", "Yes"),
        ("N11", "N12", "No"), 
        ("N12", "N13", "Yes"), 
        ("N12", "A11", "No"),
        ("N13", "A10", "Yes"),
        ("N13", "A11", "No")

    ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Runny_Nose_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have a clear, watery discharge from your nose?"
    flowchart['N2'] = "Is your temperature 100°F or higher?"
    flowchart['N3'] = "Do you have two or more of the following symptoms: headache; cough; aching joints or bones?"
    flowchart['A1'] = "Call your doctor. You probably have a viral infection such as influenza."
    flowchart['N4'] = "Do you have a sore throat, or have you had a sore throat within the past 4 days?"
    flowchart['A2'] = "You probably have a cold."
    flowchart['A3'] = "See your doctor. You may have an allergy."
    flowchart['N5'] = "Do your eyes feel itchy, or have you been sneezing?"
    flowchart['A4'] = "Your runny nose may result from irritation, such as from smoke or fumes or from eating spicy foods."
    flowchart['N6'] = "Do you have a thick, cloudy discharge from your nose?"
    flowchart['N7'] = "Does your face feel painful or tender just above or below your eyes?"
    flowchart['A5'] = "See your doctor. You probably have a viral infection of the sinuses."
    flowchart['A6'] = "You probably have a cold."
    flowchart['A7'] = "See your doctor if you are unable to make a decision from self-triage and your symptoms persist for more than 10 days."



    edges_with_conditions = [("N1", "N2", "Yes"),
                                ("N1", "N6", "No"),
                                ("N2", "N3", "Yes"),
                                ("N2", "N5", "No"),
                                ("N3", "A1", "Yes"),
                                ("N3", "A2", "No"),
                                ("N4", "A2", "Yes"),
                                ("N4", "A3", "No"),
                                ("N5", "N4", "Yes"),
                                ("N5", "A4", "No"),
                                ("N6", "N7", "Yes"),
                                ("N6", "A7", "No"),
                                ("N7", "A5", "Yes"),
                                ("N7", "A6", "No")
                                ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Painful_Arm_Or_Hand_Flowchart():
    flowchart = {}
    edges_with_conditions = []

    flowchart['N1'] = "Did the pain immediately follow an injury?"
    flowchart['A1'] = "See a doctor immediately. You may have broken a bone or dislocated a joint (especially if the area looks misshapen) or severely strained or torn a muscle or tendon."
    flowchart['N2'] = "Is the pain severe?"
    flowchart['A2'] = "See your doctor (to rule out a fracture). You may have pulled a muscle, ligament, or tendon."
    flowchart['N3'] = "Does the pain extend down the upper arm toward the wrist?"
    flowchart['N4'] = "Did the pain begin during exercise and disappear within a few minutes of stopping?"
    flowchart['A3'] = "See a doctor immediately, especially if you also have chest pain. Your pain could be angina."
    flowchart['N5'] = "Does the pain get worse with use and better with rest?"
    flowchart['N6'] = "Do the joints nearest your fingernails look swollen?"
    flowchart['A4'] = "See your doctor. You may have osteoarthritis."
    flowchart['A5'] = "See your doctor. You may have osteoarthritis or rheumatoid arthritis."
    flowchart['N7'] = "Does a warm bath or shower relieve the pain somewhat?"
    flowchart['N8'] = "Do you have stiffness in the morning that lasts longer than an hour?"
    flowchart['N9'] = "Are the joints near your knuckles swollen?"
    flowchart['A6'] = "See your doctor. You may have rheumatoid arthritis."
    flowchart['N10'] = "Do you have numbness or tingling in your hands and fingers only?"
    flowchart['N11'] = "Do you have numbness or tingling in your arm or hand?"
    flowchart['A7'] = "See your doctor. You may have carpal tunnel syndrome. Or you may have a nerve disorder related to diabetes."
    flowchart['A8'] = "See your doctor. You may have a disorder that affects the joints in the neck, especially if you have a stiff neck."
    flowchart['N12'] = "Is the pain in the elbow, wrist, or finger joints?"
    flowchart['N13'] = "Is the pain accompanied by redness and swelling?"
    flowchart['N14'] = "Is only one joint affected?"
    flowchart['A9'] = "See your doctor. You may have raynaud's disease."
    flowchart['N15'] = "Do your hands or fingers turn white, then blue, then red, especially in the cold?"
    flowchart['N16'] = "Is your temperature 100°F or higher, or have you recently begun to feel ill?"
    flowchart['A10'] = "See a doctor immediately. You may have a joint infection."
    flowchart['N17'] = "Do you have stiffness in the morning that lasts longer than an hour?"
    flowchart['N18'] = "Are the joints near your knuckles swollen?"
    flowchart['N19'] = "Does the pain occur only when you bend your arm or hand or use it in a certain way, or only during certain activities such as using a computer?"
    flowchart['A11'] = "See your doctor. You may have rheumatoid arthritis."
    flowchart['A12'] = "See your doctor. You may have bursitis or gout or pseudogout."
    flowchart['A13'] = "See your doctor. You may have inflammation of the tendons."
    flowchart['A14'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions.extend([
        ("N1", "N2", "Yes"), ("N1", "N3", "No"),
        ("N2", "A1", "Yes"), ("N2", "A2", "No"),
        ("N3", "N4", "Yes"), ("N3", "N5", "No"),
        ("N4", "A3", "Yes"), ("N4", "N5", "No"),
        ("N5", "N6", "Yes"), ("N5", "N7", "No"),
        ("N6", "A4", "Yes"), ("N6", "N7", "No"),
        ("N7", "A5", "Yes"), ("N7", "N8", "No"),
        ("N8", "N9", "Yes"), ("N8", "N10", "No"),
        ("N9", "A6", "Yes"), ("N9", "N10", "No"),
        ("N10", "A7", "Yes"), ("N10", "N11", "No"), 
        ("N11", "A8", "Yes"), ("N11", "N12", "No"),
        ("N12", "N13", "Yes"), ("N12", "A14", "No"),
        ("N13", "N14", "Yes"), ("N13", "N15", "No"),
        ("N14", "N16", "Yes"), ("N14", "N15", "No"),
        ("N15", "A9", "Yes"),  ("N15", "N17", "No"),  
        ("N16", "A10", "Yes"), ("N16", "A12", "No"),
        ("N17", "N18", "Yes"), ("N17", "N19", "No"),
        ("N18", "A11", "Yes"), ("N18", "N19", "No"),
        ("N19", "A13", "Yes"), ("N19", "A14", "No") 
    ])



    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

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
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Constipation_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you often have difficulty having a bowel movement?"
    flowchart['N2'] = "Do you often resist the urge to have a bowel movement because you are too busy?"
    flowchart['A1'] = "Putting off going to the bathroom can lead to a loss of normal muscle reflexes in the intestine and rectum. It can also result in a buildup and drying out of stool. Always respond to the urge to have a bowel movement."
    flowchart['N3'] = "Have you used laxatives regularly for a long time?"
    flowchart['A2'] = "Talk to your doctor. Overuse of laxatives can eventually make the intestines underactive. Stop taking the laxatives; add high-fiber foods such as beans, bran, fruits, and vegetables to your diet; and drink plenty of water."
    flowchart['A3'] = "Your constipation is probably the result of a lack of fiber and fluids in your diet. Increase the amount of fiber and fluids you consume. You might also want to try a natural stool softener; several brands are available over the counter."
    flowchart['N4'] = "Are bowel movements painful?"
    flowchart['A4'] = "See your doctor. Pain from an anal fissure, anal fistula, or hemorrhoids may be causing your problem."
    flowchart['N5'] = "Are you currently taking medication?"
    flowchart['A5'] = "Talk to your doctor. Some drugs can cause constipation."
    flowchart['N6'] = "Are you on a diet, or does your diet lack sufficient amounts of water and high-fiber foods such as fruit, vegetables, whole grains, and legumes?"
    flowchart['A6'] = "You may not be eating enough or you may not be getting enough water or fiber in your diet to stimulate bowel movements."
    flowchart['N7'] = "Are you pregnant?"
    flowchart['A7'] = "Constipation is common during pregnancy."
    flowchart['N8'] = "Do you have two or more of the following symptoms: frequently feeling cold; dry skin or hair; unexplained weight gain; unexplained fatigue?"
    flowchart['A8'] = "See your doctor. You may have an underactive thyroid gland."
    flowchart['N9'] = "Do you have lower abdominal pain?"

    flowchart['N10'] = "Have you had similar episodes of pain and constipation for many years?"
    flowchart['A9'] = "See your doctor. You probably have irritable bowel syndrome."
    flowchart['A10'] = "See a doctor immediately. You may have diverticular disease. Or you could have colon cancer."
    flowchart['A11'] = "See your doctor if you are unable to make a decision from self-triage and the constipation persists for more than 2 weeks or you do not have any bowel movements for 3 days or more."



    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N4", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "A3", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A5", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A6", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A7", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A8", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "N10", "Yes"),
        ("N9", "A11", "No"), 
        ("N10", "A9", "Yes"),
        ("N10", "A10", "No")
        ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())


    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G





def Fever_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have a cough?"
    flowchart['N2'] = "Are you short of breath even when resting, have you been coughing up rust-colored or grayish yellow mucus, or have you been wheezing?"
    flowchart['A1'] = "See a doctor immediately. You may have a lung infection such as pneumonia or bronchitis."
    flowchart['N3'] = "Do you have a headache, or do your bones and joints ache?"
    flowchart['A2'] = "See your doctor if your symptoms last longer than 2 or 3 days. You probably have a viral infection."
    flowchart['N4'] = "Do you have a headache?"
    flowchart['N5'] = "Do you have one or more of the following symptoms: pain when bending your head forward; nausea or vomiting; sensitivity of eyes to bright light; drowsiness or confusion?"
    flowchart['A3'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have meningitis, a potentially life-threatening infection of the brain."
    flowchart['N6'] = "Have you vomited or had diarrhea?"
    flowchart['A4'] = "See your doctor. You may have an infection of the digestive tract."
    flowchart['N7'] = "Do you have aching joints or bones?"
    flowchart['A5'] = "See your doctor if your symptoms last longer than 2 or 3 days. You probably have a viral infection such as influenza. Rest, and drink plenty of fluids."
    flowchart['N8'] = "Do you have a rash?"
    flowchart['F1'] = "Rash With Fever Flowchart" # change to rash with fever flowchart
    flowchart['N9'] = "Do you have a sore throat?"
    flowchart['A6'] = "See your doctor. You could have a throat infection."
    flowchart['N10'] = "Do you have pain in your back (on one or both sides just above the waist) and chills?"
    flowchart['A7'] = "See a doctor immediately. You could have a kidney infection, which can be serious."
    flowchart['N11'] = "Do you have pain when you urinate, or are you urinating more frequently than usual?"
    flowchart['A8'] = "See your doctor. You may have a urinary tract infection."
    flowchart['N12'] = "Have you spent most of the day in strong sunlight or in very hot conditions?"
    flowchart['A9'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have heat exhaustion or heatstroke."
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage, if your temperature has not returned to normal within 24 hours, or if it is very high or rises again."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N4", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N4", "N6", "No"),        
        ("N6", "A4", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "F1", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A6", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A7", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A8", "Yes"),
        ("N11", "N12", "No"),
        ("N12", "A9", "Yes"),
        ("N12", "A10", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Painful_Knee_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you injured your knee within the past 24 hours?"
    flowchart['N2'] = "Is the knee misshapen, or are you unable to move it?"
    flowchart['A1'] = "See a doctor immediately. You may have broken your leg or dislocated your knee."
    flowchart['N3'] = "Is the knee red, swollen, and hot?"
    flowchart['A2'] = "See your doctor. You may have bruised or sprained your knee. Or you may have torn the cartilage or ligament in your knee, especially if your knee seems to catch or give way."
    flowchart['N4'] = "Are both knees or other joints (such as the joints of the fingers) affected?"
    flowchart['N5'] = "Is your temperature 100°F or higher, or have you recently started to feel ill?"
    flowchart['A3'] = "See a doctor immediately. You may have rheumatoid arthritis but you could also have a joint infection."
    flowchart['A4'] = "See your doctor. You may have rheumatoid arthritis."
    flowchart['N6'] = "Is your temperature 100°F or higher, or have you recently started to feel ill?"
    flowchart['A5'] = "See a doctor immediately. You may have a joint infection. Or you may have a bone infection that is more common in children."
    flowchart['A6'] = "You may have bursitis or gout or pseudogout."
    flowchart['N7'] = "Does the knee seem to catch or give way?"
    flowchart['N8'] = "Is the knee painful most of the time?"
    flowchart['A7'] = "See your doctor. You may have osteoarthritis."
    flowchart['A8'] = "See your doctor. The cartilage in your knee may be damaged."
    flowchart['N9'] = "Has the knee been painful for some time?"
    flowchart['A9'] = "See your doctor. You may have osteoarthritis."
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "A2", "No"),
        ("N3", "N4", "Yes"),
        ("N3", "N7", "No"), 
        ("N4", "N5", "Yes"),
        ("N4", "N6", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "A4", "No"),
        ("N6", "A6", "No"),
        ("N6", "A5", "Yes"),
        ("N7", "N8", "Yes"),
        ("N7", "N9", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "A8", "No"),
        ("N9", "A9", "Yes"),
        ("N9", "A10", "No")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Impaired_Memory_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Are you unable to recall a specific period of time?"
    flowchart['N2'] = "Are you unable to recall the period of time immediately before or after a head injury?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. Your injury needs to be evaluated by a doctor to determine the severity and to check for any bleeding inside your skull."
    flowchart['N3'] = "Have you forgotten things that happened when you were drinking alcohol?"
    flowchart['A2'] = "See your doctor. Abusing alcohol can often result in blackouts, or memory loss."
    flowchart['N4'] = "Have you forgotten events surrounding any of the following: a severe illness with a fever, such as pneumonia; surgery; an epileptic seizure or diabetic coma?"
    flowchart['A3'] = "See your doctor to find out if you are recovering normally. Memory loss frequently occurs in such situations and is usually not a cause for concern."
    flowchart['N5'] = "Do you sometimes have difficulty remembering routine things, such as what you intend to buy when you are shopping?"
    flowchart['N6'] = "Are you under a lot of stress, or do you feel anxious or depressed?"
    flowchart['A4'] = "See your doctor if you are feeling depressed or anxious. However, stress may be affecting your ability to concentrate."
    flowchart['N7'] = "Do you recall things that happened long ago more easily than recent events?"
    flowchart['N8'] = "Do you have two or more of the following symptoms: decreased ability to deal with everyday activities such as cooking, driving, paying bills, and balancing a checkbook; personality changes; decline in personal appearance and cleanliness; difficulty following conversations or instructions?"
    flowchart['N9'] = "Has your memory gradually become less sharp over the past 10 years or longer?"
    flowchart['A5'] = "See your doctor. This combination of symptoms may indicate the onset of alzheimer's disease."
    flowchart['A6'] = "See your doctor. This type of memory loss can be caused by a physical disorder such as hypothyroidism, although it may be a natural part of aging. To help you remember, get into the habit of writing things down—for example, make shopping lists."
    flowchart['N10'] = "Is your memory loss complete— that is, you remember nothing about the past?"
    flowchart['A7'] = "See your doctor. Complete memory loss usually results from a severe emotional or mental disorder."
    flowchart['N11'] = "Are you currently taking any medication?"
    flowchart['A8'] = "Talk to your doctor. Some medications, especially sleep medications, can cause memory loss."
    flowchart['A9'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N5", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "N6", "Yes"),
        ("N5", "N10", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "N8", "Yes"),
        ("N7", "N9", "No"),
        ("N8", "A5", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A6", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A7", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A8", "Yes"),
        ("N11", "A9", "No")
    ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Difficulty_Swallowing_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have a sore throat?"
    flowchart['N2'] = "Could you have swallowed something (such as a fish bone)?"
    flowchart['A1'] = "See a doctor immediately. Something may be lodged in your throat."
    flowchart['F1'] = "Sore Throat Flowchart" # change to sore throat flowchart
    flowchart['N3'] = "Does food seem to stick high up in your chest after you swallow it?"
    flowchart['N4'] = "Do you sometimes experience pain in your chest, particularly when you squat, bend, or lie down?"
    flowchart['A2'] = "See your doctor. Your esophagus may be scarred as a result of acid reflux."
    flowchart['N5'] = "Are you having difficulty swallowing, do you regurgitate food you swallow, and have you lost a lot of weight in a short time (more than 10 pounds in 10 weeks)?"
    flowchart['A3'] = "See a doctor immediately. You may have a disorder of the esophagus, such as achalasia or a pharyngeal pouch, or you may have a scarred esophagus from chronic acid reflux. There is also a possibility that you have cancer of the esophagus, especially if you are over 40."
    flowchart['N6'] = "Do you swallow normally but feel a lump in your throat when you swallow or feel that the food will not go down?"
    flowchart['A4'] = "See your doctor. Your swallowing problem may be a symptom of anxiety. Or it may be a symptom of gastroesophageal reflux disease."
    flowchart['A5'] = "See your doctor if you are unable to make a decision from self-triage."
    
    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "A1", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "F1", "No"),
        ("N3", "N4", "Yes"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N3", "N6", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "A5", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Coughing_Up_Blood_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your temperature 102°F or higher?"
    flowchart['A1'] = "See a doctor immediately. You may have pneumonia or acute bronchitis, especially if you are coughing up mucus that is rusty brown or streaked with red."
    flowchart['N2'] = "Are you short of breath and unable to lie flat on your back, even though you have not been exercising?"
    flowchart['N3'] = "Are you coughing up mucus that is pink and frothy?"
    flowchart['A2'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have congestive heart failure."
    flowchart['A3'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have a blood clot in your lung."
    flowchart['N4'] = "Have you recently had surgery, been confined to bed, or sat for prolonged periods during a trip?"
    flowchart['N5'] = "Have you had a cold or the flu within the past month that has left you with a persistent cough?"
    flowchart['A4'] = "See your doctor. Coughing may have ruptured a small blood vessel in your airway."
    flowchart['N6'] = "Have you had a cough for many weeks or months?"
    flowchart['A5'] = "See a doctor immediately. You could have lung cancer or tuberculosis."
    flowchart['A6'] = "See a doctor immediately if you are unable to make a decision from self-triage."
    


    edges_with_conditions = [("N1", "A1", "Yes"),
                                        ("N1", "N2", "No"),
                                        ("N2", "N3", "Yes"),
                                        ("N2", "N4", "No"),
                                        ("N3", "A2", "Yes"),
                                        ("N3", "N4", "No"),
                                        ("N4", "A3", "Yes"),
                                        ("N4", "N5", "No"),
                                        ("N5", "A4", "Yes"),
                                        ("N5", "N6", "No"),
                                        ("N6", "A5", "Yes"),
                                        ("N6", "A6", "No")]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    # Add edges to the graph
    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Lack_Of_Bladder_Control_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does the problem occur in a child?"
    flowchart['A1'] = "Most children can control their bladder through the day and night by age 3½. However, some children have problems with bladder control until they are much older."
    flowchart['N2'] = "Do you have pain when you urinate?"
    flowchart['I1'] = "You may have a urinary tract infection."
    flowchart['F1'] = "Painful Urination Flowchart" # change to painful urination flowchart 
    flowchart['N3'] = "Are you a woman?"
    flowchart['N5'] = "Are you over age 60?"
    flowchart['N4'] = "Do you leak urine when you cough, sneeze, lift, or run?"
    flowchart['A2'] = "See your doctor. You probably have stress incontinence. However, you could have a bladder tumor."
    flowchart['N6'] = "Does the involuntary passing of small amounts of urine follow an intense urge to empty the bladder?"
    flowchart['N7'] = "Do you leak a small amount of urine after you have finished urinating?"
    flowchart['N8'] = "Are you over age 65?"
    flowchart['F2'] = "Lack Of Bladder Control In Older People Flowchart" # change to lack of bladder control flowchart
    flowchart['A3'] = "See your doctor. You may have an enlarged prostate gland. Or you may have a urethral stricture or a bladder tumor."
    flowchart['A4'] = "See your doctor. You probably have urge incontinence. However, you could have a bladder tumor."
    flowchart['A5'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "I1", "Yes"),
        ("I1", "F1", None),
        ("N2", "N3", "No"),
        ("N3", "N5", "No"),
        ("N3", "N4", "Yes"),
        ("N4", "N6", "No"),  
        ("N4", "A2", "Yes"),
        ("N5", "A5", "No"),
        ("N5", "N7", "Yes"), 
        ("N6", "A4", "Yes"),
        ("N6", "A5", "No"),
        ("N7", "A3", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "F2", "Yes"),
        ("N8", "A5", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Itchy_Spots_And_Rashes_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your temperature 100°F or higher?"
    flowchart['F1'] = "Rash With Fever Flowchart" # change to rash with fever flowchart
    flowchart['N2'] = "Do you have a red, flaky, or moist rash that fades into the surrounding skin?"
    flowchart['N3'] = "Do you have a smooth, raised, light-red rash with clearly defined edges?"
    flowchart['A1'] = "You may have hives."  
    flowchart['N4'] = "Is the rash on a part of your body that has been in contact with a new cosmetic or a new item of clothing or jewelry?"
    flowchart['N5'] = "Is it possible that you touched a plant to which your skin may be sensitive, such as poison ivy, poison oak, or poison sumac?"
    flowchart['N6'] = "Is the rash on only one part of your body such as your hands or the back of your legs, and have you been using shampoos, detergents, soap, bubble bath, or other substances that could irritate or dry your skin?"
    flowchart['A2'] = "See your doctor. You may have a type of dermatitis."
    flowchart['A4'] = "See your doctor. You may have contact dermatitis."
    flowchart['A5'] = "See your doctor. You may have irritant dermatitis."
    flowchart['N7'] = "Have you recently started taking any medication?"
    flowchart['N8'] = "Do you have one or more red, scaly patches that spread out in a ring?"
    flowchart['N9'] = "Do you have a widespread red rash that itches a lot, particularly at night?"
    flowchart['N10'] = "Do you have tiny gray lines or red, infected-looking spots between your fingers or on your wrists?"
    flowchart['N11'] = "Do you have one or more raised red spots on a small area?"
    flowchart['A6'] = "Talk to your doctor. Some drugs can cause an itchy rash."
    flowchart['A7'] = "See your doctor. You may have a fungal infection called ringworm."
    flowchart['A8'] = "See your doctor. You may have a parasitic infestation called scabies, especially if you have been in close physical contact with a person who has it."
    flowchart['A9'] = "See your doctor. You may have been bitten or stung by an insect."
    flowchart['A3'] = "See your doctor if you are unable to make a decision from self-triage."

    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N4", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A1", "Yes"),
        ("N3", "N7", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"), 
        ("N5", "N6", "No"), 
        ("N6", "A2", "No"),
        ("N6", "A5", "Yes"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "N10", "Yes"),
        ("N9", "N11", "No"),
        ("N10", "A8", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A3", "No"),
        ("N11", "A9", "Yes")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G





def Feeling_Generally_Ill_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your temperature 100°F or higher?"
    flowchart['F1'] = "Fever Flowchart" # change to fever flowchart
    flowchart['N2'] = "Do you suddenly feel unusually tired, and do you have any discomfort in your chest or arms when you move around?"
    flowchart['A1'] = "See a doctor immediately. Sudden onset of such symptoms may indicate that you have heart disease and are at risk of having a heart attack."
    flowchart['N3'] = "Do you feel nervous or anxious?"
    flowchart['I1'] = "You may have anxiety."
    flowchart['F2'] = "Anxiety Flowchart" # change to anxiety flowchart
    flowchart['N4'] = "Have you been feeling tired for some time?"
    flowchart['N5'] = "Have you been working hard without a break for several weeks?"
    flowchart['A2'] = "You may be feeling the effects of stress."
    flowchart['N6'] = "Have you recently recovered from a viral infection such as the flu or infectious mononucleosis?"
    flowchart['A3'] = "See your doctor if your symptoms last longer than 3 weeks. It can take a few weeks to recover from some viral infections. In the meantime, take it easy, get enough sleep, and get the proper nutrition."
    flowchart['N7'] = "Do you have one or more of the following symptoms: difficulty sleeping; inability to concentrate or make decisions; lack of interest in sex; recurring headaches; frequently feeling sad?"
    flowchart['A4'] = "See your doctor. You may have depression. Or you may have iron deficiency anemia, hypothyroidism, or chronic fatigue syndrome."
    flowchart['N8'] = "Are you overweight according to the body mass index?"
    flowchart['A5'] = "See your doctor. Being overweight puts a strain on your body. Losing weight may help you feel better."
    flowchart['N9'] = "Do you exercise regularly?"
    flowchart['A6'] = "Regular exercise keeps you fit both physically and mentally."
    flowchart['N10'] = "Are you taking any medication?"
    flowchart['A7'] = "Talk to your doctor. Some drugs can make you feel tired or sick."
    flowchart['N11'] = "Have you lost a lot of weight (10 or more pounds in 10 weeks or less) without trying?"
    flowchart['F3'] = "Unexplained Weight Loss Flowchart" # change to unexplained weight loss flowchart
    flowchart['A8'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "I1", "Yes"),
        ("I1", "F2", None),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N5", "A2", "Yes"),
        ("N5", "N6", "No"),
        ("N4", "N10", "No"), 
        ("N6", "A3", "Yes"),
        ("N6", "N7", "No"),  
        ("N7", "A4", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A5", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "N10", "Yes"), 
        ("N9", "A6", "No"),
        ("N10", "A7", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "F3", "Yes"),
        ("N11", "A8", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Toothache_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you feel pain only when eating or just after eating?"
    flowchart['N2'] = "Have you had one or more teeth filled within the past week?"
    flowchart['N3'] = "Does the tooth hurt only when you bite down?"
    flowchart['A1'] = "See your dentist. You may have a cavity caused by tooth decay, or you may have gingivitis (inflammation of the gums)."
    flowchart['A2'] = "See your dentist. The filling should be checked and may need to be adjusted."
    flowchart['A3'] = "See your dentist if the pain persists for more than a week. Twinges of pain are normal after having a tooth filled."
    flowchart['N4'] = "Do you have repeated episodes of throbbing pain in the tooth?"
    flowchart['A4'] = "See your dentist. The pulp in your tooth may be inflamed because of advanced tooth decay."
    flowchart['N5'] = "Is the pain in your tooth continuous, or is your temperature 100°F or higher?"
    flowchart['A5'] = "See a dentist immediately. You may have a tooth abscess or severe tooth decay."
    flowchart['A6'] = "See your dentist if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N4", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "A1", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "A3", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A5", "Yes"),
        ("N5", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Disturbing_Thoughts_Or_Feelings_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you feel that life is not worth living?"
    flowchart['F1'] = "Depression Flowchart" # change depression flowchart
    flowchart['N2'] = "Do you feel worried or uneasy?"
    flowchart['F2'] = "Anxiety Flowchart" # change anxiety flowchart
    flowchart['N3'] = "Do you worry about your health even though your doctor assures you that you are healthy?"
    flowchart['A1'] = "Talk to your doctor. You may have emotional conflicts that result from depression or anxiety."
    flowchart['N4'] = "Are you concerned that your sexual thoughts, feelings, or fantasies might be abnormal or unhealthy?"
    flowchart['A2'] = "See your doctor if you are concerned about your sexual thoughts or feelings or if you have an urge to act out sexual fantasies involving violence or children. Sexual thoughts and fantasies are common and are usually harmless."
    flowchart['N5'] = "Are your thoughts or feelings particularly aggressive or violent or are you under unusual stress?"
    flowchart['A3'] = "See your doctor if your thoughts or feelings seem out of proportion to the situation or involve harming yourself or others. Aggressive thoughts or feelings often occur in highly stressful situations."
    flowchart['A4'] = "See your doctor if you are unable to make a decision from self-triage and your thoughts or feelings continue to bother you."


    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "F2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A1", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "A4", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Gas_And_Belching_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is the gas expelled by belching?"
    flowchart['N2'] = "Can you taste a sour or bitter fluid when you belch, especially if you are bending over or lying down?"
    flowchart['A1'] = "See your doctor. You may have gastroesophageal reflux disease."
    flowchart['N3'] = "Do you often have a bloated, uncomfortable feeling after meals?"
    flowchart['A2'] = "You may be unconsciously swallowing air while you eat and then regurgitating it to relieve your discomfort."
    flowchart['A3'] = "See your doctor. You probably swallow large amounts of air without realizing it while eating or chewing gum or as a nervous habit."
    flowchart['N4'] = "Have you recently eaten large quantities of high-fiber foods such as beans, bran, or fruit?"
    flowchart['A4'] = "Most high-fiber foods cause gas."
    flowchart['N5'] = "Do you have episodes of lower abdominal pain that are relieved by passing gas or having a bowel movement?"
    flowchart['A5'] = "See your doctor. You may have irritable bowel syndrome."
    flowchart['N6'] = "Are your stools pale, greasy, and foul-smelling?"
    flowchart['A6'] = "See your doctor. You may have an intestinal disorder such as celiac disease."
    flowchart['A7'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [("N1", "N2", "Yes"),
                                ("N1", "N4", "No"),
                                ("N2", "A1", "Yes"),
                                ("N2", "N3", "No"),
                                ("N3", "A2", "Yes"), 
                                ("N3", "A3", "No"),  
                                ("N4", "A4", "Yes"),
                                ("N4", "N5", "No"),
                                ("N5", "A5", "Yes"),
                                ("N5", "N6", "No"),
                                ("N6", "A6", "Yes"),
                                ("N6", "A7", "No")]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Painful_Eye_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did you injure your eye?"
    flowchart['N2'] = "Is there any visible damage to your eye?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. Any damage to the eye requires immediate medical treatment."
    flowchart['N3'] = "Is your vision blurred, or does light hurt your eyes?"
    flowchart['N4'] = "Is the pain severe, or have you had any loss of vision?"
    flowchart['A2'] = "See a doctor immediately if the pain persists or if your vision is impaired."
    flowchart['A3'] = "See a doctor immediately. You could have acute glaucoma or uveitis."
    flowchart['N5'] = "Is your eyeball or eyelid red?"
    flowchart['N6'] = "Does your eyelid seem to be turning inward?"
    flowchart['A4'] = "See your doctor. You may have a disorder of the eyelid called entropion."
    flowchart['N7'] = "Is there swelling in one area of the eyelid?"
    flowchart['A5'] = "See a doctor immediately if the entire eyelid is swollen; you may have an infection of the eyelid. Or you may have a stye."
    flowchart['N8'] = "Does your eye feel gritty?" 
    flowchart['N9'] = "Is your eye sticky?" 
    flowchart['A6'] = "See your doctor. You probably have conjunctivitis."
    flowchart['A7'] = "See your doctor. You may have dry eye."
    flowchart['N10'] = "Is your eye watering?"
    flowchart['A8'] = "You may have a foreign object in your eye."
    flowchart['N11'] = "Does the pain seem to come from behind your eye?"
    flowchart['N12'] = "Do you have two or more of the following symptoms: severe headache; sensitivity of eyes to bright light; pain when you bend your head forward; drowsiness or confusion?"
    flowchart['A9'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have meningitis or a subarachnoid hemorrhage."
    flowchart['A10'] = "See a doctor immediately. You may have temporal arteritis (inflammation of arteries in the head)."
    flowchart['N13'] = "Is there an area of tenderness in the temple above the affected eye?"
    flowchart['N14'] = "Is there an area of tenderness over your nose or in your cheekbones?"
    flowchart['A11'] = "See a doctor immediately. You may have sinusitis. Or you may have an infection of the eye socket."
    flowchart['A12'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "N2", "Yes"), ("N1", "N3", "No"),
        ("N2", "A1", "Yes"), ("N2", "N4", "No"),
        ("N3", "A3", "Yes"), ("N3", "N5", "No"),
        ("N4", "A1", "Yes"), ("N4", "A2", "No"),
        ("N5", "N6", "Yes"), ("N5", "N11", "No"),
        ("N6", "A4", "Yes"), ("N6", "N7", "No"),
        ("N7", "A5", "Yes"), ("N7", "N8", "No"), 
        ("N8", "N9", "Yes"), ("N8", "N10", "No"), 
        ("N9", "A6", "Yes"), ("N9", "A7", "No"),
        ("N10", "A8", "Yes"),("N10", "N11", "No"),
        ("N11", "N12", "Yes"), ("N11", "A12", "No"),
        ("N12", "A9", "Yes"), ("N12", "N13", "No"),
        ("N13", "A10", "Yes"), ("N13", "N14", "No"),
        ("N14", "A11", "Yes"), ("N14", "A12", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Swellings_In_Children_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your child 3 months old or younger?"
    flowchart['A1'] = "Take your child to the doctor. Young babies should always be seen by a doctor if they have a medical problem."
    flowchart['N2'] = "Is the area between your child's ear and the angle of his or her jaw swollen, painful, or tender?"
    flowchart['A2'] = "Take your child to the doctor. Your child may have mumps."
    flowchart['N3'] = "Is there swelling at the back of your child's neck at the base of the skull?"
    flowchart['A3'] = "Take your child to the doctor. Your child may be developing a viral infection such as rubella, especially if he or she also has a rash."
    flowchart['N4'] = "Are the sides of your child's neck swollen?"
    flowchart['N5'] = "Is your child's temperature over 100°F?"
    flowchart['A4'] = "Take your child to the doctor. Your child may have an infection such as tonsillitis, strep throat, pharyngitis, or a tooth abscess. If the symptoms persist for more than a week, he or she may have infectious mononucleosis."
    flowchart['N6'] = "Does your child have a sore, cut, or insect bite on his or her head or neck?"
    flowchart['A5'] = "Call your child's doctor. The glands in your child's neck may be swollen because the wound is infected."
    flowchart['N7'] = "Is there a swelling in your child's armpit or at the base of one side of the neck, above the collarbone?"
    flowchart['N8'] = "Does your child have a sore, cut, or insect bite on his or her hand, arm, or shoulder on the same side as the swelling?"
    flowchart['A6'] = "Call your child's doctor. The glands in your child's armpit or at the base of his or her neck may be swollen because the wound is infected."
    flowchart['N9'] = "Has your child had a vaccination within the past week?"
    flowchart['A7'] = "Call your child's doctor. Glands in the armpit or at the base of the neck sometimes swell in response to a vaccination."
    flowchart['A8'] = "Take your child to the doctor if you are unable to make a decision from self-triage and the swelling persists for more than a week."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N7", "No"), 
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"), 
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "N8", "Yes"),
        ("N7", "A8", "No"), 
        ("N8", "A6", "Yes"),
        ("N8", "N9", "No"), 
        ("N9", "A7", "Yes"),
        ("N9", "A8", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G





def Raised_Spots_And_Lumps_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have a painful, raised red spot with a pale center?"
    flowchart['A1'] = "You may have an infected hair follicle."
    flowchart['N2'] = "Do you have a slow-growing, dark-colored lump, or have you noticed a change in a mole?"
    flowchart['A2'] = "See a doctor immediately. You may have skin cancer."
    flowchart['N3'] = "Do you have a single lump that has been growing?"
    flowchart['A3'] = "See a doctor immediately. You could have a form of skin cancer, especially if the lump has an ulcerated center. However, you probably have a harmless wart."
    flowchart['N4'] = "Do you have one or more patches of thickened skin on your toes?"
    flowchart['A4'] = "You probably have corns."
    flowchart['N5'] = "Do you have several rough-surfaced, hard lumps on your hands or feet?"
    flowchart['A5'] = "You probably have warts."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A5", "Yes"),
        ("N5", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Coughing_In_Children_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your child's temperature over 100°F?"
    flowchart['N2'] = "Is your child's breathing very rapid or noisy, or is he or she gasping for air?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or take your child to the nearest hospital emergency department. He or she may have a serious lung infection such as acute bronchitis, bronchiolitis, or pneumonia."
    flowchart['A2'] = "Call your child's doctor. Your child may have a cold, influenza, or some other respiratory infection."
    flowchart['N3'] = "Is your child having difficulty breathing, or is his or her face blue?"
    flowchart['A3'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or take your child to the nearest hospital emergency department. He or she may be having a severe attack of asthma or croup."
    flowchart['N4'] = "Does your child have episodes of uncontrollable coughing followed by noisy gasping for air?"
    flowchart['A4'] = "Take your child to the doctor immediately. Your child may have whooping cough, especially if he or she has not been vaccinated against the disease."
    flowchart['N5'] = "Is your child's breathing harsh or wheezy?"
    flowchart['A5'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or take your child to the nearest hospital emergency department. Inhaling an object can partially block the airway, causing wheezing and coughing."
    flowchart['N6'] = "Could your child have inhaled a small object or piece of food within the past few days?"
    flowchart['N7'] = "Has your child been exposed to any new cleaning products, or do you have a new pet?"
    flowchart['A6'] = "Take your child to the doctor immediately. Your child may be having an allergic reaction. He or she could also be having an asthma attack."
    flowchart['N8'] = "Does your child have a runny or stuffy nose?"
    flowchart['A7'] = "Call your child's doctor. Discharge from the back of the nose may be irritating your child's throat, making him or her cough. Your child may have a cold, influenza, or an adenoid disorder."
    flowchart['N9'] = "Has your child had whooping cough within the past 3 months?"
    flowchart['A8'] = "Persistent coughing often follows whooping cough."
    flowchart['N10'] = "Does anyone in the house smoke, or could your child be smoking?"
    flowchart['A9'] = "Smoking or breathing in secondhand smoke can produce a cough."
    flowchart['A10'] = "Take your child to the doctor if you are unable to make a decision from self-triage or if your child's cough persists for more than 2 weeks."



    edges_with_conditions = [
                             ("N1", "N2", "Yes"),
                             ("N1", "N3", "No"),
                             ("N2", "A1", "Yes"),
                             ("N2", "A2", "No"),
                             ("N3", "A3", "Yes"),
                             ("N3", "N4", "No"),
                             ("N4", "A4", "Yes"),
                             ("N4", "N5", "No"),
                             ("N5", "N6", "Yes"),
                             ("N5", "N8", "No"),
                             ("N6", "A5", "Yes"), 
                             ("N6", "N7", "No"),
                             ("N7", "A6", "Yes"),
                             ("N7", "N8", "No"),
                             ("N8", "A7", "Yes"),
                             ("N8", "N9", "No"),
                             ("N9", "A8", "Yes"),
                             ("N9", "N10", "No"),
                             ("N10", "A9", "Yes"),
                             ("N10", "A10", "No")]
                             



    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G





def Rash_With_Fever_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have red spots or blotches on your skin?"
    flowchart['N2'] = "Do you have two or more of the following symptoms: runny nose; sore, red eyes; dry cough?"
    flowchart['A1'] = "See your doctor. You may have measles or a similar viral infection, especially if the rash is mainly on your face or trunk."
    flowchart['N3'] = "Do you have swelling down the sides of the back of your neck or at the base of your skull?"
    flowchart['A2'] = "See your doctor. You may have rubella."
    flowchart['N4'] = "Do you have raised, red, itchy spots that turn into blisters?"
    flowchart['A3'] = "See your doctor. You may have chickenpox."
    flowchart['N5'] = "Do you have one or more reddish brown spots that have become bigger and developed a whitish center?"
    flowchart['A4'] = "See your doctor. You may have lyme disease, a viral infection that is spread by ticks."
    flowchart['N6'] = "Do you have a rash of purple spots?"
    flowchart['N7'] = "Do you have two or more of the following symptoms: vomiting; headache; sensitivity of eyes to bright light; pain when you bend your head forward?"
    flowchart['A5'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have meningitis."
    flowchart['A6'] = "See a doctor immediately. You may have a serious blood disorder called allergic purpura."
    flowchart['A7'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N4", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "N7", "Yes"),
        ("N6", "A7", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "A6", "No")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Infertility_In_Men_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you noticed any unusual swelling of your testicles?"
    flowchart['A1'] = "See your doctor. A disorder of the testicles may be affecting your fertility."
    flowchart['N2'] = "Do you have a discharge from your penis, or have you ever had a sexually transmitted disease (STD)?"
    flowchart['A2'] = "See your doctor. Some STDs can lead to infertility."
    flowchart['N3'] = "Did you have mumps after age 12?"
    flowchart['A3'] = "Mumps occasionally causes inflammation of the testicles, which, in rare cases, can affect fertility."
    flowchart['N4'] = "Are you overweight; do you use hot tubs or saunas, wear tight pants, smoke, drink alcohol excessively, use drugs, or eat poorly; are you in poor health; have you had surgery on your reproductive tract; or do you have an abnormality of the reproductive tract?"
    flowchart['A4'] = "See your doctor. Exposing the testicles to consistently high temperatures (as can occur when layers of fat increase the temperature around the testicles or when you use hot tubs or saunas or wear tight pants) reduces sperm count. Smoking, drinking excessively, or using drugs not only lowers sperm count but also reduces sperm motility. Being in generally poor health can also affect your fertility. Having reproductive tract surgery or a structural abnormality of the reproductive tract can obstruct the flow of semen and the passage of sperm."
    flowchart['N5'] = "Do you have intercourse less than once a week?"
    flowchart['A5'] = "Your chances of conception will increase if you have intercourse more frequently, especially if you are able to have intercourse around the time of ovulation."
    flowchart['N6'] = "Do you or your partner have a sexual problem such as difficulty with erections or pain during intercourse?"
    flowchart['A6'] = "See your doctor. Often, failure to conceive results from sexual difficulties."
    flowchart['N7'] = "Is either of you ill, or does either of you have a chronic disease?"
    flowchart['A7'] = "See your doctor. Many illnesses (particularly liver and hormone problems) and the medications used to treat them can sometimes cause infertility."
    flowchart['A8'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A5", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A6", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A7", "Yes"),
        ("N7", "A8", "No")
       
        ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Infertility_In_Women_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Are your periods infrequent or irregular?"
    flowchart['A1'] = "See your doctor. You are probably ovulating infrequently."
    flowchart['N2'] = "Have you ever had an infection of the uterus or fallopian tubes or a sexually transmitted disease?"
    flowchart['A2'] = "See your doctor. The infection may have caused a blockage in your fallopian tubes."
    flowchart['N3'] = "Do you have one or more of the following symptoms: painful periods; abnormal vaginal discharge; recurring lower abdominal pain?"
    flowchart['A3'] = "See your doctor. You may have a disorder such as endometriosis or pelvic inflammatory disease."
    flowchart['N4'] = "Are you over age 35?"
    flowchart['A4'] = "See your doctor. Fertility declines as you get older."
    flowchart['N5'] = "Do you have intercourse less than once a week?"
    flowchart['A5'] = "Your chances of conception will increase if you have intercourse more frequently, especially if you are able to have intercourse around the time of ovulation."
    flowchart['N6'] = "Do you or your partner have a sexual problem such as difficulty with erections or pain during intercourse?"
    flowchart['A6'] = "See your doctor. Often, failure to conceive results from sexual difficulties."
    flowchart['N7'] = "Is either of you ill, or does either of you have a chronic disease?"
    flowchart['A7'] = "See your doctor. Many illnesses (particularly liver and hormone problems) and the medications used to treat them can sometimes cause infertility."
    flowchart['A8'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A5", "Yes"), 
        ("N5", "N6", "No"), 
        ("N6", "A6", "Yes"), 
        ("N6", "N7", "No"), 
        ("N7", "A7", "Yes"), 
        ("N7", "A8", "No")     
        ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Hearing_Loss_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have an earache?"
    flowchart['F1'] = "Earache Flowchart" # change to earache flowchart
    flowchart['N2'] = "Does your ear have a sticky yellow discharge?"
    flowchart['A1'] = "See your doctor. Your hearing loss may be caused by an ear infection. Or you could have a ruptured or perforated eardrum or a disorder of the middle ear called cholesteatoma."
    flowchart['N3'] = "Have you had a cold or a sore throat in the past week?"
    flowchart['A2'] = "See your doctor if your hearing does not improve within 3 days. Your eustachian tube, which connects the middle ear and the back of the throat, may have become blocked as a result of a cold."
    flowchart['N4'] = "Can you hear low-pitched sounds (such as a knock on the door) better than you hear high-pitched sounds (such as a doorbell)?"
    flowchart['N5'] = "Are you routinely exposed to very loud noises at work (such as loud machinery), or do you frequently go to noisy places (such as rock concerts or a firing range)?"
    flowchart['A3'] = "See your doctor. Prolonged exposure to high noise levels can permanently damage hearing."
    flowchart['N6'] = "Are you taking or have you recently taken any nonprescription or prescription medications?"
    flowchart['A4'] = "Talk to your doctor. Hearing loss is a possible side effect of some medications, including aspirin."
    flowchart['N7'] = "Do you have occasional episodes of dizziness that make the room seem to spin?"
    flowchart['A5'] = "See your doctor. You may have an inner ear disorder called meniere's disease."
    flowchart['N8'] = "Are you over 60?"
    flowchart['A6'] = "Talk to your doctor. Hearing loss that occurs as a natural part of aging can often be treated."
    flowchart['N9'] = "Has your hearing worsened over a period of several weeks or longer?"
    flowchart['N10'] = "Have other members of your family had a gradual loss of hearing?"
    flowchart['A7'] = "See your doctor. You may have otosclerosis, a disorder that affects the middle ear."
    flowchart['A8'] = "See your doctor. An earwax blockage may be causing your hearing loss."
    flowchart['A9'] = "See your doctor if you are unable to make a decision from self-triage."
    

    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N6", "No"),  
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A6", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "N10", "Yes"),
        ("N9", "A9", "No"),
        ("N10", "A7", "Yes"),
        ("N10", "A8", "No")  
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

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
    G.add_nodes_from(flowchart.keys())

    # Add edges to the graph
    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Wheezing_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did you begin wheezing within the past few hours?"
    flowchart['N2'] = "Have you coughed up mucus that is frothy and pink or white?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have congestive heart failure."
    flowchart['N3'] = "Do you have a feeling of tightness in your chest, or do you feel as if you are suffocating?"
    flowchart['A2'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may be having a severe asthma attack. Or you may be hyperventilating."
    flowchart['A3'] = "See a doctor immediately if you have not been previously diagnosed with asthma. You are probably having a mild asthma attack."
    flowchart['N4'] = "Is your temperature 100°F or higher?"
    flowchart['A4'] = "See your doctor. You may have acute bronchitis."
    flowchart['N5'] = "Do you wheeze on most days?"
    flowchart['N6'] = "Do you cough up gray or greenish yellow phlegm on most days?"
    flowchart['A5'] = "See your doctor. You may have a lung disease such as chronic bronchitis or emphysema."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."

    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N4", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "A3", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "N6", "Yes"),
        ("N5", "A6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())


    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Numbness_Or_Tingling_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did you experience the numbness or tingling after sitting in one position for a long time or right after waking from a deep sleep?"
    flowchart['A1'] = "Stretching or pressing on a nerve or temporarily cutting off its blood supply often causes such sensations. Feeling in the affected area should return to normal in a few minutes."
    flowchart['N2'] = "Are only your hands affected?"
    flowchart['N3'] = "Are you over 50, and is your neck occasionally painful or stiff?"
    flowchart['A2'] = "See your doctor. You may have a disorder of the nerves and bones in the neck called cervical osteoarthritis."
    flowchart['N4'] = "Do you have pain in your hand or arm, or are your symptoms worse at night?"
    flowchart['A3'] = "See your doctor. You could have carpal tunnel syndrome, a disorder of the nerves that pass through the wrist."
    flowchart['N5'] = "Does the numbness or tingling affect only one side of your body?"
    flowchart['N6'] = "Did you have one or more of the following symptoms before or after the numbness or tingling began: difficulty speaking; blurred vision; confusion; dizziness; weakness in the arms or legs?"
    flowchart['A4'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have had a stroke or a transient ischemic attack. Or you may have multiple sclerosis."
    flowchart['N7'] = "Do your fingers or toes get numb and turn blue in cold weather, and then become red and painful as feeling returns?"
    flowchart['A5'] = "See your doctor. You may have a disorder called raynaud's disease, which affects the small blood vessels in the hands and feet."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [("N1", "A1", "Yes"),
                             ("N1", "N2", "No"),
                             ("N2", "N3", "Yes"),
                             ("N2", "N5", "No"),
                             ("N3", "A2", "Yes"),
                             ("N3", "N4", "No"),
                             ("N4", "A3", "Yes"),
                             ("N4", "N5", "No"),
                             ("N5", "N6", "Yes"),
                             ("N5", "N7", "No"),
                             ("N6", "A4", "Yes"),
                             ("N6", "N7", "No"),
                             ("N7", "A5", "Yes"),
                             ("N7", "A6", "No")]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Painful_Shoulder_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did you injure your shoulder within the past 24 hours?"
    flowchart['N2'] = "Is it impossible or very painful to move your shoulder, or does your shoulder seem misshapen?"
    flowchart['A1'] = "See a doctor immediately. You may have broken or dislocated your shoulder."
    flowchart['N3'] = "Did the pain begin suddenly?"
    flowchart['A2'] = "See your doctor. You may have pulled or torn a muscle or ligament."
    flowchart['N4'] = "Do you have pain, swelling, or redness in other joints, such as your finger joints?"
    flowchart['A3'] = "See your doctor. You may have rheumatoid arthritis."
    flowchart['N5'] = "Is your temperature 100°F or higher, or have you recently started to feel ill?"
    flowchart['N6'] = "Does the pain occur only when you move your arm?"
    flowchart['A5'] = "See your doctor. You may have inflammation and thickening of the lining of the joint capsule."
    flowchart['A4'] = "See your doctor. You may have bursitis or tendinitis."
    flowchart['N7'] = "Has your shoulder become increasingly painful and stiff over several weeks, and are you barely able to move your arm?"
    flowchart['A6'] = "See your doctor. You may have bursitis."
    flowchart['A7'] = "See a doctor immediately. Your shoulder pain may be angina."
    flowchart['A9'] = "See your doctor if you are unable to make a decision from self-triage."
    flowchart['N8'] = "Does the pain occur when you exert yourself or exercise the shoulder, and subside when you stop?"
    flowchart['A8'] = "See your doctor. You may have rheumatic fever, which is especially common in children. Or you could have tendinitis."



    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "A2", "No"),
        ("N3", "N5", "Yes"),
        ("N3", "N4", "No"),  
        ("N4", "A3", "Yes"),
        ("N4", "N6", "No"),
        ("N5", "A8", "Yes"),
        ("N5", "A4", "No"),
        ("N6", "N7", "Yes"),
        ("N6", "N8", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "A6", "No"),
        ("N8", "A7", "Yes"), 
        ("N8", "A9", "No")
    ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Vomiting_In_Infants_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does your baby seem healthy except for the vomiting?"
    flowchart['N2'] = "Is your baby gaining weight?"
    flowchart['A1'] = "Take your child to the doctor immediately. Vomiting that is severe enough to prevent a baby from gaining weight at the usual rate may indicate an intestinal obstruction."
    flowchart['N3'] = "Does your baby spit up small amounts of breast milk or formula during or just after feedings?"
    flowchart['A2'] = "Spitting up small amounts of breast milk or formula, especially if your baby is very active, is probably not a cause for concern."
    flowchart['A3'] = "The hole in the nipple may be the wrong size. A too-small hole can make your baby swallow air, which can overfill the stomach and cause burping. Or the hole may be too large, causing your baby to gulp the milk or formula."
    flowchart['N4'] = "Are you bottle-feeding your baby?"
    flowchart['N5'] = "Have you recently started using a new nipple on the bottle?"
    flowchart['N6'] = "Is your baby younger than 3 months, and does the vomit shoot forcefully from his or her mouth right after feedings?"
    flowchart['A4'] = "Call your child's doctor. Vomiting forcefully (called projectile vomiting) once in a while is usually not a cause for concern. However, if it happens regularly, your baby may have an intestinal obstruction, which is an emergency."
    flowchart['A5'] = "A single episode of vomiting in an otherwise healthy baby is no cause for concern."
    flowchart['N7'] = "Has your baby had three to four watery stools within 24 hours?"
    flowchart['A6'] = "Call your child's doctor immediately. Your baby has diarrhea, possibly from an infection of the digestive tract."
    flowchart['N8'] = "Is your baby's temperature over 100°F?"
    flowchart['F1'] = "Fever In Young Children Flowchart" #change to fever in young children flowchart
    flowchart['N9'] = "Does your baby have a cough or a runny nose?"
    flowchart['A7'] = "Call your child's doctor if the vomiting concerns you. However, swallowing mucus from a cold or other respiratory infection is probably causing the vomiting."
    flowchart['N10'] = "Is your baby crying as if from pain?"
    flowchart['A8'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or take your child to the nearest hospital emergency department. He or she may have an intestinal obstruction such as intussusception."
    flowchart['A9'] = "Call your child's doctor if you are unable to make a decision from self-triage."
    


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N7", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "A1", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N6", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "A5", "No"), 
        ("N7", "A6", "Yes"), 
        ("N7", "N8", "No"),
        ("N8", "F1", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A7", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A9", "No"),
        ("N10", "A8", "Yes")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Painful_Intercourse_In_Women_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Was this your first experience with intercourse, or is this a new sexual relationship?"
    flowchart['A1'] = "Bruising or soreness can sometimes occur in these circumstances. Wait a couple of days before having intercourse again."
    flowchart['N2'] = "Did you recently have a baby?"
    flowchart['A2'] = "This is a common problem after childbirth, especially if you had stitches."
    flowchart['N3'] = "Does the pain occur at the entrance to the vagina?"
    flowchart['A3'] = "You may be tense, which can lead to pain or discomfort during intercourse."
    flowchart['N4'] = "Do you have an unusual vaginal discharge?"
    flowchart['F1'] = "Abnormal Vaginal Discharge Flowchart" # change to abnormal vaginal discharge flowchart
    flowchart['N5'] = "Do you have persistent itching around the genital area?"
    flowchart['F2'] = "Vaginal Irritation Flowchart" #change to vaginal irritation flowchart
    flowchart['N6'] = "Are you urinating more often than usual?"
    flowchart['A4'] = "See your doctor. Your bladder may be inflamed from an infection."
    flowchart['N7'] = "Does your vagina seem dry, making penetration uncomfortable and difficult?"
    flowchart['N8'] = "Are you over age 45?"
    flowchart['A5'] = "Some dryness of vaginal tissues caused by a decrease in estrogen is common after menopause."
    flowchart['A6'] = "Insufficient lubrication of your vagina may be the problem."
    flowchart['N9'] = "Do you have a sharp pain deep in your pelvis during intercourse?"
    flowchart['N10'] = "Are your periods more painful than they used to be?"
    flowchart['A7'] = "See your doctor. You may have a disorder such as endometriosis fibroids."
    flowchart['N11'] = "Do you have pain only when you have intercourse in certain positions?"
    flowchart['A8'] = "The pain may result from pressure on a pelvic organ during intercourse."
    flowchart['N12'] = "Does your vagina seem so small that penetration is difficult?"
    flowchart['A9'] = "See your doctor. Your problem probably results from an involuntary spasm, or tightening, of the muscles around the lower part of the vagina."
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"), ("N1", "N2", "No"),
        ("N2", "N3", "Yes"), ("N3", "A2", "Yes"),
        ("N2", "N4", "No"), ("N3", "A3", "No"),
        ("N4", "F1", "Yes"), ("N4", "N5", "No"),
        ("N5", "F2", "Yes"), ("N5", "N6", "No"),
        ("N6", "A4", "Yes"), ("N6", "N7", "No"),  
        ("N7", "N8", "Yes"), ("N8", "A5", "Yes"),
        ("N8", "A6", "No"), ("N7", "N9", "No"),
        ("N9", "N10", "Yes"), ("N10", "N11", "No"),
        ("N10", "A7", "Yes"), ("N11", "A8", "Yes"),
        ("N9", "N12", "No"), ("N11", "N12", "No"),
        ("N12", "A9", "Yes"), ("N12", "A10", "No")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Excessive_Sweating_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you sweat a lot on most days?"
    flowchart['N2'] = "Are you overweight according to the body mass index?"
    flowchart['A1'] = "See your doctor. If you are overweight, even routine physical activity can cause sweating."
    flowchart['N3'] = "Do you have two or more of the following symptoms: unexplained weight loss; increased appetite; weakness or trembling; bulging eyes; rapid heartbeat?"
    flowchart['A2'] = "See your doctor. You could have an overactive thyroid gland."
    flowchart['N4'] = "Does the sweating occur mainly at night, even though you are not using heavy blankets?"
    flowchart['N5'] = "Do you have a persistent cough, or have you lost weight?"
    flowchart['A3'] = "See a doctor immediately. You may have a serious chronic infection such as tuberculosis or HIV. Or you could have a type of cancer such as hodgkin's disease."
    flowchart['N6'] = "Is your temperature 100°F or higher?"
    flowchart['I1'] = "Sweating is the normal response to fever."
    flowchart['F1'] = "Fever Flowchart" # change to fever flowchart
    flowchart['N7'] = "Are you a woman over 40?"
    flowchart['N8'] = "Have your periods become irregular?"
    flowchart['A4'] = "Increased perspiration is common in women who are approaching menopause."
    flowchart['N9'] = "Does the sweating occur only during your periods?"
    flowchart['A5'] = "It is normal for many women to perspire more than usual during their period."
    flowchart['N10'] = "Did you begin sweating after taking large doses of aspirin or drinking alcohol?"
    flowchart['A6'] = "See your doctor if aspirin seems to be the cause. Alcohol can increase perspiration."
    flowchart['N11'] = "Are you wearing clothes made of a synthetic fiber such as nylon?"
    flowchart['A7'] = "Most synthetic fibers increase perspiration because they do not absorb moisture or allow the skin to breathe. Wear clothes made of absorbent natural fibers such as cotton or wool if possible."
    flowchart['N12'] = "Is the sweating problem just with your feet?"
    flowchart['A8'] = "Many people have sweaty feet. Avoid wearing socks or shoes made of synthetic materials, which can increase perspiration. Wash and dry your feet once or twice a day, and sprinkle a foot powder on your feet."
    flowchart['N13'] = "Does the sweating occur only when you are nervous or excited?"
    flowchart['A9'] = "Increased perspiration is common during times of emotional stress."
    flowchart['N14'] = "Are you a teenager?"
    flowchart['A10'] = "It is normal to sweat more, especially to have sweaty palms, during adolescence."
    flowchart['A11'] = "See your doctor if you are unable to make a decision from self-triage or if you are concerned about the excessive sweating."



    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N6", "No"),
        ("N2", "N3", "No"),
        ("N2", "A1", "Yes"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N6", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "I1", "Yes"),
        ("I1", "F1", None),
        ("N6", "N7", "No"),
        ("N7", "N8", "Yes"),
        ("N7", "N10", "No"),  
        ("N8", "A4", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A5", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A6", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A7", "Yes"),
        ("N11", "N12", "No"),
        ("N12", "A8", "Yes"),
        ("N12", "N13", "No"),
        ("N13", "A9", "Yes"),
        ("N13", "N14", "No"),
        ("N14", "A10", "Yes"),
        ("N14", "A11", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Anxiety_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you feel anxious most of the time?"
    flowchart['N2'] = "Have you been feeling anxious only since giving up cigarettes, alcohol, or drugs such as sleep medications?"
    flowchart['A1'] = "Talk to your doctor. Anxiety often follows the sudden withdrawal of tobacco, alcohol, or other drugs."
    flowchart['N3'] = "Have you lost weight, or do your eyes seem to be bulging?"
    flowchart['A2'] = "See your doctor. You may have an overactive thyroid gland."
    flowchart['A3'] = "See your doctor. Your anxiety may be brought on by stress."
    flowchart['N4'] = "Do you feel anxious only in specific situations—for example, when you are in a confined space or when you are unable to do things a certain way?"
    flowchart['A4'] = "See your doctor. Your anxiety may result from a phobia or from obsessive-compulsive disorder."
    flowchart['A5'] = "See your doctor if you are unable to make a decision from self-triage."



    edges_with_conditions = [("N1", "N2", "Yes"),
                                ("N1", "N4", "No"),
                                ("N2", "A1", "Yes"),
                                ("N2", "N3", "No"),
                                ("N3", "A2", "Yes"),
                                ("N3", "A3", "No"),
                                ("N4", "A4", "Yes"),
                                ("N4", "A5", "No")]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Slow_Weight_Gain_In_Young_Children_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does your child seem to be generally healthy in spite of the slow weight gain?"
    flowchart['N2'] = "Was your child less than 5½ pounds at birth?"
    flowchart['A1'] = "A small baby (especially one who is full-term rather than preterm), although healthy, may be smaller than the average person throughout his or her life."
    flowchart['N3'] = "Is either parent smaller than average?"
    flowchart['A2'] = "Your child probably has the body type and size of the smaller parent."
    flowchart['N4'] = "Is your child younger than a year?"
    flowchart['N5'] = "Are you breastfeeding?"
    flowchart['A3'] = "Your baby's slow weight gain may result from underfeeding. Feed your baby whenever he or she is hungry, at least every few hours if he or she is very young."
    flowchart['N6'] = "Is your baby on a rigid breastfeeding schedule?"
    flowchart['N7'] = "Are you bottle-feeding?"
    flowchart['N8'] = "Could you be adding too much water to the formula, or diluting formula that is ready-to-serve?"
    flowchart['A4'] = "Your baby is probably not getting enough nourishment. Read and carefully follow the directions for preparing the formula, and make sure that the formula contains adequate amounts of calories and nutrients."
    flowchart['A5'] = "Your baby may still be hungry. As your baby grows, increase the amount of formula you offer."
    flowchart['N9'] = "Does your baby always finish all the formula?"
    flowchart['N10'] = "Does your baby often vomit after feedings?"
    flowchart['A6'] = "Take your child to the doctor. A digestive tract disorder such as an intestinal obstruction may be causing the vomiting and preventing your baby from gaining weight. Your baby may also be dehydrated if he or she is not getting sufficient nutrients and fluid."
    flowchart['N11'] = "Does your child have loose, pale, bulky, and bad-smelling bowel movements?"
    flowchart['A7'] = "Take your child to the doctor. Your child may have a digestive tract disorder such as celiac disease or lactose intolerance."
    flowchart['N12'] = "Is your child taking a corticosteroid medication for a disorder such as asthma?"
    flowchart['A8'] = "Call your child's doctor. Corticosteroid medications can sometimes affect growth."
    flowchart['A9'] = "Take your child to the doctor if you are unable to make a decision from self-triage."
   



    edges_with_conditions = [
                            ("N1", "N2", "Yes"),
                            ("N1", "N4", "No"),
                            ("N2", "A1", "Yes"),
                            ("N2", "N3", "No"),
                            ("N3", "A2", "Yes"),
                            ("N3", "N4", "No"),
                            ("N4", "N5", "Yes"),
                            ("N4", "N11", "No"),
                            ("N5", "N6", "Yes"),
                            ("N5", "N7", "No"),
                            ("N6", "A3", "Yes"),
                            ("N6", "N7", "No"),
                            ("N7", "N8", "Yes"),
                            ("N7", "N10", "No"),
                            ("N8", "A4", "Yes"),
                            ("N8", "N9", "No"),
                            ("N9", "A5", "Yes"),
                            ("N9", "N10", "No"),
                            ("N10", "A6", "Yes"),
                            ("N10", "N11", "No"),
                            ("N11", "A7", "Yes"),
                            ("N11", "N12", "No"),
                            ("N12", "A8", "Yes"),
                            ("N12", "A9", "No")]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Irregular_Vaginal_Bleeding_Flowchart():
   flowchart = {}
  
   flowchart['N1'] = "Could you be pregnant?"
   flowchart['N2'] = "Could you be more than 3 months pregnant?"
   flowchart['A1'] = "See a doctor immediately. Bleeding 3 months or more into a pregnancy may be a sign of an impending miscarriage."
   flowchart['N3'] = "Do you have severe abdominal pain?" 
   flowchart['A2'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. A pregnancy may be developing outside the uterus."
   flowchart['N4'] = "Has your pregnancy been confirmed?"
   flowchart['A3'] = "See a doctor immediately. Some women have slight vaginal bleeding, or spotting, early in a pregnancy. However, you may be having a miscarriage."
   flowchart['N5'] = "Did you have your last period more than 6 months ago?"
   flowchart['A4'] = "See a doctor immediately. You could be pregnant. However, vaginal bleeding can also be a sign of cancer of the uterus or cancer of the cervix, especially if you are over age 45."
   flowchart['N6'] = "Do you have a heavy, watery vaginal discharge, or does the bleeding occur immediately after intercourse?"
   flowchart['A5'] = "See a doctor immediately. You may have cancer of the cervix or cancer of the uterus."
   flowchart['N7'] = "Do you have an intrauterine device (IUD)?"
   flowchart['N8'] = "Do you have severe abdominal pain?"
   flowchart['A6'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. A pregnancy may be developing outside the uterus."
   flowchart['A7'] = "See your doctor. An IUD sometimes causes vaginal bleeding."
   flowchart['N9'] = "Are you taking an oral contraceptive?"
   flowchart['A8'] = "Talk to your doctor. You are probably having breakthrough bleeding, which is common in women taking oral contraceptives."
   flowchart['N10'] = "Was the bleeding like that of a period?"
   flowchart['N11'] = "Have you started your periods within the past 3 years?"
   flowchart['A9'] = "Talk to your doctor. Irregular periods are common during the first 3 years of menstruation."
   flowchart['N12'] = "Are you in your 40s?"
   flowchart['A10'] = "Talk to your doctor. Irregular periods are common as women approach menopause."
   flowchart['A11'] = "See your doctor if you are unable to make a decision from self-triage."

   edges_with_conditions = [("N1", "N2", "Yes"),
                           ("N1", "N5", "No"),
                           ("N2", "A1", "Yes"),
                           ("N2", "N3", "No"),
                           ("N3", "A2", "Yes"),
                           ("N3", "N4", "No"),
                           ("N4", "A3", "Yes"),
                           ("N4", "N5", "No"),
                           ("N5", "A4", "Yes"),
                           ("N5", "N6", "No"),
                           ("N6", "A5", "Yes"),
                           ("N6", "N7", "No"),
                           ("N7", "N8", "Yes"),
                           ("N7", "N9", "No"),
                           ("N8", "A6", "Yes"),
                           ("N8", "A7", "No"),
                           ("N9", "A8", "Yes"),
                           ("N9", "N10", "No"),
                           ("N10", "N11", "Yes"),
                           ("N11", "A9", "Yes"),
                           ("N11", "N12", "No"),
                           ("N12", "A10", "Yes"),
                           ("N12", "A11", "No"),
                           ("N10", "A11", "No")]

   G = nx.DiGraph()
   G.add_nodes_from(flowchart.keys())

   for edge in edges_with_conditions:
       G.add_edge(edge[0], edge[1], condition=edge[2])
  
   return flowchart, G



def Palpitations_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you been drinking caffeine-containing beverages such as coffee or cola, or have you been smoking more than usual?"
    flowchart['A1'] = "Caffeine and nicotine are stimulants and can increase your heart rate. Cut down on your caffeine and nicotine intake, and the palpitations should subside in a few hours."
    flowchart['N2'] = "Are you under stress?"
    flowchart['A2'] = "Palpitations are a common symptom of anxiety."
    flowchart['N3'] = "Have you recently lost weight even though you are eating no less than usual?"
    flowchart['A3'] = "See your doctor. You may have an overactive thyroid gland."
    flowchart['N4'] = "Is your temperature 100°F or higher?"
    flowchart['I1'] = "A fever can cause palpitations."
    flowchart['F1'] = "Fever Flowchart" # change to fever flowchart
    flowchart['N5'] = "Do you feel ill, do you have any chest discomfort, or have you had irregular heartbeats or other heart problems?"
    flowchart['A4'] = "See a doctor immediately. You may have a disorder of heart rate or rhythm."
    flowchart['A5'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [("N1", "A1", "Yes"),
                            ("N1", "N2", "No"),
                            ("N2", "A2", "Yes"),
                            ("N2", "N3", "No"),
                            ("N3", "A3", "Yes"),
                            ("N3", "N4", "No"),
                            ("N4", "I1", "Yes"),
                            ("I1", "F1", None),
                            ("N4", "N5", "No"),
                            ("N5", "A4", "Yes"),
                            ("N5", "A5", "No")]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

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
    G.add_nodes_from(flowchart.keys())


    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Crying_In_Infants_Flowchart():
    flowchart = {}

    flowchart['N1'] = "When not crying, is your baby irritable, listless, or eating poorly?" 
    flowchart['N2'] = "Is your baby's temperature over 100°F?"
    flowchart['F1'] = "Fever In Young Children Flowchart" # change to fever in younf children flowchart
    flowchart['A1'] = "Talk to your child's doctor. Your baby may have a minor illness such as a cold or a mild case of gastroenteritis, or he or she may be teething. However, he or she may have a more serious illness."
    flowchart['N3'] = "Is your baby less than 3 months old?"
    flowchart['N4'] = "Does your baby usually cry for a long period in the late afternoon or early evening?"
    flowchart['A2'] = "Talk to your child's doctor. Your baby may have colic."
    flowchart['N5'] = "Does your baby start crying just as he or she is falling asleep?"
    flowchart['A3'] = "Small muscle spasms and twitches that occur just before sleep may jerk your baby awake."
    flowchart['N6'] = "Could your baby be cold?"
    flowchart['A4'] = "Keep the temperature of your home at least 68°F and make sure your baby is adequately dressed. Don't expose your baby to extremely cold outside temperatures unnecessarily or without the proper clothing for the weather. Make sure that his or her head is covered and loosely cover his or her nose and mouth with a scarf or blanket."
    flowchart['N7'] = "Does your baby generally stop crying when you pick him or her up?"
    flowchart['A5'] = "Your baby is probably bored or lonely. Be sure to interact with your baby often throughout the day. Try offering a little more attention or place the baby where he or she can see you. Some babies settle down when they are given a favorite toy or blanket."
    flowchart['N8'] = "Does your baby's bottom look red or have a rash?"
    flowchart['A6'] = "Diaper rash may be making your baby uncomfortable."
    flowchart['N9'] = "Does your baby stop crying after being fed?"
    flowchart['N10'] = "Does your baby start crying again less than 2 hours after a feeding?"
    flowchart['A7'] = "You may not be providing enough food. If you are breastfeeding, nurse your baby more often and longer. If you are bottle-feeding, increase the amount of formula."
    flowchart['A8'] = "Try feeding your baby whenever he or she cries to make sure he or she is not hungry."
    flowchart['A9'] = "Call your child's doctor if the crying worries you and you are unable to make a decision from self-triage."

   

    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "F1", "Yes"),
        ("N2", "A1", "No"),
        ("N3", "N4", "Yes"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),  
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),  
        ("N3", "N6", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "N7", "No"), 
        ("N7", "A5", "Yes"), 
        ("N7", "N8", "No"), 
        ("N8", "A6", "Yes"), 
        ("N8", "N9", "No"), 
        ("N9", "N10", "Yes"),
        ("N10", "A7", "Yes"),
        ("N10", "A8", "No"),
        ("N9", "A9", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G


def Abdominal_Pain_In_Children_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does even the slightest movement seem to hurt so much that your child screams with pain?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or take your child to the nearest hospital emergency department. He or she could have appendicitis."
    flowchart['N2'] = "Has your child overeaten or eaten anything (such as a spicy food) that could have upset his or her stomach?"
    flowchart['A2'] = "Your child probably has indigestion."
    flowchart['N3'] = "Has your child had three to four watery bowel movements within 24 hours or been vomiting?"
    flowchart['A3'] = "Take your child to the doctor. Your child may have an infection of the digestive tract such as gastroenteritis or he or she could have food poisoning."
    flowchart['N4'] = "Has your child not had a bowel movement in 2 or 3 days, or does he or she have difficulty passing stools?"
    flowchart['A4'] = "Talk to your child's doctor. Your child may be constipated."
    flowchart['N5'] = "Does your child have a runny nose or a sore throat?"
    flowchart['N6'] = "Is your child urinating frequently, or is urination painful?"
    flowchart['A5'] = "Children often have abdominal pain when they have a cold or other respiratory infection because they swallow mucus, which can upset the stomach." 
    flowchart['A6'] = "Take your child to the doctor. Your child may have a urinary tract infection."
    flowchart['N7'] = "Did your child seem healthy before the abdominal pain started?"
    flowchart['N8'] = "Does your child often have this type of abdominal pain?"
    flowchart['A7'] = "Take your child to the doctor. Although many children who are generally healthy get regular attacks of abdominal pain, your child may have an underlying disorder that is causing the pain."
    flowchart['A8'] = "Take your child to the doctor if you are unable to make a decision from self-triage."
    

    edges_with_conditions = [("N1", "A1", "Yes"),
                                ("N1", "N2", "No"),
                                ("N2", "A2", "Yes"),
                                ("N2", "N3", "No"),
                                ("N3", "A3", "Yes"),
                                ("N3", "N4", "No"),
                                ("N4", "A4", "Yes"),
                                ("N4", "N5", "No"),  
                                ("N5", "A5", "Yes"),  
                                ("N5", "N6", "No"),
                                ("N6", "A6", "Yes"),
                                ("N6", "N7", "No"),
                                ("N7", "N8", "Yes"),
                                ("N7", "A8", "No"),  
                                ("N8", "A7", "Yes"),
                                ("N8", "A8", "No")] 
                                

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Confusion_In_Older_People_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you been feeling confused only recently?"
    flowchart['N2'] = "Have you recently started taking a new medication or changed the dose of one you have been taking?"
    flowchart['A1'] = "Talk to your doctor. He or she may change the dosage or prescribe a different medication or tell you to stop taking the medication."
    flowchart['N3'] = "Did the confusion begin in the days or weeks after a fall or head injury?"
    flowchart['A2'] = "See a doctor immediately. These symptoms suggest the possibility of bleeding inside the skull."
    flowchart['N4'] = "Have you noticed two or more of the following symptoms: change in personality; decline in personal appearance or cleanliness; impaired ability to remember recent events?"
    flowchart['A3'] = "See a doctor immediately. These symptoms may indicate the onset of alzheimer's disease. You may have had several minor strokes. Or you may have a brain tumor."
    flowchart['N5'] = "Is the confusion accompanied by signs of illness such as a fever, coughing, or lack of bladder control?"
    flowchart['A4'] = "See a doctor immediately. Many physical illnesses can cause these symptoms along with confusion in older people."
    flowchart['N6'] = "Do you feel very cold or chilled, or does your abdomen feel unusually cold?"
    flowchart['A5'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. Feeling cold along with being confused can indicate a dangerous drop in body temperature."
    flowchart['N7'] = "Do you feel hot, is the weather very hot and humid, or have you been out in the sun?"
    flowchart['A6'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. Your confusion may be the result of exposure to very hot conditions."
    flowchart['N8'] = "Have you gone without eating for some time?"
    flowchart['A7'] = "Have something to eat or drink, especially if you have a condition such as diabetes. See your doctor if the confusion persists."
    flowchart['A8'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N5", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"), 
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "A8", "No")]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Vaginal_Irritation_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have a vaginal discharge that is different than usual in color or consistency?"
    flowchart['F1'] = "Abnormal Vaginal Discharge Flowchart" # change to abnormal vaginal discharge flowchart
    flowchart['N2'] = "Do you use a vaginal douche or spray or a spermicidal cream or jelly?"
    flowchart['A1'] = "See your doctor if a spermicide seems to be causing the problem or if the irritation persists. You should not use vaginal douches or sprays because they can eliminate helpful bacteria from the vagina and can cause irritation."
    flowchart['N3'] = "Does the skin around your vagina look abnormal?"
    flowchart['A2'] = "See your doctor. The irritation may result from a skin disorder."
    flowchart['N4'] = "Does any other part of your body itch?"
    flowchart['F2'] = "Itching Without A Rash Flowchart" # change to itching without a rash flowchart
    flowchart['N5'] = "Do you seem to be producing more urine than usual, or do you get up at night to urinate?"
    flowchart['N6'] = "Have you noticed one or more of the following symptoms: increased thirst; loss of weight; unexplained fatigue?"
    flowchart['A3'] = "See your doctor. You may have diabetes."
    flowchart['N7'] = "Are you over age 45?"
    flowchart['A4'] = "Talk to your doctor. The irritation is probably the result of hormonal changes brought on by menopause."
    flowchart['A5'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [("N1", "F1", "Yes"),
                                ("N1", "N2", "No"),
                                ("N2", "A1", "Yes"),
                                ("N2", "N3", "No"),
                                ("N3", "A2", "Yes"), 
                                ("N3", "N4", "No"),
                                ("N4", "F2", "Yes"),
                                ("N4", "N5", "No"), 
                                ("N5", "N6", "Yes"),
                                ("N5", "N7","No"), 
                                ("N6", "A3", "Yes"),
                                ("N6", "N7", "No"), 
                                ("N7", "A4", "Yes"),
                                ("N7", "A5", "No")]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Abnormal_Looking_Urine_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your urine dark yellow or orange?"
    flowchart['N2'] = "Is your temperature 100°F or higher, is the weather very hot, or have you been exercising?"
    flowchart['A1'] = "Losing fluid through perspiration concentrates the urine, making it darker than usual. Drink more fluids, especially water."
    flowchart['N3'] = "Have you been vomiting or have you had diarrhea?"
    flowchart['A2'] = "Loss of fluid through vomiting or diarrhea can concentrate the urine, making it darker. Drink more fluids, especially water or a rehydration solution or sports drink."
    flowchart['N4'] = "Is your urine dark brown but clear?"
    flowchart['N5'] = "Are your stools pale, or do the whites of your eyes and your skin look yellow?"
    flowchart['A3'] = "See your doctor. You may have jaundice caused by a liver disorder."
    flowchart['N6'] = "Is urination painful?"
    flowchart['F1'] = "Painful Urination Flowchart" # change to painful urination flowchart
    flowchart['N7'] = "Is your urine pink, red, or smoky brown?"
    flowchart['N8'] = "Are you taking a laxative that contains senna, or have you started to take any new medications or vitamins within the past 24 hours?"
    flowchart['A4'] = "Senna contains substances that can darken the urine temporarily, and some drugs (including some vitamins) can darken urine."
    flowchart['N9'] = "Have you eaten any foods within the past 24 hours that contain red or dark artificial dyes (such as brightly colored candies) or that are dark in color (such as rhubarb, beets, or blackberries)?"
    flowchart['A5'] = "Many artificial food dyes and the natural coloring of some foods can discolor urine."
    flowchart['A6'] = "See a doctor immediately. You may have blood in your urine or a urinary tract infection such as cystitis. There is also a slight chance that you may have a kidney tumor, bladder tumor, or tuberculosis. If you are a man, you may have an enlarged prostate gland."
    flowchart['N10'] = "Is your urine green or blue?"
    flowchart['A7'] = "Green or blue urine is almost always the result of artificial coloring in food or medication."
    flowchart['A8'] = "See your doctor if you are unable to make a decision from self-triage."
   


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N4", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N6", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "F1", "Yes"),
        ("N6", "N7", "No"),  
        ("N7", "N8", "Yes"),
        ("N7", "N10", "No"), 
        ("N8", "A4", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A5", "Yes"),
        ("N9", "A6", "No"),
        ("N10", "A7", "Yes"),
        ("N10", "A8", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Lack_Of_Bladder_Control_In_Older_People_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your urine cloudy, or does it smell unusually strong."
    flowchart['A1'] = "See a doctor immediately. You may have a urinary tract infection. If you are a woman, you may have chronic urethritis."
    flowchart['N2'] = "Have you been constipated for more than a week?"
    flowchart['A2'] = "See a doctor immediately. Your urinary incontinence may result from pressure on the bladder."
    flowchart['N3'] = "Are you currently taking any prescription medication?"
    flowchart['A3'] = "Talk to your doctor. Some drugs may cause you to leak urine."
    flowchart['N4'] = "Are you a woman?"
    flowchart['N5'] = "Do you leak small amounts of urine when you cough, sneeze, laugh, or run?"
    flowchart['A4'] = "Talk to your doctor. You probably have stress incontinence."
    flowchart['N6'] = "Does your genital area itch?"
    flowchart['A5'] = "Talk to your doctor. Genital irritation caused by a vaginal yeast infection, as a result of lack of estrogen during menopause, or from dermatitis, can make it difficult to control your bladder."
    flowchart['N7'] = "Do you dribble a little urine after you have finished urinating?"
    flowchart['A6'] = "See your doctor. You may have a disorder of the prostate gland."
    flowchart['N8'] = "Do you get to the bathroom in time once you feel the urge to urinate?"
    flowchart['A7'] = "See your doctor. If you are a woman, you may have an irritable bladder."
    flowchart['N9'] = "Have you noticed two or more of the following symptoms: change in personality; decline in personal appearance or cleanliness; impaired ability to remember recent events?"
    flowchart['A8'] = "See your doctor. These symptoms may indicate the onset of alzheimer's disease."
    flowchart['A9'] = "See your doctor if you are unable to make a decision from self-triage."

    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"), 
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N7", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "N8", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A8", "Yes"),
        ("N9", "A9", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Painful_Leg_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did the muscles in your leg suddenly tighten painfully for a few minutes and then return to normal?"
    flowchart['F1'] = "Cramp Flowchart" # change tp cramp flowchart
    flowchart['N2'] = "Did the pain immediately follow a fall or other injury?"
    flowchart['N3'] = "Can you walk on the affected leg?"
    flowchart['A1'] = "See your doctor. You may have pulled a muscle, ligament, or tendon."
    flowchart['A2'] = "See a doctor immediately. You may have broken your leg or severely torn a muscle or tendon."
    flowchart['N4'] = "Does the pain shoot down the back of your leg, especially when you cough or strain?"
    flowchart['A3'] = "See your doctor. You probably have sciatica (pressure on the sciatic nerve) caused by a prolapsed disk."
    flowchart['N5'] = "Do you have persistent pain in one area of your leg?"
    flowchart['N6'] = "Is your temperature 100°F or higher, or do you have chills and feel generally ill?"
    flowchart['A4'] = "See a doctor immediately. You may have osteomyelitis, a bone infection that is most common in children."
    flowchart['N7'] = "Do both of your legs ache and do your ankles swell sometimes, particularly after you stand for long periods?"
    flowchart['N8'] = "Are the veins in your legs twisted, swollen, and unusually prominent?"
    flowchart['A5'] = "See your doctor. You probably have varicose veins."
    flowchart['N9'] = "Is your hip painful or stiff on the same side as the affected leg?" 
    flowchart['A6'] = "See your doctor. You may have osteoarthritis."
    flowchart['N10'] = "Is the pain mainly in your calf?"
    flowchart['N11'] = "Is your calf swollen, and does it hurt when you walk?"
    flowchart['A7'] = "See a doctor immediately. You may have a blood clot in your leg."
    flowchart['N12'] = "Is just one of your veins red and inflamed?"
    flowchart['A8'] = "See a doctor immediately. You may have thrombophlebitis."
    flowchart['N13'] = "Does your leg hurt when you walk but not when you are resting?"
    flowchart['A9'] = "See your doctor. Pain in the calf during exercise that disappears promptly when you stop may be a sign of a circulatory problem such as atherosclerosis. It could also be a pulled muscle, ligament, or tendon."
    flowchart['N14'] = "Did your leg become painful following unusually strenuous exercise?"
    flowchart['A10'] = "See your doctor. You may have pulled a muscle, ligament, or tendon."
    flowchart['A11'] = "See your doctor if you are unable to make a decision from self-triage and the pain persists for more than 48 hours or gets worse."



    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N3", "A1", "Yes"),
        ("N3", "A2", "No"),
        ("N2", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "N6", "Yes"),
        ("N5", "N7", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "N8", "Yes"),
        ("N7", "N9", "No"),
        ("N8", "A5", "Yes"),
        ("N8", "N9", "No"), 
        ("N9", "A6", "Yes"), 
        ("N9", "N10", "No"),
        ("N10", "N11", "Yes"),
        ("N10", "N14", "No"),
        ("N11", "A7", "Yes"),
        ("N11", "N12", "No"),
        ("N12", "A8", "Yes"),
        ("N12", "N13", "No"),
        ("N13", "A9", "Yes"),
        ("N13", "N14", "No"),
        ("N14", "A10", "Yes"),
        ("N14", "A11", "No") 
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Noises_In_The_Ear_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have any hearing loss?"
    flowchart['F1'] = "Hearing Loss Flowchart" # change to hearing loss flowchart
    flowchart['N2'] = "Did you begin hearing the noises during or after an airplane flight?"
    flowchart['A1'] = "See your doctor. Changes in air pressure inside the plane may have damaged your middle ear."
    flowchart['N3'] = "Are you taking or have you recently taken any prescription or over-the-counter medications?"
    flowchart['A2'] = "Talk to your doctor. Noises in the ear are a common side effect of some drugs, including aspirin."
    flowchart['N4'] = "Do you have a tickling sensation in your ear?"
    flowchart['A3'] = "See your doctor. An insect may be trapped in your outer ear canal."
    flowchart['A4'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "A4", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Painful_Periods_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have a vaginal discharge between periods that is unusually heavy or that has an unpleasant odor, or is your temperature 100°F or higher?"
    flowchart['A1'] = "See your doctor. You may have an infection of the uterus, fallopian tubes, ovaries, or surrounding tissues."
    flowchart['N2'] = "Does the pain get worse as your period continues?"
    flowchart['A2'] = "See your doctor. You may have endometriosis."
    flowchart['N3'] = "Have you started menstruating within the past 3 months?"
    flowchart['A3'] = "Talk to your doctor. The pain is unlikely to be caused by an underlying disorder."
    flowchart['N4'] = "Have you had painful periods for most of your adult life, and is the pain the same as usual?"
    flowchart['N5'] = "Have your periods become more painful since you had an intrauterine device (IUD) inserted?"
    flowchart['A4'] = "See your doctor. An increase in menstrual pain is sometimes associated with insertion of an IUD."
    flowchart['N6'] = "Have you recently stopped taking oral contraceptives?"
    flowchart['A5'] = "Talk to your doctor. Oral contraceptives often reduce menstrual pain, so some women notice an increase in menstrual pain when they stop taking them."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."

    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G



def Abnormally_Frequent_Urination_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is urination painful?"
    flowchart['F1'] = "Painful Urination Flowchart" # change to painful urination flowchart
    flowchart['N2'] = "Do you seem to be urinating more than usual, or do you have to get up at night to urinate?"
    flowchart['N3'] = "Have you noticed two or more of the following symptoms: increased thirst; weight loss; unexplained tiredness; blurred vision?"
    flowchart['A1'] = "See a doctor immediately. Any of these symptoms can result from diabetes."
    flowchart['N4'] = "Have you been drinking more beverages that contain caffeine (such as coffee or colas) or more alcohol than usual?"
    flowchart['A2'] = "Caffeine and alcohol act as diuretics and increase urine production. Reduce your intake of these substances and you should urinate less frequently."
    flowchart['N5'] = "Are you currently taking medication for heart disease or high blood pressure?"
    flowchart['A3'] = "Talk to your doctor. Many medications prescribed for treating these conditions increase urine output."
    flowchart['N6'] = "Are you nervous or excited?"
    flowchart['A4'] = "Excitement can trigger urination." 
    flowchart['N7'] = "Are you a woman?"
    flowchart['N8'] = "Could you be pregnant?"
    flowchart['A5'] = "Increased frequency of urination is common throughout pregnancy, especially during the first 3 months and the last 3 months."
    
    flowchart['N9'] = "Are you a man over 50?" 
    flowchart['N10'] = "Do you have two or more of the following symptoms: waking up at night to urinate; difficulty starting to urinate; weak stream of urine; dribbling urine after urination?"
    flowchart['A6'] = "See your doctor. You may have an enlarged prostate gland."
    flowchart['N11'] = "Do you sometimes have a strong urge to urinate followed by an uncontrollable leaking of urine?"
    flowchart['A7'] = "See your doctor. You could have urge incontinence or a bladder tumor."
    flowchart['N12'] = "Do you have difficulty controlling your bladder?"
    flowchart['F2'] = "Lack Of Bladder Control Flowchart" # change to lack of bladder control flowchart
    flowchart['A8'] = "See your doctor if you are unable to make a decision from self-triage and the urge to urinate wakes you at night or continues for more than 1 week."


    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N3", "A1", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N2", "N6", "No"),
        ("N6", "A4", "Yes"), 
        ("N6", "N7", "No"), 
        ("N7", "N8", "Yes"),   
        ("N7", "N9", "No"),
        ("N8", "N11", "No"),
        ("N8", "A5", "Yes"),
        ("N9", "N10", "Yes"),
        ("N9", "N12", "No"),
        ("N10", "A6", "Yes"), 
        ("N10", "N12", "No"), 
        ("N11", "A7", "Yes"), 
        ("N11", "N12", "No"),  
        ("N12", "F2", "Yes"), 
        ("N12", "A8", "No")  
    ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G




def Bad_Breath_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Are your gums swollen, and do they bleed easily when you brush or floss your teeth?"
    flowchart['A1'] = "See your dentist. Bad breath often results from gingivitis (inflammation of the gums)."
    flowchart['N2'] = "Is your tongue or the inside of your mouth sore?"
    flowchart['A2'] = "See your dentist. An infection or sore in the mouth or on the tongue can cause bad breath."
    flowchart['N3'] = "Has it been more than 6 months since your last dental checkup, or do you have a toothache?"
    flowchart['A3'] = "See your dentist. Tooth decay may be causing your bad breath."
    flowchart['N4'] = "Do you brush and floss your teeth less often than twice a day?"
    flowchart['A4'] = "Decaying food particles stuck on and between your teeth and can make your breath smell and affect the condition of your teeth and gums."
    flowchart['N5'] = "Do you wear dentures?"
    flowchart['N6'] = "Do you sometimes forget to remove your dentures at night or to clean them thoroughly?"
    flowchart['A5'] = "Decaying food particles may be stuck to your dentures, causing bad breath."

    flowchart['N7'] = "Have you had garlic, onions, or other strong-smelling foods, or alcohol within the past 24 hours?"
    flowchart['A6'] = "Some foods and beverages contain strong-smelling substances that are absorbed into the bloodstream and released into the lungs, where they are exhaled, causing temporary bad breath. Your breath should return to normal within 24 hours of consuming these substances."
    flowchart['N8'] = "Do you smoke?"
    flowchart['A7'] = "Smoking causes bad breath, and inflammation caused by the smoke increases the risk of nasal and sinus infections."
    flowchart['N9'] = "Is your temperature 100°F or higher, or do you have frequent sore throats?"
    flowchart['A8'] = "See your doctor. Bad breath sometimes occurs with a fever. Some people have tiny pockets in their tonsils that trap bacteria, resulting in chronic tonsillitis."
    flowchart['N10'] = "Do you have a persistent cough that produces foul-smelling mucus?"
    flowchart['A9'] = "See your doctor. You may have bronchiectasis."
    flowchart['N11'] = "Do you breathe through your mouth?"
    flowchart['A10'] = "Talk to your doctor or dentist. Constantly breathing through the mouth dries up saliva, which creates an environment in which bacteria that cause bad breath can multiply."
    flowchart['A11'] = "See your doctor or dentist if your bad breath persists."
    

    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "N6", "Yes"),
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N5", "N7", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A8", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A9", "Yes"),
        ("N10", "N11", "No"),  
        ("N11", "A10", "Yes"),
        ("N11", "A11", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G



def Swollen_Abdomen_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did the swelling develop suddenly within the past 24 hours?"
    flowchart['N2'] = "Do you have severe abdominal pain?"
    flowchart['N3'] = "Do you have one or more of the following symptoms: vomiting; diarrhea; temperature over 100°F; no bowel movements for the past few days?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have a dangerous abdominal condition such as an intestinal obstruction."
    flowchart['F1'] = "Abdominal Pain Flowchart" # change to abdominal pain flowchart
    flowchart['N4'] = "Are your ankles puffy, or do dents form when you press your ankles with your fingers?"
    flowchart['N5'] = "Are you short of breath, particularly at night?"
    flowchart['A2'] = "See a doctor immediately. You may have fluid retention resulting from congestive heart failure."
    flowchart['N6'] = "Are you urinating less than usual?"
    flowchart['A3'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have acute kidney failure or a chronic kidney disease such as glomerulonephritis."
    flowchart['N7'] = "Do the whites of your eyes and your skin look yellow?"
    flowchart['A4'] = "See your doctor. Yellowish skin or eyes, called jaundice, suggests a liver disorder such as cirrhosis of the liver."
    flowchart['N8'] = "Are you a woman of childbearing age?"
    flowchart['N9'] = "Could you be pregnant?"
    flowchart['A5'] = "See your doctor. He or she will determine if you are pregnant."
    flowchart['N10'] = "Did the swelling develop just before or during your period?"
    flowchart['A6'] = "Many women have a swollen abdomen around the time of their period."
    flowchart['N11'] = "Do you have persistent constipation?"
    flowchart['A7'] = "Constipation sometimes causes swelling in the abdomen."
    flowchart['N12'] = "Are you overweight according to the body mass index?"
    flowchart['A8'] = "Talk to your doctor about losing weight."
    flowchart['A9'] = "See your doctor if you are unable to make a decision from self-triage and your abdomen stays swollen for more than 24 hours."
    

    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N4", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "N4", "No"),
        ("N3", "A1", "Yes"),
        ("N3", "F1", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N7", "No"),
        ("N5", "A2", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A3", "Yes"),
        ("N6", "N7", "No"),  
        ("N7", "A4", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "N9", "Yes"),
        ("N8", "N11", "No"),
        ("N9", "A5", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A6", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A7", "Yes"),
        ("N11", "N12", "No"),
        ("N12", "A8", "Yes"),
        ("N12", "A9", "No")

    ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Dizziness_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you feel as though the room is spinning around you?"
    flowchart['F1'] = "Feeling Faint And Fainting Flowchart" # change to feeling faint and fainting flowchart
    flowchart['N2'] = "Have you noticed one or more of the following symptoms: weakness in your arms or legs; numbness or tingling in any part of your body; blurred vision; difficulty speaking?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have had a stroke or a transient ischemic attack."
    flowchart['N3'] = "Do you have any hearing loss, or do you hear noises in your ear when there is no external source of noise?"
    flowchart['A2'] = "See your doctor. You could have an inner ear disorder such as labyrinthitis or Meniere's disease."
    flowchart['N4'] = "Are you over 50?"
    flowchart['N5'] = "Does raising your head bring on dizziness?"
    flowchart['A3'] = "See your doctor. This symptom can occur in a disorder involving the nerves and bones in the neck called cervical osteoarthritis. See your eye doctor if you wear bifocals; they may be improperly fitted."
    flowchart['N6'] = "Do you have recurring severe headaches in the mornings, accompanied by nausea or vomiting?"
    flowchart['N7'] = "Did you injure your head recently?"
    flowchart['A4'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have a subdural hemorrhage and hematoma."
    flowchart['A5'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have increased fluid pressure inside your brain, which is life-threatening. However, you may be having migraine headaches."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."
    

    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "F1", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N4", "N6", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "N7", "Yes"),
        ("N7", "A4", "Yes"),
        ("N7", "A5", "No"),
        ("N6", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Unexplained_Weight_Loss_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your appetite the same as usual?"
    flowchart['N2'] = "Have you been getting more exercise than usual?"
    flowchart['A1'] = "See your doctor if you continue to lose weight quickly or for no apparent reason. If you feel healthy and have no other symptoms, you are probably losing weight because you are burning more calories than you are consuming."
    flowchart['N3'] = "Do you have one or more of the following symptoms: unusually frequent urination; increased thirst; unexplained fatigue; itching around the genitals; blurred vision?"
    flowchart['A2'] = "See a doctor immediately. You may have diabetes."  
    flowchart['N4'] = "Do you have two or more of the following symptoms: excessive sweating; weakness or trembling; unexplained fatigue; bulging eyes?"
    flowchart['A3'] = "See your doctor. You may have an overactive thyroid gland."
    flowchart['A4'] = "See your doctor. If you feel healthy, your weight loss is probably normal. However, there is a slight possibility that you have an infection or cancer."
    flowchart['N5'] = "Do you have diarrhea?"
    flowchart['N6'] = "Is your stool pale, bulky, floating, and greasy?"
    flowchart['A5'] = "See your doctor. You may have a disorder that blocks your body's ability to absorb nutrients, such as celiac disease, inflammatory bowel disease, or lactose intolerance."
    flowchart['N7'] = "Have your bowel habits changed, or is there blood in your stools?"
    flowchart['A6'] = "See a doctor immediately. You may have inflammatory bowel disease or colon cancer."
    flowchart['N8'] = "Have you been having recurring attacks of upper abdominal pain?"
    flowchart['A7'] = "See a doctor immediately. You may have a peptic ulcer, gallstones, or cancer of the stomach."
    flowchart['N9'] = "Do you have two or more of the following symptoms: sweating at night; recurring fever; unexplained fatigue; feeling generally ill; persistent cough; coughing up blood-tinged mucus?"
    flowchart['A8'] = "See a doctor immediately. You may have a serious chronic infection, such as tuberculosis or HIV. Or you could have a type of cancer such as hodgkin's disease."
    flowchart['A9'] = "See your doctor if you are unable to make a decision from self-triage."






    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),  
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "A4", "No"),
        ("N1", "N5", "No"),
        ("N5", "N6", "Yes"),
        ("N6", "A5", "Yes"),
        ("N5", "N7", "No"),
        ("N6", "A6", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A8", "Yes"),
        ("N9", "A9", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Backache_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did the pain start suddenly?"
    flowchart['N2'] = "Have you noticed one or more of the following symptoms: loss of bladder or bowel control; difficulty moving a limb; numbness or tingling in a limb?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have damaged your spinal cord."
    flowchart['A2'] = "See your doctor if the pain is severe or lasts more than 3 days. Your backache is probably caused by bruising or a muscle spasm."
    flowchart['N3'] = "Did the pain follow a fall or other injury to your back?"
    flowchart['N4'] = "Have you lifted something heavy recently, exercised strenuously, or otherwise strained your back?"
    flowchart['N5'] = "Does the pain shoot down the back of your leg?"
    flowchart['A3'] = "See your doctor. You probably have sciatica (pressure on the sciatic nerve) caused by a prolapsed disk."
    flowchart['N6'] = "Is the pain mainly in the small of your back?"
    flowchart['A4'] = "You probably have low back pain from strain. Or you could have osteoarthritis."
    flowchart['N7'] = "Are you a woman over age 60 and have you recently spent several weeks in bed or in a wheelchair?"
    flowchart['N8'] = "Do you have a sharp pain in one area of your spine?"
    flowchart['N9'] = "Is your temperature 100°F or higher?"
    flowchart['N10'] = "Is the pain mainly in the lower part of your back?"
    flowchart['N11'] = "Does the pain shoot down the back of your leg?"
    flowchart['N12'] = "Are you more than 4 months pregnant?"
    flowchart['A5'] = "See a doctor immediately. You may have a crushed vertebra (compression fracture) as a result of osteoporosis."
    flowchart['A6'] = "See your doctor if the pain lasts more than 3 days. You probably strained some back muscles."
    flowchart['A7'] = "See a doctor immediately. You may have a serious kidney infection such as acute pyelonephritis or you may have an epidural abscess."
    flowchart['A8'] = "You probably have sciatica (pressure on the sciatic nerve) caused by a prolapsed disk."
    flowchart['A9'] = "Lower backache is common during pregnancy."
    flowchart['N13'] = "Are you overweight according to the body mass index?"
    flowchart['N14'] = "Are you over age 50, and is the pain worse after a period of inactivity (such as after getting up in the morning)?"
    flowchart['N15'] = "Do you have pain in other joints, including the hip, knee, or ankle?"
    flowchart['N16'] = "Could your back be strained by your working conditions (such as sitting in a chair the wrong height for your desk or hunching over while looking at your computer screen)?"
    flowchart['A10'] = "Carrying too much weight can strain your back muscles. Losing weight will ease some of the strain on your back."
    flowchart['A11'] = "You may have osteoarthritis, or you may be doing something that hurts your back."
    flowchart['A12'] = "Backache often results from such strain and poor posture."
    flowchart['A13'] = "See your doctor if you are unable to make a decision from self-triage."





    edges_with_conditions = [
        ("N1", "N3", "Yes"),
        ("N2", "A1", "Yes"),
        ("N2", "A2", "No"),
        ("N1", "N9", "No"),
        ("N3", "N2", "Yes"),
        ("N3", "N4", "No"),  
        ("N4", "N5", "Yes"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N4", "N7", "No"), 
        ("N6", "A4", "Yes"),
        ("N6", "N7", "No"), 
        ("N7", "N8", "Yes"),
        ("N7", "A6", "No"),
        ("N8", "A5", "Yes"),
        ("N8", "A6", "No"),
        ("N9", "A7", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "N14", "No"),
        ("N10", "N11", "Yes"),
        ("N11", "N12", "No"),
        ("N11", "A8", "Yes"),
        ("N12", "A9", "Yes"),
        ("N12", "N13", "No"),
        ("N13", "A10", "Yes"),
        ("N13", "N14", "No"),
        ("N14", "N15", "Yes"),
        ("N15", "A11", "Yes"),
        ("N15", "N16", "No"),
        ("N14", "N16","No"),
        ("N16", "A12", "Yes"),
        ("N16", "A13", "No")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    

    return flowchart, G




def Fever_In_Children_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does your child have a rash?"
    flowchart['N2'] = "Does your child have abdominal pain?"
    flowchart['F1'] = "Rash With Fever Flowchart"  # change to rash with fever flowchart
    flowchart['F2'] = "Abdominal Pain In Children Flowchart" # change to abdominal pain in children flowchart
    flowchart['N3'] = "Does your child have an earache?"
    flowchart['A1'] = "Call your child's doctor. Your child may have an ear infection."
    flowchart['N4'] = "Has your child had three or four watery bowel movements within 24 hours?"
    flowchart['A2'] = "Call your child's doctor immediately. Your child has diarrhea, possibly caused by an infection of the digestive tract such as gastroenteritis."
    flowchart['N5'] = "Is your child coughing?"
    flowchart['N6'] = "Is your child's breathing very rapid or noisy, or is he or she gasping for air?"
    flowchart['A3'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or take your child to the nearest hospital emergency department. Your child may have a serious lung infection such as acute bronchitis or pneumonia."
    flowchart['A4'] = "Call your child's doctor. Your child may have a cold, influenza, or some other infectious disease."
    flowchart['N7'] = "Does your child have a sore throat, or is his or her voice faint or hoarse?"
    flowchart['A5'] = "Call your child's doctor. Your child may have an infection of the upper respiratory tract such as tonsillitis, pharyngitis, or laryngitis."
    flowchart['N8'] = "Does your child have a runny nose?"
    flowchart['A6'] = "Call your child's doctor. Your child may have a cold, influenza, or some other infectious disease."
    flowchart['N9'] = "Is the area between your child's ear and the angle of his or her jaw swollen, painful, or tender?"
    flowchart['A7'] = "Take your child to the doctor. Your child may have mumps."
    flowchart['N10'] = "Does your child seem ill, and does he or she have two or more of the following symptoms: vomiting; headache; sensitivity of the eyes to bright light; stiff neck, or pain when trying to bend the head forward?"
    flowchart['A8'] = "Take your child to the doctor immediately. Your child may have meningitis."
    flowchart['A9'] = "Call your child's doctor if you are unable to make a decision from self-triage, if your child's temperature remains high for more than 6 hours, or if his or her temperature is over 102°F."
    

    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "F2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A1", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "N6", "Yes"),
        ("N5", "N7", "No"),
        ("N6", "A3", "Yes"),
        ("N6", "A4", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A6", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A7", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A8", "Yes"),
        ("N10", "A9", "No") 
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Painful_Urination_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have pain in your side (toward the back and just above the waist), along with fever and chills?"
    flowchart['A1'] = "See your doctor. You may have a kidney infection."
    flowchart['N2'] = "Are you a man?"
    flowchart['N3'] = "Do you have a discharge from your penis?"
    flowchart['A2'] = "See your doctor. You may have a sexually transmitted disease such as chlamydia, nongonococcal urethritis, or gonorrhea."
    flowchart['N4'] = "Do you have a dull, heavy ache in your groin, or is your temperature 100°F or higher?"
    flowchart['A3'] = "See your doctor. You may have an infection of the prostate gland."
    flowchart['N5'] = "Do you have a greenish yellow or white discharge from your vagina or itching around the genital area?"
    flowchart['A4'] = "See your doctor. You may have a vaginal yeast infection or trichomoniasis."
    flowchart['N6'] = "Are you urinating more frequently than usual?"
    flowchart['A5'] = "See your doctor. You may have inflammation of the bladder."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "N5", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N6", "No"),  
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),  
        ("N6", "A5", "Yes"),
        ("N6", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

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
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G



def Itching_In_Children_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does your child have spots, blisters, or discolored areas on any part of his or her body?"
    flowchart['F1'] = "Itchy Spots And Rashes Flowchart"  # change to itchy spots and rashes flowchart
    flowchart['N2'] = "Is the itching only around the anus or genitals?"
    flowchart['A1'] = "Take your child to the doctor. Inadequate washing or rinsing of the genital area may be causing the itching, or your child may have pinworms. In girls, vulvovaginitis may be the problem."
    flowchart['N3'] = "Is the itching confined to your child's head?"
    flowchart['N4'] = "Do you see tiny white spots clinging to your child's hair that cannot easily be rubbed off?"
    flowchart['A2'] = "Call your child's doctor. Your child may have lice."
    flowchart['N5'] = "Does your child have small bald patches on his or her scalp?"
    flowchart['A3'] = "Take your child to the doctor. Your child may have a fungal infection called ringworm."
    flowchart['N6'] = "Is the itching mainly in an area covered by clothing?"
    flowchart['A4'] = "Take your child to the doctor. Your child may have dermatitis caused by an allergic reaction from contact with a substance such as wool clothing, laundry detergent, or fabric softener."
    flowchart['A5'] = "Take your child to the doctor if you are unable to make a decision from self-triage."
    

    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "N4", "Yes"),
        ("N3", "N6", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "A5", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

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
    G.add_nodes_from(flowchart.keys())

    # Add edges to the graph
    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G



def Swollen_Ankles_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have pain in one or both ankles?"
    flowchart['F1'] = "Painful Ankles Flowchart" # change to painful ankles flowchart
    flowchart['N2'] = "Is only one ankle swollen?"
    flowchart['N3'] = "Is the calf of the same leg swollen, or do you feel pain in the calf when you walk?"
    flowchart['A1'] = "See a doctor immediately. You may have a blood clot in a vein."
    flowchart['N4'] = "Have you injured your ankle within the past 6 months?"
    flowchart['A2'] = "See your doctor if the ankle becomes painful. Your ankle is likely to swell occasionally for several months after an injury."
    flowchart['A3'] = "See your doctor to determine what is causing the swelling."
    flowchart['N5'] = "Are both ankles swollen?"
    flowchart['N6'] = "Are you becoming progressively short of breath?"
    flowchart['A4'] = "See your doctor. You may have congestive heart failure."
    flowchart['N7'] = "Are your ankles hot, red, and stiff?"
    flowchart['A5'] = "See your doctor. You may have rheumatoid arthritis."
    flowchart['N8'] = "Have you been standing or sitting for many hours?"
    flowchart['A6'] = "See your doctor if the swelling persists for more than 48 hours or if you feel sick. It is normal for your ankles to swell when you have been standing or sitting for long periods, especially if the room is uncomfortably warm or the weather is hot."
    flowchart['N9'] = "Is it possible that you could have kidney or liver disease?"
    flowchart['A7'] = "See a doctor immediately. If not treated and controlled, kidney or liver disease can cause swollen ankles."
    flowchart['N10'] = "Are you a woman?"
    flowchart['N11'] = "Could you be more than 3 months pregnant?"
    flowchart['A8'] = "See a doctor immediately. Although swollen ankles are common during pregnancy, they can be a sign of life-threatening high blood pressure later in pregnancy."
    flowchart['N12'] = "Are you taking oral contraceptives or a corticosteroid medication?"
    flowchart['A9'] = "Talk to your doctor. Swollen ankles can be a side effect of both oral contraceptives and corticosteroid medication."
    flowchart['N13'] = "Is your period due in a few days, and do you usually have swollen ankles just before your period?"
    flowchart['A10'] = "Having swollen ankles before a period is usually a sign of premenstrual syndrome."
    flowchart['A11'] = "See your doctor if you are unable to make a decision from self-triage and the swelling persists for more than 48 hours or you feel sick."


    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N3", "A1", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "A3", "No"),
        ("N2", "N5", "No"),
        ("N5", "N6", "Yes"),
        ("N5", "A11", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N8", "No"),  
        ("N8", "A6", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A7", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "N11", "Yes"),
        ("N10", "A11", "No"),
        ("N11", "A8", "Yes"),
        ("N11", "N12", "No"),
        ("N12", "A9", "Yes"),
        ("N12", "N13", "No"),
        ("N13", "A10", "Yes"),
        ("N13", "A11", "No")


    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Breast_Problems_In_New_Mothers_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Can you see or feel one or more lumps in your breast?"
    flowchart['A1'] = "See your doctor. You probably have a harmless cyst or tumor. However, you could have breast cancer."
    flowchart['N2'] = "Was your baby born within the past 4 days?"
    flowchart['N3'] = "Are both breasts swollen, hard, and tender?"
    flowchart['A2'] = "Call your doctor if you are concerned. Breasts often become painfully engorged with milk in the days after delivery."
    flowchart['N4'] = "Can you feel a hard, tender lump on one of your breasts?"
    flowchart['N5'] = "Is your temperature 100°F or higher, or is the breast painful, red, and throbbing?"
    flowchart['A3'] = "See a doctor immediately. You probably have a breast infection or abscess and need to start taking antibiotics as soon as possible."
    flowchart['A4'] = "See your doctor. You could have a blocked milk duct."
    flowchart['N6'] = "Are only your nipples sore?"
    flowchart['N7'] = "Do you have pain in your nipple when your baby starts to suck, and does the pain continue throughout the feeding?"
    flowchart['A5'] = "See your doctor. You may have a cracked nipple."
    flowchart['A6'] = "Talk to your doctor. Sore nipples are common in the first weeks of breastfeeding."
    flowchart['A7'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "N4", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"), 
        ("N4", "N6", "No"),  
        ("N5", "A3", "Yes"),
        ("N5", "A4", "No"),
        ("N6", "N7", "Yes"),
        ("N6", "A7", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Pain_In_The_Face_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you or did you recently have a red, blistering rash where you now feel pain?"
    flowchart['A1'] = "See your doctor. You may have shingles."
    flowchart['N2'] = "Do you have severe pain radiating from one bloodshot eye?"
    flowchart['A2'] = "See a doctor immediately. The pressure inside your eyeball may be increased, which can affect vision."
    flowchart['N3'] = "Is the pain between your eye and nose on one side of your face?"
    flowchart['N4'] = "Are your nose and the affected eye both runny?"
    flowchart['A3'] = "See your doctor. You may have a migraine or an infected or blocked lacrimal duct."
    flowchart['N5'] = "Do you have dull pain or tenderness around your eyes or cheekbones that worsens when you bend forward?"
    flowchart['A4'] = "See your doctor. You probably have a sinus infection, especially if you recently had a cold."
    flowchart['N6'] = "Do you have continuous, throbbing pain on one side of your face?"
    flowchart['N7'] = "Is the pain worse at night, when you eat, or when you touch a particular tooth?"
    flowchart['A5'] = "See a doctor or dentist immediately. You may have a tooth abscess."
    flowchart['N8'] = "Do you have severe, throbbing pain that comes on suddenly in one or both temples?"
    flowchart['N9'] = "Have you been feeling sick, or does your scalp hurt when you touch it?"
    flowchart['A6'] = "See a doctor immediately. You may have temporal arteritis (inflammation of the arteries in your head), which can affect your vision."
    flowchart['N10'] = "Do you have stabbing pain on one side of your face, brought on by any of the following: touching your face; chewing; breathing cold air; drinking cold liquid?"
    flowchart['A7'] = "See your doctor. The pain is probably caused by a damaged nerve."
    flowchart['A8'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "N4", "Yes"),
        ("N3", "N5", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),  
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"), 
        ("N6", "N7", "Yes"),
        ("N6", "N8", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N8", "No"), 
        ("N8", "N9", "Yes"),
        ("N8", "N10", "No"),
        ("N9", "A6", "Yes"),
        ("N9", "N10", "No"), 
        ("N10", "A7", "Yes"),
        ("N10", "A8", "No")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Diarrhea_In_Infants_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your baby content, alert, and feeding well?"
    flowchart['N2'] = "Is your baby bottle-fed?"
    flowchart['N3'] = "Have you added sugar to any formula, milk, or water?"
    flowchart['A1'] = "Sugar is difficult for babies to digest and is likely to be causing the diarrhea. Do not add sugar to your baby's diet."
    flowchart['N4'] = "Have you just started to add solids to your baby's diet?"
    flowchart['A2'] = "Talk to your child's doctor about when you should introduce solid foods into your baby's diet. Your baby may still be too young to digest solid food."
    flowchart['N5'] = "Are you giving your baby fruit juices?"
    flowchart['A3'] = "Your baby's digestive system has probably been upset by the sugar in the fruit juice. Don't give your baby juices until he or she is at least 6 months old."
    flowchart['N6'] = "Have you given your baby any nonprescription medication?"  
    flowchart['A4'] = "Call your child's doctor. Some medications can cause diarrhea. Never give a baby any medications, including alternative medicines such as herbal preparations, unless they are recommended by your doctor."
    flowchart['N7'] = "Is your child taking a medication prescribed for some other disorder?"
    flowchart['A5'] = "Call your child's doctor about the problem, but do not stop giving the medication to your baby. Some medications prescribed for children are difficult to digest and can cause diarrhea, often because they have a sugary, syrupy base."
    flowchart['N8'] = "Is your baby's temperature over 100°F, and is he or she vomiting?"
    flowchart['A6'] = "Take your child to the doctor immediately. Your baby may have an infection of the digestive tract such as gastroenteritis."
    flowchart['A7'] = "Take your child to the doctor immediately if the diarrhea persists or your baby seems ill and you are unable to make a decision from self-triage."



    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N7", "No"),  
        ("N2", "N3", "Yes"),
        ("N2", "N4", "No"),
        ("N3", "A1", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"), 
        ("N6", "A4", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A6", "Yes"),
        ("N8", "A7", "No") 
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Painful_Or_Enlarged_Testicles_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you suddenly developed a painful swelling in one or both testicles?"
    flowchart['N2'] = "Have you had an injury to the genital area within the past 48 hours?"
    flowchart['A1'] = "See a doctor immediately. Painful or swollen testicles after an injury may be a sign of tissue damage."
    flowchart['A2'] = "See a doctor immediately. Painful, enlarged testicles without an injury may be caused by a twisted spermatic cord. Or you could have an infection inside or just outside the testicle."
    flowchart['N3'] = "Do you have a painless swelling in your scrotum?"
    flowchart['A3'] = "See your doctor. The swelling may result from an inguinal hernia or from an accumulation of fluid such as from varicose veins around a testicle."
    flowchart['N4'] = "Is only one of your testicles enlarged?"
    flowchart['A4'] = "See a doctor immediately. You may have a harmless cyst. However, you could have cancer of the testicle."
    flowchart['A5'] = "See your doctor if you are unable to make a decision from self-triage."
   


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "A2", "No"),
        ("N2", "A1", "Yes"),
        ("N1", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "A5", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Heavy_Periods_Flowchart():
    flowchart = {}


    flowchart['N1'] = "Have your periods always been heavy?"
    flowchart['N2'] = "Have your periods become heavier in recent months?"
    flowchart['A1'] = "See your doctor. Your heavy periods are probably not a cause for concern, but you are at risk of iron deficiency anemia from heavy blood loss."
    flowchart['N3'] = "Did your periods become heavier after an intrauterine device (IUD) was inserted?"
    flowchart['A2'] = "Call your doctor. Heavier periods are a common side effect of IUDs."
    flowchart['N4'] = "Have your periods become more painful?"
    flowchart['N5'] = "Is the pain worse toward the end of a period?"
    flowchart['A3'] = "See your doctor. You may have a disorder of the pelvic organs such as endometriosis."
    flowchart['N7'] = "Do you have a vaginal discharge between periods that is unusually heavy or that has an unpleasant odor, or is your temperature 100°F or higher?"
    flowchart['A4'] = "See your doctor. You may have an infection of the uterus, fallopian tubes, ovaries, or surrounding tissues."
    flowchart['A5'] = "See your doctor. You may have a benign growth in the uterus."
    flowchart['N6'] = "Have you had only one heavy period that was a week or more late?"
    flowchart['A6'] = "See your doctor. A delayed period can be heavier than usual and is seldom a cause for concern. However, if there is a possibility that you were pregnant, you could have had an early miscarriage."
    flowchart['N8'] = "Have you recently started to have a few days of light bleeding at the beginning or end of a period?"
    flowchart['A7'] = "See your doctor. These symptoms are common as women approach menopause. However, they can also be symptoms of fibroids or polycystic ovarian syndrome."
    flowchart['N9'] = "Have you recently had a baby?"
    flowchart['A8'] = "Talk to your doctor. The first period after childbirth is often heavier than usual."
    flowchart['A9'] = "See your doctor if you are unable to make a decision from self-triage."  
    


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "A1", "No"),
        ("N2", "N3", "Yes"),
        ("N3", "N4", "No"),
        ("N1", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N4", "N5", "Yes"),
        ("N4", "N6", "No"), 
        ("N5", "N7", "No"), 
        ("N5", "A3", "Yes"),  
        ("N7", "A4", "Yes"),
        ("N7", "A5", "No"),
        ("N6", "A6", "Yes"),
        ("N6", "N8", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "N9", "No"), 
        ("N9", "A8", "Yes"),
        ("N9", "A9", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Sore_Throat_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your temperature 100°F or higher?"
    flowchart['N2'] = "Do you have two or more of the following symptoms: headache; cough; aching joints or bones?"
    flowchart['A1'] = "Talk to your doctor. You probably have a viral infection such as influenza."
    flowchart['N3'] = "Do you have swelling or tenderness in your neck?"
    flowchart['N4'] = "Is the swollen or tender area in front of your ear or at the angle of the jaw?"
    flowchart['A2'] = "See your doctor. You may have mumps."
    flowchart['A3'] = "See your doctor. You probably have strep throat, tonsillitis, or pharyngitis. If your symptoms persist for more than a week, you may have infectious mononucleosis."
    flowchart['N5'] = "Do you have a stuffy or runny nose, or have you been sneezing?"
    flowchart['A4'] = "You probably have a cold."
    flowchart['N6'] = "Do you smoke or drink a lot of alcohol, or were you in a smoky place (such as a bar) just before your throat got sore?"
    flowchart['A5'] = "Call your doctor. Smoking, inhaling secondhand smoke, and drinking alcohol can all cause throat inflammation."
    flowchart['N7'] = "Are you hoarse, or have you lost your voice?"
    flowchart['F1'] = "Hoarseness Or Loss Of Voice Flowchart" # change to hoarseness or loss of voice flowchart
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage and your sore throat persists for more than 2 days."
    
    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N1", "N3", "No"),
        ("N3", "N4", "Yes"),
        ("N4", "A2", "Yes"),
        ("N4", "A3", "No"),
        ("N3", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "F1", "Yes"),
        ("N7", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

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
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Waking_At_Night_In_Children_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your child's temperature over 100°F, or does he or she seem ill in any way?"
    flowchart['A1'] = "Call your child's doctor. An illness may be disturbing your child's sleep."
    flowchart['N2'] = "Is your child younger than 6 weeks?"
    flowchart['N3'] = "When your baby wakes, do you feed him or her?"
    flowchart['N4'] = "Does your baby go back to sleep after the feeding?"
    flowchart['A4'] = "Waking at night from hunger is normal at this age. Feed your baby whenever he or she is hungry, at least every few hours."
    flowchart['A2'] = "Your baby is too young to sleep through the night without at least one or two feedings."
    flowchart['A3'] = "Your baby may have developed an irregular sleep pattern, or the room may be too noisy, bright, warm, or cool. Establish a consistent sleep schedule and bedtime routine and keep the room dark and quiet and the temperature comfortable (68°F to 70°F) to help promote sleep."
    flowchart['N5'] = "Is your child younger than 6 months?"
    flowchart['N6'] = "When your baby wakes, do you feed him or her?"
    flowchart['N7'] = "Does your baby go back to sleep after the feeding?"
    flowchart['A6'] = "Babies this age often wake from hunger. Try feeding your baby just before you go to bed."
    flowchart['A5'] = "Try feeding your baby when he or she wakes. Your baby may be hungry and may sleep better if fed during the night."
    flowchart['N8'] = "Is your child younger than 1 year?"
    flowchart['N9'] = "Does your baby tend to kick off his or her covers during the night?"
    flowchart['A7'] = "Your baby may be waking up at night because he or she is cold. Putting your baby in warmer pajamas or a sleeping sack, or making the room warmer, may solve the problem."
    flowchart['N10'] = "Does your baby's bottom look red or have a rash?"
    flowchart['A8'] = "Call your child's doctor. Your baby probably has diaper rash, which stings and wakes the baby when he or she urinates."
    flowchart['N11'] = "Does your baby usually sleep through most of the night but wake early in the morning?"
    flowchart['A9'] = "Your baby may not need any more sleep. Changing your baby's diaper, giving him or her a drink of water, or putting a few toys in the crib may comfort and occupy your child enough to allow you to get more sleep."
    flowchart['N12'] = "Does your child seem upset or frightened when he or she wakes up?"
    flowchart['A10'] = "Your baby probably has developed an irregular sleeping pattern. Establish a consistent sleep schedule and bedtime routine."
    flowchart['A11'] = "Nightmares may be waking your child. Keep a dim light on in the room if your child seems to be afraid of the dark."
    flowchart['N13'] = "Does your child have any new experiences that may be a source of stress (such as the arrival of a new baby or starting school), or is there tension in the home?"
    flowchart['A12'] = "Anxiety may be making it difficult for your child to sleep. Extra reassurance and affection during the day and at bedtime may help solve the problem."
    flowchart['A13'] = "Call your child's doctor if you are worried about your child waking at night and you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "N2", "No"),
        ("N1", "A1", "Yes"),
        ("N2", "N3", "Yes"),
        ("N3", "A2", "No"),
        ("N2", "N5", "No"),
        ("N3", "N4", "Yes"),
        ("N4", "A3", "No"),
        ("N4", "A4", "Yes"),
        ("N5", "N6", "Yes"),
        ("N6", "A5", "No"),
        ("N6", "N7", "Yes"),
        ("N7", "A6", "Yes"),  
        ("N7", "N8", "No"),
        ("N5", "N8", "No"),
        ("N8", "N9", "Yes"),
        ("N9", "A7", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A8", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A9", "Yes"),
        ("N11", "A10", "No"),
        ("N8", "N12", "No"),
        ("N12", "A11", "Yes"),
        ("N12", "N13", "No"),
        ("N13", "A12", "Yes"),
        ("N13", "A13", "No")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Disturbed_Or_Impaired_Vision_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did you injure your head recently?"
    flowchart['A1'] = "See a doctor immediately. You may have bleeding inside your skull."
    flowchart['N2'] = "Did you suddenly lose some or all of the field of vision in one or both eyes?"
    flowchart['N3'] = "Do you have a headache?"
    flowchart['A2'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have had a stroke. However, you could be having a migraine."
    flowchart['A3'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. Even if the loss of vision was only temporary, you may have a serious eye disorder such as retinal artery occlusion."
    flowchart['N4'] = "Is your vision blurred?"
    flowchart['N5'] = "Is only one eye affected?"
    flowchart['N6'] = "Do you feel pain in the affected eye?"
    flowchart['A4'] = "See a doctor immediately. You could have acute glaucoma or optic neuritis."
    flowchart['A5'] = "See a doctor immediately. You may have a serious eye disorder such as uveitis."
    flowchart['N7'] = "Did your vision problem begin within the past 2 days, and do you feel pain in the affected eye?"
    flowchart['A6'] = "See a doctor immediately. You may have a detached retina."
    flowchart['N8'] = "Have you recently started taking any medication?"
    flowchart['A7'] = "See a doctor immediately. Some drugs can cause blurred vision."
    flowchart['N9'] = "Do you have diabetes?"
    flowchart['A8'] = "See a doctor immediately. Your blood sugar may not be under control."
    flowchart['N10'] = "Are you over 50?"
    flowchart['A9'] = "See a doctor immediately. You could be developing an eye disorder such as cataracts or macular degeneration."
    flowchart['N11'] = "Do you have double vision?"
    flowchart['N12'] = "Do your eyes seem to be bulging?"
    flowchart['A10'] = "See your doctor. You may have an eye disorder called exophthalmos."
    flowchart['A11'] = "See your doctor. You may have misaligned eyes."
    flowchart['N13'] = "Do you see flashing lights or floating spots?"
    flowchart['A12'] = "See a doctor immediately. These may be early symptoms of a detached retina."
    flowchart['A13'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N3", "A2", "Yes"),
        ("N3", "A3", "No"),
        ("N2", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N5", "N6", "Yes"),
        ("N6", "A4", "Yes"),
        ("N6", "A6", "No"),
        ("N5", "N7", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N8", "No"),  
        ("N4", "N11", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A8", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A9", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "N12", "Yes"),
        ("N12", "A10", "Yes"),
        ("N12", "A11", "No"),
        ("N11", "N13", "No"),
        ("N13", "A12", "Yes"),
        ("N13", "A13", "No")

    ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Absent_Periods_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you ever had a period?"
    flowchart['N2'] = "Could you be pregnant?"
    flowchart['A1'] = "See your doctor. If you want, you can take a home pregnancy test before your doctor's appointment to see if you are pregnant."
    flowchart['N3'] = "Have you recently had a baby?"
    flowchart['A3'] = "Periods seldom start until at least 6 to 8 weeks after childbirth, and later if you are breastfeeding. If you are breastfeeding, your periods will restart when you give your baby supplemental bottles regularly, introduce solid foods, or begin weaning your baby from breast milk."
    flowchart['A2'] = "See your doctor if you have never had a period but think that your periods should have started by now. The age at which a girl has her first period varies from family to family but usually is between ages 11 and 14."
    flowchart['N4'] = "Have you recently been ill or under stress?"
    flowchart['A4'] = "Change or stress can affect your periods."
    flowchart['N5'] = "Have you recently stopped taking oral contraceptives?"
    flowchart['A5'] = "Talk to your doctor. It can take several months for periods to begin again after oral contraceptives are stopped."
    flowchart['N6'] = "Have you been exercising strenuously, or have you lost a lot of weight in a short time?"
    flowchart['A6'] = "See your doctor. Sudden weight loss or very strenuous exercise can disrupt ovulation (the release of an egg from an ovary) and menstruation."
    flowchart['N7'] = "Are you over age 45?"
    flowchart['A7'] = "It is common for women over age 45 to begin having irregular periods."
    flowchart['N8'] = "Do you have two or more of the following symptoms: increased hairiness; deepening of the voice; unexplained weight gain?"
    flowchart['A8'] = "See your doctor. The lack of periods may be caused by disruption in the production of hormones."
    flowchart['N9'] = "Are you currently taking any medication?"
    flowchart['A9'] = "Talk to your doctor. Some drugs can cause periods to stop."
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage."



    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "A2", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A5", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A6", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A7", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A8", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A9", "Yes"),
        ("N9", "A10", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Hair_Loss_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Has your hair become generally thin?"
    flowchart['N2'] = "Did the thinning occur 2 to 3 months after a fever?"
    flowchart['A1'] = "Call your doctor if you are concerned about your hair loss. Temporary hair loss sometimes occurs a few months after a fever. Your hair should return to normal within a few months."
    flowchart['N3'] = "Are you currently taking any medication?"
    flowchart['A2'] = "Talk to your doctor. Some drugs can cause temporary hair loss."
    flowchart['N4'] = "Are you a woman?"
    flowchart['N5'] = "Did your hair become thin 2 to 3 months after childbirth?"
    flowchart['A3'] = "Talk to your doctor. Hormonal changes can affect hair growth."
    flowchart['N6'] = "Is your front hairline receding, or is the hair on the top of your head thinning?"
    flowchart['A4'] = "These are symptoms of male pattern baldness, which can occur in men of any age."
    flowchart['N7'] = "Did your hair loss occur slowly over several years?"
    flowchart['A5'] = "Mildly thinning hair, especially on the top of the head, is a normal part of aging."
    flowchart['N8'] = "Did one or more bald patches develop suddenly?"
    flowchart['A6'] = "See your doctor. In adults, this type of hair loss can result from a skin condition such as lichen planus or from a disease called alopecia areata. In children, it can result from a fungal infection such as ringworm."
    flowchart['N9'] = "Do you frequently use any of the following techniques on your hair: tight braiding or corn-rowing; straightening; curling iron or hot rollers; bleaching or dyeing; permanent?"
    flowchart['A7'] = "See your doctor if the thinning persists. All of these techniques can damage hair. Change to a more natural hairstyle and your hair should return to normal."
    flowchart['A8'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N1", "N8", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "N5", "Yes"),
        ("N5", "A3", "Yes"),
        ("N5", "N7", "No"), 
        ("N4", "N6", "No"),  
        ("N6", "A4", "Yes"),
        ("N6", "N9", "No"),
        ("N7", "A5", "Yes"),
        ("N7", "N9", "No"),
        ("N8", "A6", "Yes"),
        ("N8", "N9", "No"), 
        ("N9", "A7", "Yes"),
        ("N9", "A8", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Recurring_Abdominal_Pain_Flowchart():

    flowchart = {}
    
    flowchart['N1'] = "Is the pain in the upper part of your abdomen?"
    flowchart['N2'] = "Is it burning pain that worsens when you bend over?"
    flowchart['A1'] = "See your doctor. You may have gastroesophageal reflux disease."
    flowchart['N3'] = "Does the pain stop when you take an antacid?"
    flowchart['A2'] = "See your doctor. You may have indigestion or a peptic ulcer."
    flowchart['N4'] = "Does the pain occur in waves, and is it mainly in the upper right side of your abdomen or around your ribs?"
    flowchart['N5'] = "Is your temperature 100°F or higher?"
    flowchart['A3'] = "See your doctor. You may have an inflamed gallbladder or gallstones."
    flowchart['A4'] = "See your doctor. You may have indigestion or irritable bowel syndrome."
    flowchart['N6'] = "Have you lost your appetite, or have you lost a lot of weight (more than 10 pounds in 10 weeks) for no apparent reason?"
    flowchart['A5'] = "See a doctor immediately. You may have cancer of the stomach or colon cancer, especially if you are over age 40."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."
    flowchart['N7'] = "Is the pain mainly in the lower part of your abdomen?"
    flowchart['N8'] = "Do you have episodes of diarrhea?"
    flowchart['N9'] = "Do you feel sick, or is your temperature 100°F or higher?"
    flowchart['N10'] = "Do you have traces of blood and pus or mucus in your stool?"
    flowchart['A7'] = "See your doctor. You may have an inflammatory bowel disease such as Crohn's disease or ulcerative colitis."
    flowchart['A8'] = "See your doctor. You may have an inflammatory bowel disease such as Crohn's disease."
    flowchart['A9'] = "See a doctor immediately. You may have diverticular disease. There is also a slight possibility that you have colon cancer."
    flowchart['N11'] = "Are you a woman of childbearing age?"
    flowchart['F1'] = "Pelvic Pain In Women Flowchart" # change to pelvic pain in women flowchart
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [("N1", "N2", "Yes"),
                            ("N2", "A1", "Yes"),
                            ("N2", "N3", "No"),
                            ("N3", "A2", "Yes"),
                            ("N3", "N4", "No"),
                            ("N4", "N5", "Yes"),
                            ("N5", "A3", "Yes"),
                            ("N5", "A4", "No"),
                            ("N4", "N6", "No"),
                            ("N6", "A5", "Yes"),
                            ("N6", "A6", "No"),
                            ("N1", "N7", "No"),
                            ("N7", "N8", "Yes"),
                            ("N8", "N9", "Yes"),
                            ("N9", "N10", "Yes"),
                            ("N10", "A7", "Yes"),
                            ("N10", "A8", "No"),
                            ("N9", "A9", "No"),
                            ("N8", "N11", "No"),
                            ("N11", "F1", "Yes"),
                            ("N11", "A10", "No"),
                            ("N7", "A10", "No")
                            ]
    
    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G



def Hoarseness_Or_Loss_Of_Voice_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did the hoarseness begin within the past 3 days?"
    flowchart['N2'] = "Do you (or did you recently) have a cold, cough, or sore throat?"
    flowchart['A1'] = "You probably have inflammation of the vocal cords."
    flowchart['N3'] = "Were you talking more than usual just before the hoarseness developed or before you lost your voice?"
    flowchart['A2'] = "Talking too much can cause inflammation of the vocal cords."
    flowchart['N4'] = "Have you recently been feeling tense, nervous, or anxious?"
    flowchart['A3'] = "Anxiety can cause a sudden loss of voice."
    flowchart['N5'] = "Does your job require you to talk a lot—for example, are you a teacher or a lawyer?"
    flowchart['A4'] = "See your doctor. You may have persistent inflammation of the vocal cords or a growth on a vocal cord."
    flowchart['N6'] = "Have you been drinking a lot of alcohol?"
    flowchart['A5'] = "Excessive drinking can lead to inflammation of the vocal cords."
    flowchart['N7'] = "Do you smoke, or have you been in a smoky place (such as a bar)?"
    flowchart['A6'] = "See your doctor. Smoking can lead to inflammation of the vocal cords. However, it can also cause cancer."
    flowchart['N8'] = "Do you have two or more of the following symptoms: sensitivity to cold weather; dry skin or dry hair; unexplained weight gain; unexplained fatigue?"
    flowchart['A7'] = "See your doctor. You may have an underactive thyroid gland."
    flowchart['N9'] = "Has the hoarseness or loss of voice lasted longer than a week?"
    flowchart['N10'] = "Have you had several episodes of hoarseness or voice loss in the past 6 months?"
    flowchart['A8'] = "See a doctor immediately. You could have a polyp on a vocal cord or cancer of the larynx."
    flowchart['A9'] = "See your doctor if you are unable to make a decision from self-triage and your hoarseness persists for more than a week."

    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N1", "N5", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
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
        ("N10", "A8", "Yes"),
        ("N10", "A9", "No")
    ]

    # Create a directed graph
    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    # Add edges to the graph
    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Earache_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does the pain get worse when you pull down on your earlobe?"
    flowchart['A1'] = "See your doctor. You probably have an infection of the ear canal."
    flowchart['N2'] = "Do you have a blocked-up feeling in your ear that cannot be cleared by swallowing?"
    flowchart['N3'] = "Did the pain begin after an airplane flight?"
    flowchart['A2'] = "See a doctor immediately. Changes in air pressure may have damaged your middle ear."
    flowchart['N4'] = "Does the affected ear have a sticky yellow discharge?"
    flowchart['A3'] = "See your doctor. You could have an infection of the ear canal or an acute middle ear infection."
    flowchart['N5'] = "Do you have a cold?"
    flowchart['A4'] = "See your doctor if the pain is severe; you could have a middle ear infection. Earaches are a common symptom of colds that involve the upper respiratory tract, and usually subside when the cold clears up."
    flowchart['N6'] = "Do you also have pain in your teeth, jaw, or neck?"
    flowchart['A5'] = "See your doctor or dentist. Tooth and gum problems frequently cause pain in the ear. A strained or torn muscle in the neck can also cause pain in the ear."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."
    flowchart['N7'] = "Has your hearing worsened in the past few weeks or months?"
    flowchart['A7'] = "See your doctor. You could have an earwax blockage."
    flowchart['A8'] = "See your doctor. You could have an acute middle ear infection or a chronic middle ear infection."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "N4", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N7", "No"), 
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "A6", "No"),
        ("N7", "A7", "Yes"),
        ("N7", "A8", "No")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Skin_Problems_In_Young_Children_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your child younger than 3 months?"
    flowchart['A1'] = "Take your child to the doctor. Young babies should always be seen by a doctor if they have a medical problem."
    flowchart['N2'] = "Does your child have red spots or patches of red skin?"
    flowchart['N3'] = "Is your child's temperature over 100°F?"
    flowchart['F1'] = "Rash With Fever Flowchart" # change to rash with fever flowchart
    flowchart['N4'] = "Is the rash mainly on a skin area usually covered by a diaper?"
    flowchart['A2'] = "Your child probably has diaper rash."
    flowchart['N5'] = "Does your child have one or more flaky patches of itchy, inflamed skin?"
    flowchart['A3'] = "Take your child to the doctor. Your child may have a type of dermatitis called infantile eczema."
    flowchart['N7'] = "Is the rash red with raised, pimply blemishes?"
    flowchart['N8'] = "Has your child been in a warm room, or is the weather very hot?"
    flowchart['A4'] = "Your child may have a heat-related rash called prickly heat, especially if the rash is in a skin area that has been covered by tight or heavy clothing. Move your baby to a cool place and loosen or remove any tight or excess clothing. Apply cool washcloths and let the affected area air-dry. Don't apply any ointments or lotions, which can trap moisture under the skin and make the rash worse. Only apply a calamine or corticosteroid cream if the doctor has prescribed one. Take your child to the doctor if the rash gets worse or if your child develops a fever, seems ill, or is very uncomfortable."
    flowchart['N9'] = "Does your child have a rash of dark red spots that do not disappear when you press on them?"
    flowchart['A5'] = "Take the child to the doctor immediately. Your child may be having a serious allergic reaction."
    flowchart['N6'] = "Does your child have any greasy, crusty patches on the scalp?"
    flowchart['A6'] = "Your child probably has cradle cap."
    flowchart['A7'] = "Take your child to the doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "N6", "No"),
        ("N3", "F1", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N7", "No"),  
        ("N7", "N8", "Yes"),
        ("N8", "A4", "Yes"), 
        ("N7", "N9", "No"),
        ("N9", "A7", "No"), 
        ("N8", "A7", "No"),
        ("N6", "A6", "Yes"),
        ("N6", "N7", "No"),
        ("N9", "A5", "Yes")

    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Difficulty_Speaking_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you had one or more of the following symptoms: dizziness; headache; weakness in your arms or legs; numbness or tingling in any part of your body; blurred vision; difficulty swallowing?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have had a stroke or a transient ischemic attack."
    flowchart['N2'] = "Do you think that you are pronouncing words correctly but what you say does not seem to make sense to others?"
    flowchart['N3'] = "Do you have two or more of the following symptoms: decreased ability to deal with everyday activities such as cooking, driving, paying bills, and balancing a checkbook; decline in personal appearance or cleanliness; difficulty following complex conversations and instructions?"
    flowchart['A2'] = "See your doctor. You may have a mental disorder such as schizophrenia."
    flowchart['A3'] = "See your doctor. This combination of symptoms may indicate the onset of alzheimer's disease. In rare cases, these symptoms can result from a brain tumor or stroke."
    flowchart['N4'] = "Is it difficult to speak because of pain inside your mouth or in your tongue?"
    flowchart['F1'] = "Sore Mouth Or Tongue Flowchart" # change to sore mouth or tongue flowchart
    flowchart['N5'] = "Have you been drinking alcohol?"
    flowchart['A4'] = "Drinking can make you slur your speech."
    flowchart['N6'] = "Are you taking any medication?"
    flowchart['A5'] = "Talk to your doctor. Some drugs can affect speech."
    flowchart['N7'] = "Is it difficult to speak because you are unable to move the muscles on one side of your face?"
    flowchart['A6'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have had a stroke. However, you could have a less serious nerve disorder called bell's palsy."
    flowchart['N8'] = "Do people say you speak very softly, and does your speech lack normal variations in tone and pauses, making it sound expressionless?"
    flowchart['N9'] = "Do your hands tremble?"
    flowchart['A7'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have had a stroke. Or you could have a nervous system disorder such as parkinson's disease."
    flowchart['N10'] = "Are you sometimes unable to speak even though you know what you want to say, or do you sometimes get stuck at the beginning of a word and find yourself repeating the first consonant for several seconds before you can say the entire word?"
    flowchart['A8'] = "Talk to your doctor. This problem, called stuttering, often develops in early childhood and may recur during adulthood when a person is under stress."
    flowchart['A9'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "N4", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "A2", "No"),
        ("N4", "F1", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "N9", "Yes"),
        ("N8", "N10", "No"),
        ("N9", "A7", "Yes"),
        ("N9", "N10", "No"), 
        ("N10", "A8", "Yes"),
        ("N10", "A9", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Abnormal_Hair_Growth_In_Women_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Has the excess hair growth occurred in less than a few months?"
    flowchart['N2'] = "Do you have two or more of the following symptoms: unexplained weight gain; deepening voice; absence of periods?"
    flowchart['A1'] = "See your doctor. These symptoms suggest a hormonal disorder."
    flowchart['N4'] = "Did the excess hair appear after you began taking medication for a condition such as a threatened miscarriage, bleeding between periods, or epilepsy?"
    flowchart['A2'] = "Talk to your doctor. Some drugs can cause excess hair growth."
    flowchart['N3'] = "Did the excess hair growth occur before age 20?"
    flowchart['N5'] = "Do any female relatives also have heavy hair growth?"
    flowchart['A3'] = "A tendency to have heavy hair growth can run in families."
    flowchart['N6'] = "Are you over age 45?"
    flowchart['N7'] = "Is the excessive hair mainly on your face?"
    flowchart['A4'] = "An increase in facial hair is common as you get older."
    flowchart['A5'] = "Talk to your doctor if your hair growth concerns you."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N4", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "N3", "No"),
        ("N3", "N5", "Yes"),
        ("N3", "N6", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "N7", "Yes"),
        ("N6", "A5", "No"),
        ("N7", "A4", "Yes"),
        ("N7", "A5", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Depression_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did the depression follow a significant personal loss, such as a death in the family?"
    flowchart['A1'] = "See a doctor immediately. Although such feelings are normal, depression can be treated."
    flowchart['N2'] = "Did you recently recover from an infectious disease such as the flu, infectious mononucleosis, or hepatitis?"
    flowchart['A2'] = "See your doctor if the depression worsens or lasts longer than 2 weeks. Infectious diseases are sometimes followed by depression."
    flowchart['N3'] = "Did you recently have a baby?"
    flowchart['A3'] = "See a doctor immediately. Many women experience depression in the weeks after childbirth."
    flowchart['N4'] = "Do you regularly use alcohol or other drugs?"
    flowchart['A4'] = "Talk to your doctor. Abuse of alcohol or other drugs can cause depression or may be a symptom of depression."
    flowchart['N5'] = "Do you have two or more of the following symptoms: difficulty sleeping; difficulty getting out of bed; loss of appetite; lack of energy?"
    flowchart['A5'] = "See a doctor immediately. You may have depression."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."

    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A5", "Yes"),
        ("N5", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    

    return flowchart, G


def Painful_Intercourse_In_Men_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is the pain brought on by ejaculation?"
    flowchart['N2'] = "Do you have a burning sensation when you urinate or any unusual discharge from the penis?"
    flowchart['A1'] = "See your doctor. You may have an infection such as nongonococcal urethritis or prostatitis."
    flowchart['N3'] = "Do you have pain in your penis during intercourse?"
    flowchart['N4'] = "Do you have any redness, swelling, lumps, or sores on the skin or tip of your penis, or does your penis bend at an angle during an erection?"
    flowchart['A2'] = "See your doctor. You may have inflammation of the head or foreskin of the penis such as balanitis. If your penis bends to one side during an erection, you probably have peyronie's disease."
    flowchart['N5'] = "Does the tip of your penis become sore after intercourse?"
    flowchart['A3'] = "See your doctor. You may be allergic to a substance used by your partner (such as a spermicide or a douching solution) or you may be allergic to latex in condoms."
    flowchart['N6'] = "Is your partner tense or difficult to arouse sexually, or does she also have discomfort during intercourse?"
    flowchart['A4'] = "Your partner's vagina may be dry as a result of inadequate foreplay, tension, or anxiety. This can make intercourse painful for both of you."
    flowchart['A5'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [("N1", "N2", "Yes"),
                             ("N2", "A1", "Yes"),
                             ("N2", "N3", "No"),
                             ("N4", "A2", "Yes"),
                             ("N1", "N3", "No"),
                             ("N3", "N5", "No"),
                             ("N3", "N4", "Yes"),
                             ("N4", "N6", "No"),
                             ("N5", "A3", "Yes"),
                             ("N6", "A4", "Yes"),
                             ("N6", "A5", "No"),
                             ("N5", "A5", "No")
                             ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Fever_In_Young_Children_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your child 3 months old or younger?"
    flowchart['A1'] = "Take your child to the doctor. Young babies should always be seen by a doctor if they have a medical problem."
    flowchart['N2'] = "Does your child have a rash?"
    flowchart['F1'] = "Rash With Fever Flowchart" # change to rash with fever flowchart
    flowchart['N3'] = "Is your child crying as if in pain?"
    flowchart['A2'] = "Take your child to the doctor. Your child may have an ear infection, especially if he or she is batting at or pulling on an ear repeatedly."
    flowchart['N4'] = "Is your child's breathing noisy?"
    flowchart['A3'] = "Take your child to the doctor. Your child may have croup."
    flowchart['N5'] = "Is your child's breathing very rapid or noisy, or is he or she gasping for air?"
    flowchart['A4'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or take your child to the nearest hospital emergency department. He or she could have a serious lung infection such as acute bronchitis, bronchiolitis, or pneumonia."
    flowchart['N6'] = "Has your child had three to four watery bowel movements within 24 hours?"
    flowchart['A5'] = "Take your child to the doctor. Your child has diarrhea, possibly caused by an infection of the digestive tract such as gastroenteritis."
    flowchart['N7'] = "Does your child have a runny nose?"
    flowchart['A6'] = "Call your child's doctor. Your child may have a cold, influenza, or some other infectious disease."
    flowchart['N8'] = "Is the weather hot or the room warm, or is your child dressed in heavy clothing?"
    flowchart['A7'] = "Call your child's doctor if the fever doesn't go down after you have moved your child to a cool place, removed some of his or her clothing, and given him or her a drink of water. Your child may be overheated."
    flowchart['A8'] = "Call your child's doctor if you are unable to make a decision from self-triage, if your child's temperature remains high for more than 6 hours, or if his or her temperature is higher than 102°F."
    

    edges_with_conditions = [
                            ("N1", "A1", "Yes"),
                            ("N1", "N2", "No"),
                            ("N2", "F1", "Yes"),
                            ("N2", "N3", "No"),
                            ("N3", "A2", "Yes"),
                            ("N3", "N4", "No"),
                            ("N4", "A3", "Yes"),
                            ("N4", "N5", "No"),
                            ("N5", "A4", "Yes"),
                            ("N5", "N6", "No"), 
                            ("N6", "A5", "Yes"),
                            ("N6", "N7", "No"),
                            ("N7", "A6", "Yes"),
                            ("N7", "N8", "No"),
                            ("N8", "A7", "Yes"),
                            ("N8", "A8", "No") 
                           ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Painful_Or_Stiff_Neck_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did the pain start within the past 24 hours?"
    flowchart['N2'] = "Do you have one or more of the following symptoms: severe headache; nausea or vomiting; sensitivity of the eyes to bright light; drowsiness or confusion; fever?"
    flowchart['A1'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have meningitis. Or you may have bleeding in the brain."
    flowchart['N3'] = "Has your neck had a sudden jolt within the past day or two?"
    flowchart['A2'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have damaged your spinal cord."
    flowchart['N4'] = "Have you had a problem controlling an arm or leg since then?"
    flowchart['N5'] = "Is the pain severe, or do you have shooting pain in your shoulders or arms when you move your head?"
    flowchart['A3'] = "See your doctor. A disk in your spine may have moved out of its normal position."
    flowchart['A4'] = "See your doctor. You may have pulled a muscle."
    flowchart['N6'] = "Can you feel any swelling or bumps in the sides or back of your neck?"
    flowchart['A5'] = "See your doctor. You may have swollen lymph glands."
    flowchart['N7'] = "Did you wake up with a stiff neck, although your neck felt fine when you went to bed?"
    flowchart['N8'] = "Has the pain or stiffness been getting worse for several months?"
    flowchart['A6'] = "See your doctor if your neck still hurts after 24 hours. You probably slept in an awkward position or in a draft, causing a painful, severe muscle spasm."
    flowchart['A7'] = "See your doctor. You may have a disorder of the joints in the neck. Or you may have a nerve disorder such as carpal tunnel syndrome."
    flowchart['N9'] = "Do you have numbness or tingling in your arm or hand, or are you over age 50?"
    flowchart['A8'] = "See your doctor if you are unable to make a decision from self-triage and the problem persists for more than 24 hours."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N8", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "N4", "Yes"),
        ("N3", "N6", "No"),
        ("N4", "A2", "Yes"), 
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "A4", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "N8", "No"),
        ("N7", "A6", "Yes"),
        ("N8", "N9", "Yes"),
        ("N9", "A7", "Yes"),
        ("N9", "A8", "No"), 
        ("N8", "A8", "No")
    
    ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Sore_Mouth_Or_Tongue_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is your tongue sore?"
    flowchart['N2'] = "Is the soreness limited to one area of your tongue?"
    flowchart['N3'] = "Is your tongue red and painful all over?"
    flowchart['N4'] = "Do you have any discolored areas inside your mouth or on your tongue?"
    flowchart['N5'] = "Are the discolored areas whitish yellow, and can they be scraped off easily?"
    flowchart['N6'] = "Are the discolored areas painful, pale yellow spots?"
    flowchart['N7'] = "Do you feel sick, or is your temperature 100°F or higher?"
    flowchart['A1'] = "See your doctor or dentist if your mouth still feels sore after 1 week. Your tongue may be rubbing against a jagged tooth or a poorly fitting denture, or you may have a canker sore. In rare cases, a sore tongue may be an early sign of cancer."
    flowchart['A2'] = "See your doctor. You probably have glossitis (inflammation of the tongue)."
    flowchart['A3'] = "See your doctor or dentist. You may have an oral yeast infection, especially if you have been taking antibiotics or if you use an inhaler for corticosteroid medications to treat asthma. Wearing dentures, especially poorly fitting ones, can also contribute to the development of oral yeast infections."
    flowchart['A5'] = "See your doctor or dentist. You probably have canker sores."
    flowchart['A4'] = "See your doctor. You may have a viral infection."
    flowchart['N8'] = "Are your gums painful, red, and swollen?"
    flowchart['N9'] = "Do you have bad breath, or do you have a bad taste in your mouth?"
    flowchart['N10'] = "Do you have sores on or around your lips?"
    flowchart['N11'] = "Are the sores red, rough, or blistered?"
    flowchart['N12'] = "Do you have cracks at the corners of your mouth?"
    flowchart['N13'] = "Did you recently start using any new cosmetics or lotions on your lips?"
    flowchart['A6'] = "See your dentist. You may have severe gingivitis (inflammation of the gums)."
    flowchart['A7'] = "See your doctor. You may have a cold sore."
    flowchart['A8'] = "See your doctor. You probably have cold sores."
    flowchart['A9'] = "See your doctor or dentist. You may have an oral yeast infection, especially if you have been taking antibiotics or if you use an inhaler for corticosteroid medications to treat asthma. Wearing dentures, especially poorly fitting ones, can also increase the risk of oral yeast infections."
    flowchart['A10'] = "The soreness may be an allergic reaction to an ingredient in the cosmetic or lotion."
    flowchart['A11'] = "See your doctor if you are unable to make a decision from self-triage."



    edges_with_conditions = [("N1", "N2", "Yes"),
                             ("N1", "N4", "No"),
                             ("N2", "A1", "Yes"),
                             ("N2", "N3", "No"),
                             ("N3", "A2", "Yes"),
                             ("N3", "N4", "No"),
                             ("N4", "N5", "Yes"),
                             ("N4", "N8", "No"),
                             ("N5", "A3", "Yes"),
                             ("N5", "N6", "No"),
                             ("N6", "N7", "Yes"),
                             ("N6", "N8", "No"),
                             ("N7", "A4", "Yes"),
                             ("N7", "A5", "No"),
                             ("N8", "N9", "Yes"),  
                             ("N8", "N10", "No"),
                             ("N9", "A6", "Yes"),  
                             ("N9", "A7", "No"),
                             ("N10", "N11", "Yes"), 
                             ("N10", "A11", "No"),
                             ("N11", "A8", "Yes"),  
                             ("N11", "N12", "No"),
                             ("N12", "A9", "Yes"),  
                             ("N12", "N13", "No"),
                             ("N13", "A10", "Yes"),  
                             ("N13", "A11", "No")
                            ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

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
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Twitching_And_Trembling_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Are you taking any medication?"
    flowchart['A1'] = "Talk to your doctor. Some drugs can cause twitching and trembling."
    flowchart['N2'] = "Is the twitching limited to brief flickering movements of one small area of your body, such as an eyelid?"
    flowchart['A2'] = "See your doctor if the twitching bothers you, if you feel sick, or if the affected muscles seem weak. Minor muscle twitching often results from tension or fatigue."
    flowchart['N3'] = "Is the trembling or shaking limited to one part of your body?"
    flowchart['N4'] = "Is the trembling worse when you are not moving the affected part of the body?"
    flowchart['A3'] = "See your doctor. You could have a disorder of the nervous system called parkinson's disease, especially if you are over age 60."
    flowchart['N5'] = "Have you recently stopped drinking alcohol after a long period of heavy drinking?"
    flowchart['A4'] = "See your doctor. Trembling or shaking is a common response of the body to withdrawal from alcohol."
    flowchart['N6'] = "Have you been drinking a lot more caffeine-containing beverages (such as coffee or cola) than usual?"
    flowchart['A5'] = "Caffeine is a stimulant and can make you jittery. The trembling should stop when you stop consuming caffeine."
    flowchart['N7'] = "Do you have two or more of the following symptoms: excessive sweating; unexplained fatigue; bulging eyes; unexplained weight loss?"
    flowchart['A6'] = "See your doctor. You may have an overactive thyroid gland."
    flowchart['A7'] = "Call your doctor. A tendency to tremble or shake can run in families and is often brought on by anxiety or stress."
    flowchart['N8'] = "Does the trembling consist of occasional sudden spasms (jerking movements) of the body or limbs?"
    flowchart['N9'] = "Do the spasms occur only when you are about to fall asleep, and do they stop on their own?"
    flowchart['A8'] = "Such nighttime spasms are normal."
    flowchart['A9'] = "See your doctor. You may have restless legs syndrome. In rare cases, spasms are a sign of a neurological disorder such as parkinson's disease."
    flowchart['A10'] = "See your doctor if you are unable to make a decision from self-triage."



    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "N4", "Yes"),
        ("N3", "N8", "No"),  
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),  
        ("N6", "A5", "Yes"), 
        ("N6", "N7", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "A7", "No"),
        ("N8", "N9", "Yes"),
        ("N8", "A10", "No"),  
        ("N9", "A8", "Yes"),
        ("N9", "A9", "No")
    ]
    
    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Feeling_Faint_And_Fainting_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Was the feeling of faintness accompanied by dizziness?"
    flowchart['F1'] = "Dizziness Flowchart"  # change to dizziness flowchart
    flowchart['N2'] = "Did you stand up suddenly after sitting, lying down, or crouching, or had you just gotten up after a few days in bed?"
    flowchart['N3'] = "Are you taking medication for high blood pressure?"
    flowchart['A1'] = "See your doctor. You probably felt faint because of a temporary drop in blood pressure."
    flowchart['A2'] = "See your doctor. Your blood pressure may have fallen too low and your doctor may need to adjust the dosage of your medication or prescribe a different drug."
    flowchart['N4'] = "Were you exercising more vigorously than usual, and were you short of breath just before you felt faint?"
    flowchart['A3'] = "See a doctor immediately. You may have an arrhythmia. Or you may have an abnormal heart valve."
    flowchart['N5'] = "Have you not eaten for some time, or do you have diabetes?"
    flowchart['A4'] = "See your doctor if you have diabetes so you can discuss ways to control your blood sugar better. Low blood sugar may be causing you to feel faint. Drinking something sweet or eating something sugary or starchy will probably make you feel better."
    flowchart['N6'] = "Did you spend several hours in strong sunlight or in very hot or stuffy conditions?"
    flowchart['A5'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could have heat exhaustion, which can lead to heatstroke, a life-threatening condition."
    flowchart['N7'] = "Have you had one or more of the following symptoms: numbness or tingling in any part of your body; blurred vision; confusion; difficulty speaking; loss of movement in your arms or legs?"
    flowchart['A6'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have had a stroke or a transient ischemic attack."
    flowchart['N8'] = "Do you have heart disease, or did your heartbeat speed up or slow down just before you felt faint?"
    flowchart['N9'] = "Did you lose consciousness?"
    flowchart['A7'] = "See a doctor immediately. Your loss of consciousness may have been caused by a serious abnormal heart rhythm."
    flowchart['A8'] = "See your doctor. You may have a disorder of heart rate and rhythm, such as an arrhythmia."
    flowchart['N10'] = "Were you breathing very deeply or rapidly before you felt faint?"
    flowchart['A9'] = "Feeling faint was probably caused by hyperventilation, possibly because you were anxious or stressed."
    flowchart['N11'] = "Did you feel faint after a stressful event?"
    flowchart['A10'] = "Stress can affect the nerves that control blood pressure, causing a person to feel faint."
    flowchart['N12'] = "Did you feel faint while doing any of the following: coughing; urinating; stretching; holding your breath?"
    flowchart['A11'] = "See your doctor if you faint or feel faint more than once. Any of these activities can occasionally affect the oxygen supply to the brain."
    flowchart['N13'] = "Are you over 50?"
    flowchart['N14'] = "Does raising or turning your head make you feel faint?"
    flowchart['A12'] = "See your doctor. This symptom can occur in a disorder involving the nerves and bones in the neck called cervical osteoarthritis. See your eye doctor if you wear bifocals; they may be improperly fitted."
    flowchart['N15'] = "Do you feel unusually tired, or are you often short of breath?"
    flowchart['A13'] = "See your doctor. You may have a form of anemia or congestive heart failure. If you are a woman of childbearing age and you feel unusually tired, you may be pregnant."
    flowchart['A14'] = "See your doctor if you are unable to make a decision from self-triage."



    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N3", "A2", "Yes"),
        ("N3", "A1", "No"),
        ("N2", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "N9", "Yes"), 
        ("N9", "A7", "Yes"),
        ("N9", "A8", "No"),
        ("N8", "N10", "No"),
        ("N10", "A9", "Yes"),
        ("N10", "N11", "No"),
        ("N11", "A10", "Yes"),
        ("N11", "N12", "No"),
        ("N12", "A11", "Yes"),
        ("N12", "N13", "No"),
        ("N13", "N14", "Yes"),
        ("N14", "A12", "Yes"),
        ("N14", "N15", "No"),
        ("N13", "N15", "No"),
        ("N15", "A13", "Yes"),
        ("N15", "A14", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Swellings_Under_The_Skin_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Is the lump or swelling painful, red, and warm?"
    flowchart['A1'] = "See your doctor. You may have a skin infection such as a boil. If you recently injured the area, you could have a hematoma, an accumulation of blood caused by bleeding from an injured blood vessel."
    flowchart['N2'] = "Do you have any lumps or swellings in any of the lymph nodes in your neck, armpit, or groin?"
    flowchart['N3'] = "Is your temperature 100°F or higher?"
    flowchart['A2'] = "See your doctor. You could have an infection such as infectious mononucleosis."
    flowchart['N4'] = "Do you smoke?"
    flowchart['A3'] = "See your doctor. A lump in the neck can be a sign of throat cancer."
    flowchart['N5'] = "Did you have a vaccination (such as a typhoid shot) within the past few days?"
    flowchart['A4'] = "Talk to your doctor. Vaccinations can sometimes cause swollen glands."
    flowchart['N6'] = "Are you currently taking any medication?"
    flowchart['A5'] = "Talk to your doctor. Some drugs, especially those used to treat epilepsy and some thyroid disorders, can cause swollen glands."
    flowchart['A6'] = "See a doctor immediately. You may have an infection, but there is also a slight possibility that you have cancer of the lymphatic system."
    flowchart['N7'] = "Is the area between your ear and the angle of your jaw swollen, painful, or tender?"
    flowchart['N8'] = "Is the swelling on both sides of your face?"
    flowchart['A7'] = "Call your doctor. You could have mumps."
    flowchart['A8'] = "See a doctor immediately. Swelling on one side of the face can result from mumps, a tooth abscess, a stone in the salivary duct or gland, or a salivary gland tumor."
    flowchart['N9'] = "Do you have swelling on both sides of the back of your neck?"
    flowchart['N10'] = "Do you have a pink rash, or is your temperature 100°F or higher?"
    flowchart['A9'] = "See your doctor. You could have rubella or infectious mononucleosis."
    flowchart['N11'] = "Is the swelling on both sides of your neck?"
    flowchart['N12'] = "Do you have a sore throat?"
    flowchart['A10'] = "See a doctor immediately. You may have a throat infection such as strep throat, tonsillitis, or pharyngitis. Or you could have a more generalized infection such as infectious mononucleosis or possibly HIV."
    flowchart['A11'] = "See your doctor. You probably have a throat infection such as strep throat, tonsillitis, or pharyngitis. However, you may have a cancer of the lymphatic system such as hodgkin's disease or non-hodgkin's lymphoma or possibly HIV."
    flowchart['N13'] = "Is the swelling at the front of your neck, and does it move when you swallow?"
    flowchart['A12'] = "See your doctor. The lump could simply be your larynx (Adam's apple). However, you could have goiter caused by hyperthyroidism or a thyroid nodule."
    flowchart['N14'] = "Is the swelling only in your armpit?"
    flowchart['A13'] = "See your doctor. The glands in your armpit could be swollen as a result of an infection in your arm, possibly from a cut or scratch. However, this type of swelling is sometimes one of the first signs of breast cancer or lung cancer."
    flowchart['N15'] = "Is the swelling in your groin?"
    flowchart['N16'] = "Is it a soft lump that disappears when you lie down and press on it, or does it enlarge when you cough or strain?"
    flowchart['A14'] = "See your doctor. You could have a femoral or inguinal hernia."
    flowchart['A15'] = "See your doctor. Your glands are probably swollen as a result of an infection."
    flowchart['N17'] = "Do you have a lump in your breast?"
    flowchart['A16'] = "See a doctor immediately. Most breast lumps are harmless cysts. However, breast lumps can also be a sign of breast cancer."
    flowchart['A17'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "A6", "No"),
        ("N2", "N7", "No"),
        ("N7", "N8", "Yes"),
        ("N8", "A7", "Yes"),
        ("N8", "A8", "No"),
        ("N7", "N9", "No"),
        ("N9", "N10", "Yes"),
        ("N10", "A9", "Yes"),
        ("N10", "N12", "No"), 
        ("N9", "N11", "No"), 
        ("N11", "N12", "Yes"),
        ("N12", "A10", "Yes"),
        ("N12", "A11", "No"),
        ("N11", "N13", "No"), 
        ("N13", "A12", "Yes"),
        ("N13", "N14", "No"),
        ("N14", "A13", "Yes"),
        ("N14", "N15", "No"),
        ("N15", "N16", "Yes"),
        ("N16", "A14", "Yes"),
        ("N16", "A15", "No"),
        ("N15", "N17", "No"),
        ("N17", "A16", "Yes"),
        ("N17", "A17", "No")
]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

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
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G




def Foot_Problems_Flowchart():
    flowchart = {}

  
    flowchart['N1'] = "Have you injured your foot within the past 24 hours?"
    flowchart['A1'] = "See a doctor immediately. You may have broken a bone or strained a ligament."
    flowchart['N2'] = "Do both feet ache all over?"
    flowchart['N3'] = "Have you been walking or standing for long periods of time?"
    flowchart['A2'] = "Call your doctor if the pain persists. Your feet may simply be overtired, but the pain may also be caused by stretching or straining of the ligaments of your feet. You may have to wear arch supports and perform exercises to help strengthen the ligaments and muscles of your feet. If you are overweight, losing weight can ease some of the strain on the ligaments."
    flowchart['N4'] = "Are you overweight according to the body mass index?"
    flowchart['A3'] = "See your doctor. Carrying extra weight puts a strain on your feet."
    flowchart['N5'] = "Did the pain start after walking or running?"
    flowchart['A4'] = "See your doctor. You may have broken a small bone in your foot. Or you may have a swollen nerve that rubs between two bones when you walk or run. However, if you have pain in the foot when you walk that disappears promptly when you stop, you may have a circulatory disorder such as atherosclerosis."
    flowchart['N6'] = "Do you have pain in one or more toe joints?"
    flowchart['N7'] = "Is the pain accompanied by redness and swelling?"
    flowchart['N8'] = "Is only one toe joint affected?"
    flowchart['A5'] = "See your doctor. You may have gout or pseudogout."
    flowchart['N10'] = "Are you over age 50 and do you also have pain in your ankle, knee, or hip?"
    flowchart['A6'] = "See your doctor. You may have osteoarthritis."
    flowchart['N9'] = "Do you have pain in the sole of your foot, heel pain, thick areas of skin on your toes or on the bottoms of your feet, or a swollen area at the base of your big toe?"
    flowchart['N11'] = "Did the pain begin suddenly?"
    flowchart['N12'] = "Do you also have similar symptoms in your finger joints and other joints?"
    flowchart['A8'] = "See your doctor. You may have rheumatoid arthritis."
    flowchart['A7'] = "See your doctor. You may have an infected toe."
    flowchart['N13'] = "Do you have a patch of skin on the sole of your foot that is painful when you walk, or thick areas of skin on the bottoms of your feet or on your toes?"
    flowchart['A9'] = " A small spot of thick skin on the sole may be a plantar wart. Thick skin on the soles of the feet may be calluses, and thick skin on the toes may be corns."
    flowchart['N14'] = "Is there an area of redness or swelling on the sole of your foot, heel pain, or a swollen area at the base of your big toe?"
    flowchart['A10'] = "See your doctor. If you have pain in the sole, you may have an infection resulting from a minor cut, or you may have torn the fibrous tissue at the bottom of your foot, which is a common cause of heel pain. A swollen area at the base of the big toe probably is a bunion." 
    flowchart['N15'] = "Do you have itching in one or both feet?"
    flowchart['A12'] = "See your doctor if you are unable to make a decision from self-triage."
    flowchart['N16'] = "Is the skin between your toes red, soft, and peeling?"
    flowchart['A11'] = "See your doctor. You may have a fungal infection such as athlete's foot."
    

    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "N5", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "N7", "Yes"),
        ("N6", "N9", "No"), 
        ("N7", "N8", "Yes"),
        ("N7", "N10", "No"), 
        ("N8", "A5", "Yes"),
        ("N8", "N11", "No"), 
        ("N10", "N9", "No"),
        ("N10", "A6", "Yes"),
        ("N11", "A7", "No"), 
        ("N11", "N12", "Yes"),
        ("N12", "A7", "No"),
        ("N12", "A8", "Yes"),
        ("N9", "N15", "No"),
        ("N9", "N13", "Yes"),
        ("N13", "N14", "No"),
        ("N13", "A9", "Yes"),
        ("N14", "N15", "No"), 
        ("N14", "A10", "Yes"),
        ("N15", "N16", "Yes"), 
        ("N15", "A12", "No"),
        ("N16", "A12", "No"),
        ("N16", "A11", "Yes")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G






def Abnormal_Vaginal_Discharge_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Does the discharge look normal in color and consistency but is heavier than usual??"
    flowchart['N2'] = "Do you have itching or soreness in the vaginal area?"
    flowchart['F1'] = "Vaginal Irritation Flowchart" #change to vaginal irritation flowchart
    flowchart['N3'] = "Is the discharge white and lumpy?"
    flowchart['A1'] = "See your doctor. Both oral contraceptives and pregnancy cause hormonal changes that can increase vaginal discharge."
    flowchart['A2'] = "Increased vaginal discharge is normal in the middle of the menstrual cycle, when ovulation occurs."
    flowchart['N4'] = "Are you taking oral contraceptives, or could you be pregnant?"
    flowchart['N5'] = "Is the discharge particularly heavy about halfway between periods?"
    flowchart['A3'] = "See your doctor. You may have a vaginal yeast infection."
    flowchart['N6'] = "Is the discharge greenish yellow with an unpleasant odor?"
    flowchart['N7'] = "Do you have pain in your lower abdomen?"
    flowchart['N8'] = "Is it possible you forgot to remove a tampon or contraceptive device (such as a diaphragm)?"
    flowchart['A4'] = "See a doctor immediately. The discharge may result from an acute infection of the uterus, fallopian tubes, ovaries, or surrounding tissues."
    flowchart['N9'] = "Is the discharge red or brown, or do you have occasional spotting between periods?"
    flowchart['F2'] = "Irregular Vaginal Bleeding Flowchart" #change to irregular vaginal bleeding flowchart
    flowchart['A5'] = "See a doctor immediately after you remove the object, especially if you feel ill or have developed a rash or fever. The object may have caused an infection."
    flowchart['A6'] = "See your doctor. You may have a vaginal infection."
    flowchart['A7'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "F1", "Yes"),
        ("N2", "N4", "No"),
        ("N3", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N4", "A1", "Yes"),
        ("N5", "A2", "Yes"),
        ("N5", "N3", "No"),
        ("N3", "N6" ,"No"),
        ("N6", "N7", "Yes"),
        ("N6", "N9", "No"),
        ("N7", "A4", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A5", "Yes"),
        ("N8", "A6", "No"),
        ("N9", "F2", "Yes"),
        ("N9", "A7", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])
    
    return flowchart, G


def Pain_Or_Lumps_In_The_Breast_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you had a baby within the past 4 months?"
    flowchart['F1'] = "Breast Problems In New Mothers Flowchart" # chage to breast problems in new mothers flowchart
    flowchart['N2'] = "Can you see or feel one or more lumps in your breast?"
    flowchart['A1'] = "See your doctor. You probably have a harmless cyst or tumor (such as a fibroadenoma). However, you could have breast cancer."
    flowchart['N3'] = "Are both breasts painful or tender?"
    flowchart['N4'] = "Could you be pregnant?"
    flowchart['A2'] = "See your doctor. Breasts often become tender and sensitive during pregnancy, especially during the first few months."
    flowchart['N5'] = "Are your breasts painful just before your period?"
    flowchart['A3'] = "Talk to your doctor. The pain probably results from hormonal changes during your menstrual cycle."
    flowchart['A4'] = "See your doctor if you are unable to make a decision from self-triage."
   

    edges_with_conditions = [
        ("N1", "F1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "N4", "Yes"),
        ("N4", "N5", "No"),
        ("N3", "A4", "No"),
        ("N4", "A2", "Yes"),
        ("N5", "A3", "Yes"),
        ("N5", "A4", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Abnormal_Looking_Stools_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Have you noticed red blood in your stools?"
    flowchart['N2'] = "Do you feel generally ill, or is your temperature 100°F or higher?"
    flowchart['A1'] = "See your doctor. You may have inflammatory bowel disease."
    flowchart['A2'] = "See your doctor. You may have hemorrhoids, an anal fissure, or an anal fistula, or you could have colon cancer."
    flowchart['N3'] = "Are your stools very dark or black, or do they contain dark material?"
    flowchart['N4'] = "Are you taking iron supplements?"
    flowchart['A3'] = "Iron often causes dark stools."
    flowchart['A4'] = "See your doctor immediately. Dark stools may be a sign of bleeding from a peptic ulcer or some other intestinal condition."
    flowchart['N5'] = "Are your stools unusually pale, or do they contain mucus?"
    flowchart['N6'] = "Do the whites of your eyes and your skin look yellow?"
    flowchart['A5'] = "See your doctor. You may have jaundice caused by a liver, bile duct, or gallbladder disorder."
    flowchart['A6'] = "See your doctor. You may have problems with digestion, or you may have an intestinal disorder such as celiac disease or lactose intolerance."
    flowchart['A7'] = "See your doctor if you are unable to make a decision from self-triage."
    


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "A2", "No"),
        ("N3", "N4", "Yes"),
        ("N3", "N5", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "A4", "No"),
        ("N5", "N6", "Yes"),
        ("N5", "A7", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "A6", "No")

    ]


    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G


def Painful_Ankles_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did the pain follow an injury?"
    flowchart['N2'] = "Is it impossible or very painful to move your ankle?"
    flowchart['A1'] = "See a doctor immediately. You may have a broken bone. Or you may have strained a ligament."
    flowchart['A2'] = "See your doctor. You have probably strained a ligament."
    flowchart['N3'] = "Is the pain accompanied by redness and swelling?"
    flowchart['N4'] = "Are both ankles or any other joints (such as your knee or finger joints) affected?"
    flowchart['N5'] = "Is your temperature 100°F or higher, or have you recently started to feel ill?"
    flowchart['A3'] = "See a doctor immediately. You may have rheumatoid arthritis, or you could have a joint infection."
    flowchart['A4'] = "See your doctor. You may have rheumatoid arthritis."
    flowchart['A5'] = "See your doctor. You may have gout or pseudogout."
    flowchart['N6'] = "Is your temperature 100°F or higher, or have you recently started to feel ill?"
    flowchart['N7'] = "Are you over age 50?"
    flowchart['A6'] = "See your doctor. You may have osteoarthritis or gout or pseudogout."
    flowchart['A7'] = "See your doctor if you are unable to make a decision from self-triage."


    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "A2", "No"),
        ("N3", "N4", "Yes"),
        ("N3", "N7", "No"),
        ("N4", "N5", "Yes"),  
        ("N4", "N6", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N7", "No"),
        ("N6", "A3", "Yes"), 
        ("N6", "A5", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "A7", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Cramp_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Did the cramp occur while you were sleeping?"
    flowchart['A1'] = "Cramps are common at night during sleep."
    flowchart['N2'] = "Have you been in a very hot place for several hours, and do you have other symptoms such as feeling faint, excessive sweating, clammy skin, rapid heart rate, and rapid breathing?"
    flowchart['A2'] = "EMERGENCY: Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have heat exhaustion."
    flowchart['N3'] = "Did the cramp occur during or shortly after vigorous exercise?"
    flowchart['A3'] = "The cramp was probably caused by overexertion of the muscles. However, if you repeatedly have a cramp in your legs when you walk, you may have a circulatory disorder such as atherosclerosis."
    flowchart['N4'] = "Were you sitting in an awkward position before the cramp occurred?"
    flowchart['A4'] = "Your cramp is probably the result of muscle strain."
    flowchart['A5'] = "See your doctor if you are unable to make a decision from self-triage and you continue to have cramps."
  

    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "A5", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G



def Hallucinations_Flowchart():
    flowchart = {}

    flowchart['N1'] = "Do you have one or more of the following symptoms: general confusion about time, places, or events; agitated behavior; signs of physical illness?"
    flowchart['A1'] = "See a doctor immediately. You could be experiencing delirium."
    flowchart['N2'] = "Do the hallucinations occur only just before you fall asleep or just after you wake up?"
    flowchart['A2'] = "It is normal for hallucinations to occur at the point between sleeping and waking."
    flowchart['N3'] = "Do you drink a lot of alcohol, or do you use illegal drugs?"
    flowchart['A3'] = "Talk to your doctor. Abuse of alcohol or other drugs can cause hallucinations."
    flowchart['N4'] = "Did you think that you saw or heard a close relative or friend who died recently?"
    flowchart['A4'] = "Talk to your doctor, although this type of hallucination often occurs as part of the grieving process."
    flowchart['N5'] = "Do you hear voices?"
    flowchart['A5'] = "See a doctor immediately. Hearing voices may be a sign of a mood disorder or a psychotic disorder, especially if the hallucinations are accompanied by feelings of guilt."
    flowchart['A6'] = "See your doctor if you are unable to make a decision from self-triage."

    edges_with_conditions = [
        ("N1", "A1", "Yes"),
        ("N1", "N2", "No"),
        ("N2", "A2", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A3", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A5", "Yes"),
        ("N5", "A6", "No")
    ]

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.keys())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G
