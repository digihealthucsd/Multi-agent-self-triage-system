import { useState } from 'react';
import { PatientInfo } from '../App';
import { ChatInterface, Message } from './ChatInterface';
import { FlowchartView } from './FlowchartView';
import { Button } from './ui/button';
import { ArrowLeft, ChevronLeft, ChevronRight } from 'lucide-react';
import { FlowchartData } from './flowchart-data';
import { retrieveFlowchart } from '../services/triageApi';

interface ChatPageProps {
  patientInfo: PatientInfo;
  onBackToHome: () => void;
}

type ChatStage = 'initial' | 'loading' | 'flowchart';

export function ChatPage({ patientInfo, onBackToHome }: ChatPageProps) {
  const [chatStage, setChatStage] = useState<ChatStage>('initial');
  const [showFlowchart, setShowFlowchart] = useState(true);
  const [visitedNodes, setVisitedNodes] = useState<string[]>(['start']);
  const [selectedFlowchart, setSelectedFlowchart] = useState<FlowchartData | null>(null);
  const [recommendedFlowchart, setRecommendedFlowchart] = useState<FlowchartData | null>(null);
  const [similarFlowcharts, setSimilarFlowcharts] = useState<FlowchartData[]>([]);
  
  // Debug: Log patientInfo to console
  console.log('ChatPage - patientInfo:', patientInfo);
  
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      sender: 'bot',
      text: `Hi ${patientInfo?.name || 'there'}, how can I help you today?`,
      timestamp: new Date(),
      nodeId: 'start'
    }
  ]);

  const handleFirstMessage = async (userMessage: string) => {
    setChatStage('loading');
    
    try {
      // Call real API to retrieve flowchart
      const result = await retrieveFlowchart(patientInfo, userMessage);
      
      setRecommendedFlowchart(result.flowchart);
      setSimilarFlowcharts(result.similar_flowcharts.map(f => ({
        id: f.id,
        name: f.name,
        description: f.description,
        nodes: [],
        edges: []
      })));
      
      // Add bot message with flowchart selection
      const botMessage: Message = {
        id: Date.now().toString(),
        sender: 'bot',
        text: `Based on your symptoms, I've identified the ${result.flowchart.name}. Let's proceed with your assessment.`,
        timestamp: new Date(),
        flowchartSelection: {
          recommended: {
            id: result.flowchart.id,
            name: result.flowchart.name,
            description: result.flowchart.description
          },
          others: result.similar_flowcharts.slice(0, 2)
        }
      };
      
      setMessages((prev) => [...prev, botMessage]);
      setChatStage('initial'); // Keep in initial stage until flowchart is selected
    } catch (error) {
      console.error('Error retrieving flowcharts:', error);
      
      // Show error message to user
      const errorMessage: Message = {
        id: Date.now().toString(),
        sender: 'bot',
        text: 'Sorry, I encountered an error retrieving the flowchart. Please try again or check if the backend server is running.',
        timestamp: new Date()
      };
      setMessages((prev) => [...prev, errorMessage]);
      setChatStage('initial');
    }
  };

  const handleFlowchartSelection = (flowchartId: string) => {
    // Find the selected flowchart from recommended or similar
    let flowchart: FlowchartData | null = null;
    
    if (recommendedFlowchart?.id === flowchartId) {
      flowchart = recommendedFlowchart;
    } else {
      flowchart = similarFlowcharts.find(f => f.id === flowchartId) || null;
    }
    
    if (!flowchart) return;
    
    setSelectedFlowchart(flowchart);
    setVisitedNodes(['N1']); // Start at N1
    setChatStage('flowchart');
    
    // Get the first question (N1) and ask it
    const firstQuestion = flowchart.nodes.find(n => n.id === 'N1');
    const botMessage: Message = {
      id: Date.now().toString(),
      sender: 'bot',
      text: firstQuestion?.label || `Great! I'll guide you through the ${flowchart.name}. Let's begin.`,
      timestamp: new Date(),
      nodeId: 'N1'
    };
    setMessages((prev) => [...prev, botMessage]);
  };



  return (
    <div className="min-h-screen bg-gradient-to-br from-white via-blue-50/30 to-purple-50/30 flex flex-col">
      {/* Header */}
      <div className="bg-white/80 backdrop-blur-sm border-b border-gray-200 sticky top-0 z-10">
        <div className="px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <Button
                variant="ghost"
                size="sm"
                onClick={onBackToHome}
                className="text-gray-600 hover:text-gray-900"
              >
                <ArrowLeft className="w-4 h-4 mr-2" />
                Back
              </Button>
              <div className="flex items-center gap-2">
                <div className="w-8 h-8 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                  <svg 
                    className="w-5 h-5 text-white" 
                    fill="none" 
                    stroke="currentColor" 
                    viewBox="0 0 24 24"
                  >
                    <path 
                      strokeLinecap="round" 
                      strokeLinejoin="round" 
                      strokeWidth={2} 
                      d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" 
                    />
                    <path 
                      strokeLinecap="round" 
                      strokeLinejoin="round" 
                      strokeWidth={2.5} 
                      d="M12 9v6M9 12h6" 
                    />
                  </svg>
                </div>
                <div>
                  <div className="text-sm text-gray-500">TriageMD</div>
                  <div className="text-xs text-gray-400">AMA Compliant</div>
                </div>
              </div>
            </div>

            {/* Flowchart Toggle - Only show when flowchart is available */}
            {chatStage === 'flowchart' && (
              <Button
                variant="outline"
                size="sm"
                onClick={() => setShowFlowchart(!showFlowchart)}
                className="flex items-center gap-2"
              >
                {showFlowchart ? (
                  <>
                    <ChevronLeft className="w-4 h-4" />
                    Hide Flowchart
                  </>
                ) : (
                  <>
                    <ChevronRight className="w-4 h-4" />
                    Show Flowchart
                  </>
                )}
              </Button>
            )}
          </div>
        </div>
      </div>

      {/* Main Content */}
      {/* Chat State - Always show chat interface */}
      <div className="flex flex-1 overflow-hidden">
        {/* Flowchart Panel - Left Side */}
        {chatStage === 'flowchart' && showFlowchart && selectedFlowchart && (
          <div className="w-[450px] border-r border-gray-200 bg-white flex-shrink-0 overflow-hidden">
            <FlowchartView visitedNodes={visitedNodes} flowchart={selectedFlowchart} />
          </div>
        )}

        {/* Chat Panel */}
        <div className="flex-1 overflow-hidden">
          <div className="h-full px-4 py-6">
            <ChatInterface 
              patientInfo={patientInfo}
              messages={messages}
              setMessages={setMessages}
              onNodeVisit={(nodeId) => {
                if (!visitedNodes.includes(nodeId)) {
                  setVisitedNodes([...visitedNodes, nodeId]);
                }
              }}
              onFirstMessage={handleFirstMessage}
              isInitialStage={chatStage === 'initial'}
              isLoadingFlowchart={chatStage === 'loading'}
              onFlowchartSelect={handleFlowchartSelection}
              selectedFlowchart={selectedFlowchart}
            />
          </div>
        </div>
      </div>
    </div>
  );
}
