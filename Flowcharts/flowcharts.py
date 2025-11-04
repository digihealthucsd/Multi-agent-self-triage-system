import networkx as nx

# an examples of the self-triage flowcharts
# for the complete version of flowcharts, please refer to American Medical Association Family Medical Guide, 4th Edition

def Feeling_Generally_Ill_Flowchart():
    
    # initialize a dict to store flowchart content
    flowchart = {}

    # define nodes
    flowchart['N1'] = "Is your temperature 100°F or higher?"
    flowchart['F1'] = "Fever Flowchart" # change to fever flowchart
    flowchart['N2'] = "Do you suddenly feel unusually tired, and do you have any discomfort in your chest or arms when you move around?"
    flowchart['A1'] = "See a doctor immediately. Sudden onset of such symptoms may indicate that you have heart disease and are at risk of having a heart attack."
    flowchart['N3'] = "Do you feel nervous or anxious?"
    flowchart['I1'] = "You may have anxiety." # provide the information to patient before going to the linked flowchart
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

    # define edges with conditions
    # (from_node, to_node, condition)
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
    G.add_nodes_from(flowchart.items())

    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G