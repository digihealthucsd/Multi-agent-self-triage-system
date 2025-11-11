export const API_CONFIG = {
  BASE_URL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  ENDPOINTS: {
    HEALTH: '/health',
    RETRIEVE_FLOWCHART: '/api/retrieve-flowchart',
    CHAT: '/api/chat',
  },
  TIMEOUT: 30000, // 30 second timeout
} as const;



