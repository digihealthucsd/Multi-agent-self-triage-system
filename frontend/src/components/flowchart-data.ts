export interface FlowNode {
  id: string;
  label: string;
  type: 'start' | 'question' | 'decision' | 'action' | 'end';
}

export interface FlowEdge {
  from: string;
  to: string;
  label?: string;
}

export interface FlowchartData {
  id: string;
  name: string;
  description: string;
  nodes: FlowNode[];
  edges: FlowEdge[];
}

// Abdominal Pain Flowchart
export const abdominalPainFlowchart: FlowchartData = {
  id: 'abdominal-pain',
  name: 'Abdominal Pain Flowchart',
  description: 'Assessment for patients experiencing abdominal pain, including severity evaluation and potential causes.',
  nodes: [
    { id: 'start', label: 'Abdominal Pain\nFlowchart', x: 215, y: 50, type: 'start', width: 140, height: 50 },
    { id: 'symptoms_check', label: 'Have you had similar\nepisodes of pain that\ncome and go?', x: 215, y: 140, type: 'question', width: 180, height: 80 },
    { id: 'severe_yes', label: 'Severe or\nRecurring\nAbdominal Pain', x: 320, y: 260, type: 'decision', width: 140, height: 80 },
    { id: 'severe_no', label: 'Is the pain\nsevere?', x: 110, y: 260, type: 'decision', width: 120, height: 70 },
    { id: 'pain_scale', label: 'Do you have\ndiarrhea?', x: 110, y: 370, type: 'question', width: 120, height: 60 },
    { id: 'high_pain', label: 'Do you have one or\nmore of the following?\n• Severe pain\n• Swollen abdomen\n• Fever over 100°F', x: 320, y: 380, type: 'question', width: 190, height: 100 },
    { id: 'emergency', label: 'EMERGENCY\nSeek Immediate Care\nCall 911 or go to ER\n\nPossible:\n• Intestinal Obstruction\n• Appendicitis', x: 320, y: 530, type: 'end', width: 190, height: 130 },
    { id: 'see_doctor', label: 'See Your Doctor\n\nPossible:\n• Food Poisoning\n• Gastroenteritis\n• Inflammatory Bowel', x: 200, y: 530, type: 'action', width: 160, height: 110 },
    { id: 'low_pain', label: 'Did pain occur\nafter a meal?', x: 60, y: 530, type: 'question', width: 140, height: 70 },
    { id: 'clarification', label: 'Monitor and Rest\nSeek care if worsens', x: 60, y: 650, type: 'action', width: 140, height: 60 },
  ],
  edges: [
    { from: 'start', to: 'symptoms_check' },
    { from: 'symptoms_check', to: 'severe_yes', label: 'Yes' },
    { from: 'symptoms_check', to: 'severe_no', label: 'No' },
    { from: 'severe_no', to: 'pain_scale', label: 'No' },
    { from: 'severe_no', to: 'see_doctor', label: 'Yes' },
    { from: 'severe_yes', to: 'high_pain' },
    { from: 'high_pain', to: 'emergency', label: 'Yes' },
    { from: 'high_pain', to: 'see_doctor', label: 'No' },
    { from: 'pain_scale', to: 'low_pain', label: 'No' },
    { from: 'pain_scale', to: 'see_doctor', label: 'Yes' },
    { from: 'low_pain', to: 'clarification', label: 'No' },
    { from: 'low_pain', to: 'see_doctor', label: 'Yes' },
  ],
};

// Chest Pain Flowchart
export const chestPainFlowchart: FlowchartData = {
  id: 'chest-pain',
  name: 'Chest Pain Flowchart',
  description: 'Evaluation of chest pain symptoms to identify potential cardiac or respiratory issues.',
  nodes: [
    { id: 'start', label: 'Chest Pain\nFlowchart', x: 215, y: 50, type: 'start', width: 140, height: 50 },
    { id: 'severity', label: 'Is the pain\nsevere or\ncrushing?', x: 215, y: 140, type: 'question', width: 140, height: 80 },
    { id: 'breathing', label: 'Difficulty\nBreathing?', x: 320, y: 250, type: 'decision', width: 130, height: 70 },
    { id: 'radiation', label: 'Does pain\nradiate to arm\nor jaw?', x: 110, y: 250, type: 'question', width: 140, height: 80 },
    { id: 'emergency', label: 'EMERGENCY\nCall 911\n\nPossible:\n• Heart Attack\n• Pulmonary Embolism', x: 320, y: 380, type: 'end', width: 180, height: 110 },
    { id: 'urgent_care', label: 'Seek Urgent Care\n\nPossible:\n• Angina\n• Pleurisy', x: 170, y: 380, type: 'action', width: 150, height: 90 },
    { id: 'monitor', label: 'Monitor Symptoms\nSee doctor if worsens', x: 50, y: 380, type: 'action', width: 150, height: 70 },
  ],
  edges: [
    { from: 'start', to: 'severity' },
    { from: 'severity', to: 'breathing', label: 'Yes' },
    { from: 'severity', to: 'radiation', label: 'No' },
    { from: 'breathing', to: 'emergency', label: 'Yes' },
    { from: 'breathing', to: 'urgent_care', label: 'No' },
    { from: 'radiation', to: 'urgent_care', label: 'Yes' },
    { from: 'radiation', to: 'monitor', label: 'No' },
  ],
};

// Headache Flowchart
export const headacheFlowchart: FlowchartData = {
  id: 'headache',
  name: 'Headache Flowchart',
  description: 'Assessment for headaches, including evaluation of severity, duration, and associated symptoms.',
  nodes: [
    { id: 'start', label: 'Headache\nFlowchart', x: 215, y: 50, type: 'start', width: 140, height: 50 },
    { id: 'sudden', label: 'Was onset\nsudden and\nsevere?', x: 215, y: 140, type: 'question', width: 140, height: 80 },
    { id: 'neurological', label: 'Vision changes,\nweakness, or\nconfusion?', x: 320, y: 250, type: 'decision', width: 150, height: 80 },
    { id: 'fever', label: 'Do you have\na fever or\nstiff neck?', x: 110, y: 250, type: 'question', width: 130, height: 80 },
    { id: 'emergency', label: 'EMERGENCY\nSeek Immediate Care\n\nPossible:\n• Stroke\n• Brain Hemorrhage\n• Meningitis', x: 320, y: 380, type: 'end', width: 180, height: 120 },
    { id: 'see_doctor', label: 'See Your Doctor\n\nPossible:\n• Migraine\n• Tension Headache', x: 170, y: 400, type: 'action', width: 150, height: 90 },
    { id: 'home_care', label: 'Rest and Hydrate\nMonitor symptoms', x: 50, y: 400, type: 'action', width: 140, height: 70 },
  ],
  edges: [
    { from: 'start', to: 'sudden' },
    { from: 'sudden', to: 'neurological', label: 'Yes' },
    { from: 'sudden', to: 'fever', label: 'No' },
    { from: 'neurological', to: 'emergency', label: 'Yes' },
    { from: 'neurological', to: 'see_doctor', label: 'No' },
    { from: 'fever', to: 'emergency', label: 'Yes' },
    { from: 'fever', to: 'home_care', label: 'No' },
  ],
};

// Respiratory Symptoms Flowchart
export const respiratoryFlowchart: FlowchartData = {
  id: 'respiratory',
  name: 'Respiratory Symptoms Flowchart',
  description: 'Evaluation for cough, shortness of breath, and other respiratory symptoms.',
  nodes: [
    { id: 'start', label: 'Respiratory\nSymptoms', x: 215, y: 50, type: 'start', width: 140, height: 50 },
    { id: 'breathing', label: 'Severe difficulty\nbreathing or\nchest pain?', x: 215, y: 140, type: 'question', width: 150, height: 80 },
    { id: 'oxygen', label: 'Blue lips or\nface?', x: 320, y: 250, type: 'decision', width: 120, height: 70 },
    { id: 'duration', label: 'Symptoms for\nmore than\n7 days?', x: 110, y: 250, type: 'question', width: 130, height: 80 },
    { id: 'emergency', label: 'EMERGENCY\nCall 911\n\nPossible:\n• Severe Asthma\n• Pneumonia\n• COVID-19', x: 320, y: 370, type: 'end', width: 170, height: 110 },
    { id: 'see_doctor', label: 'See Your Doctor\n\nPossible:\n• Bronchitis\n• Upper Respiratory\n  Infection', x: 170, y: 380, type: 'action', width: 150, height: 100 },
    { id: 'home_care', label: 'Rest and Monitor\nStay hydrated', x: 50, y: 390, type: 'action', width: 130, height: 70 },
  ],
  edges: [
    { from: 'start', to: 'breathing' },
    { from: 'breathing', to: 'oxygen', label: 'Yes' },
    { from: 'breathing', to: 'duration', label: 'No' },
    { from: 'oxygen', to: 'emergency', label: 'Yes' },
    { from: 'oxygen', to: 'see_doctor', label: 'No' },
    { from: 'duration', to: 'see_doctor', label: 'Yes' },
    { from: 'duration', to: 'home_care', label: 'No' },
  ],
};

// All available flowcharts
export const allFlowcharts: FlowchartData[] = [
  abdominalPainFlowchart,
  chestPainFlowchart,
  headacheFlowchart,
  respiratoryFlowchart,
];

// Simulate flowchart retrieval based on user input
export function retrieveFlowchart(userMessage: string): {
  recommended: FlowchartData;
  similar: FlowchartData[];
} {
  const lowerMessage = userMessage.toLowerCase();
  
  // Simple keyword matching for demo
  if (lowerMessage.includes('stomach') || lowerMessage.includes('abdomen') || lowerMessage.includes('abdominal') || lowerMessage.includes('belly')) {
    return {
      recommended: abdominalPainFlowchart,
      similar: [respiratoryFlowchart, headacheFlowchart, chestPainFlowchart],
    };
  } else if (lowerMessage.includes('chest') || lowerMessage.includes('heart')) {
    return {
      recommended: chestPainFlowchart,
      similar: [respiratoryFlowchart, abdominalPainFlowchart, headacheFlowchart],
    };
  } else if (lowerMessage.includes('head') || lowerMessage.includes('migraine')) {
    return {
      recommended: headacheFlowchart,
      similar: [chestPainFlowchart, respiratoryFlowchart, abdominalPainFlowchart],
    };
  } else if (lowerMessage.includes('cough') || lowerMessage.includes('breath') || lowerMessage.includes('lung')) {
    return {
      recommended: respiratoryFlowchart,
      similar: [chestPainFlowchart, headacheFlowchart, abdominalPainFlowchart],
    };
  }
  
  // Default to abdominal pain
  return {
    recommended: abdominalPainFlowchart,
    similar: [chestPainFlowchart, headacheFlowchart, respiratoryFlowchart],
  };
}
