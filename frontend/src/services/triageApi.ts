import { API_CONFIG } from '../config/api';
import { PatientInfo } from '../App';
import { FlowchartData } from '../components/flowchart-data';

// Types matching backend responses
export interface FlowchartRetrievalResponse {
  flowchart: FlowchartData;
  similar_flowcharts: Array<{
    name: string;
    id: string;
    description: string;
  }>;
  retrieved: boolean;
}

export interface ChatResponse {
  response: string;
  next_node: string;
  current_path: string[];
  prompt_type: number;
  is_terminal: boolean;
}

// API Error handling
class ApiError extends Error {
  constructor(
    message: string,
    public statusCode?: number,
    public details?: any
  ) {
    super(message);
    this.name = 'ApiError';
  }
}

async function fetchWithTimeout(
  url: string,
  options: RequestInit,
  timeout = API_CONFIG.TIMEOUT
): Promise<Response> {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    });
    clearTimeout(id);
    return response;
  } catch (error) {
    clearTimeout(id);
    throw error;
  }
}

export async function retrieveFlowchart(
  patientInfo: PatientInfo,
  openingMessage: string
): Promise<FlowchartRetrievalResponse> {
  try {
    const response = await fetchWithTimeout(
      `${API_CONFIG.BASE_URL}${API_CONFIG.ENDPOINTS.RETRIEVE_FLOWCHART}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          patient_info: patientInfo,
          opening_message: openingMessage,
        }),
      }
    );

    if (!response.ok) {
      const error = await response.json();
      throw new ApiError(
        error.detail || 'Failed to retrieve flowchart',
        response.status,
        error
      );
    }

    return await response.json();
  } catch (error) {
    if (error instanceof ApiError) throw error;
    throw new ApiError('Network error: Unable to reach server');
  }
}

export async function sendChatMessage(
  message: string,
  patientInfo: PatientInfo,
  conversation: string[],
  currentNode: string,
  currentPath: string[],
  flowchartName: string
): Promise<ChatResponse> {
  try {
    const response = await fetchWithTimeout(
      `${API_CONFIG.BASE_URL}${API_CONFIG.ENDPOINTS.CHAT}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message,
          patient_info: patientInfo,
          conversation,
          current_node: currentNode,
          current_path: currentPath,
          flowchart_name: flowchartName,
        }),
      }
    );

    if (!response.ok) {
      const error = await response.json();
      throw new ApiError(
        error.detail || 'Failed to send message',
        response.status,
        error
      );
    }

    return await response.json();
  } catch (error) {
    if (error instanceof ApiError) throw error;
    throw new ApiError('Network error: Unable to reach server');
  }
}



