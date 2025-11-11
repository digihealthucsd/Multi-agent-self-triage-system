import { useState, useRef, useEffect } from 'react';
import { PatientInfo } from '../App';
import { Button } from './ui/button';
import { Textarea } from './ui/textarea';
import { Send } from 'lucide-react';
import { FlowchartData } from './flowchart-data';
import { sendChatMessage } from '../services/triageApi';

export interface FlowchartOption {
  id: string;
  name: string;
  description: string;
}

export interface Message {
  id: string;
  sender: 'user' | 'bot';
  text: string;
  timestamp: Date;
  nodeId?: string;
  flowchartSelection?: {
    recommended: FlowchartOption;
    others: FlowchartOption[];
  };
}

interface ChatInterfaceProps {
  patientInfo: PatientInfo;
  messages: Message[];
  setMessages: React.Dispatch<React.SetStateAction<Message[]>>;
  onNodeVisit: (nodeId: string) => void;
  onFirstMessage: (userMessage: string) => void;
  isInitialStage: boolean;
  isLoadingFlowchart: boolean;
  onFlowchartSelect?: (flowchartId: string) => void;
  selectedFlowchart: FlowchartData | null;
}

export function ChatInterface({ 
  patientInfo, 
  messages, 
  setMessages, 
  onNodeVisit, 
  onFirstMessage, 
  isInitialStage,
  isLoadingFlowchart,
  onFlowchartSelect,
  selectedFlowchart
}: ChatInterfaceProps) {
  const [inputValue, setInputValue] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [hasUserSentMessage, setHasUserSentMessage] = useState(false);
  const [currentNode, setCurrentNode] = useState('N1');
  const [currentPath, setCurrentPath] = useState<string[]>(['N1']);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async () => {
    if (!inputValue.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      sender: 'user',
      text: inputValue,
      timestamp: new Date()
    };

    setMessages((prev) => [...prev, userMessage]);
    const messageText = inputValue;
    setInputValue('');
    
    // If this is the first user message, trigger flowchart retrieval
    if (!hasUserSentMessage) {
      setHasUserSentMessage(true);
      onFirstMessage(messageText);
      return; // Don't send bot response yet
    }
    
    // Can only chat once flowchart is selected
    if (!selectedFlowchart) {
      return;
    }
    
    setIsTyping(true);

    try {
      // Build conversation history format
      const conversationHistory = messages
        .filter(m => m.sender !== 'bot' || m.text)
        .map(m => 
          m.sender === 'user' 
            ? `Patient: ${m.text}` 
            : `TriageMD: ${m.text}`
        );
      conversationHistory.push(`Patient: ${messageText}`);
      
      // Call real chat API
      const chatResponse = await sendChatMessage(
        messageText,
        patientInfo,
        conversationHistory,
        currentNode,
        currentPath,
        selectedFlowchart.name
      );
      
      // Update state with response
      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        sender: 'bot',
        text: chatResponse.response,
        timestamp: new Date(),
        nodeId: chatResponse.next_node
      };
      
      onNodeVisit(chatResponse.next_node);
      setMessages((prev) => [...prev, botMessage]);
      
      // Update current node/path for next request
      setCurrentNode(chatResponse.next_node);
      setCurrentPath(chatResponse.current_path);
      
    } catch (error) {
      console.error('Error sending message:', error);
      
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        sender: 'bot',
        text: 'Sorry, I encountered an error. Please try again or check if the backend server is running.',
        timestamp: new Date()
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsTyping(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="h-full flex flex-col max-w-4xl mx-auto">
      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto mb-4 space-y-4 px-4">
        {messages.map((message, index) => (
          <div key={message.id}>
            <div className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`flex gap-3 max-w-[80%] ${message.sender === 'user' ? 'flex-row-reverse' : 'flex-row'}`}>
                {/* Avatar */}
                <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
                  message.sender === 'bot' 
                    ? 'bg-gradient-to-br from-blue-500 to-purple-600' 
                    : 'bg-gray-300'
                }`}>
                  {message.sender === 'bot' ? (
                    <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v6M9 12h6" />
                    </svg>
                  ) : (
                    <svg className="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                  )}
                </div>

                {/* Message Bubble */}
                <div>
                  <div
                    className={`rounded-2xl px-4 py-3 ${
                      message.sender === 'bot'
                        ? 'bg-white shadow-sm border border-gray-100'
                        : 'bg-gradient-to-r from-blue-500 to-purple-600 text-white'
                    }`}
                  >
                    <p className="whitespace-pre-line">{message.text}</p>
                  </div>
                  <div className={`text-xs text-gray-400 mt-1 px-1 ${message.sender === 'user' ? 'text-right' : 'text-left'}`}>
                    {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </div>
                </div>
              </div>
            </div>
            
            {/* Flowchart Selection UI - Appears on right side */}
            {message.flowchartSelection && onFlowchartSelect && (
              <div className="flex justify-end mt-3">
                <div className="flex gap-3 max-w-[80%] flex-row-reverse">
                  {/* Empty space for alignment */}
                  <div className="flex-shrink-0 w-8 h-8"></div>
                  
                  <div className="space-y-3 min-w-[320px]">
                    {/* Most Appropriate Flowchart */}
                    <div>
                      <p className="text-xs text-gray-700 mb-2 text-right" style={{ fontWeight: 600 }}>Most Appropriate Flowchart</p>
                      <Button
                        onClick={() => onFlowchartSelect(message.flowchartSelection!.recommended.id)}
                        className="w-full bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white shadow-md hover:shadow-lg transition-all cursor-pointer px-6 py-3 h-auto"
                      >
                        <span className="flex items-center gap-2 justify-between w-full">
                          <span>{message.flowchartSelection.recommended.name}</span>
                          <svg className="w-4 h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                          </svg>
                        </span>
                      </Button>
                    </div>
                    
                    {/* Other Relevant Flowcharts */}
                    {message.flowchartSelection.others.length > 0 && (
                      <div>
                        <p className="text-xs text-gray-700 mb-2 text-right" style={{ fontWeight: 600 }}>Other Relevant Flowcharts</p>
                        <div className="space-y-2">
                          {message.flowchartSelection.others.map((flowchart) => (
                            <Button
                              key={flowchart.id}
                              onClick={() => onFlowchartSelect(flowchart.id)}
                              className="w-full bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white shadow-md hover:shadow-lg transition-all cursor-pointer px-6 py-3 h-auto"
                            >
                              <span className="flex items-center gap-2 justify-between w-full">
                                <span>{flowchart.name}</span>
                                <svg className="w-4 h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                                </svg>
                              </span>
                            </Button>
                          ))}
                        </div>
                      </div>
                    )}
                    
                    <p className="text-xs text-gray-400 text-right italic">Click to select a flowchart</p>
                  </div>
                </div>
              </div>
            )}
          </div>
        ))}

        {/* Typing Indicator */}
        {isTyping && (
          <div className="flex justify-start">
            <div className="flex gap-3 max-w-[80%]">
              <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
                <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v6M9 12h6" />
                </svg>
              </div>
              <div className="rounded-2xl px-4 py-3 bg-white shadow-sm border border-gray-100">
                <div className="flex gap-1">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
                </div>
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Loading Flowchart Notification Banner - Above Input */}
      {isLoadingFlowchart && (
        <div className="mb-4 bg-blue-50/80 border border-blue-200/50 rounded-lg px-4 py-3 flex items-center gap-3 animate-in fade-in slide-in-from-bottom-2 duration-300">
          <div className="flex-shrink-0">
            <div className="w-5 h-5 border-2 border-purple-600 border-t-transparent rounded-full animate-spin"></div>
          </div>
          <div className="flex-1">
            <p className="text-sm text-gray-700">TriageMD is retrieving the appropriate flowchart for you...</p>
          </div>
        </div>
      )}

      {/* Input Area */}
      <div className="bg-white rounded-2xl shadow-lg border border-gray-200 p-4">
        <div className="flex gap-3 items-end">
          <Textarea
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type your message..."
            className="flex-1 min-h-[50px] max-h-[150px] resize-none border-0 focus-visible:ring-0 focus-visible:ring-offset-0"
            rows={1}
          />
          <Button
            onClick={handleSend}
            disabled={!inputValue.trim() || isTyping}
            className="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white rounded-xl h-12 w-12 p-0"
          >
            <Send className="w-5 h-5" />
          </Button>
        </div>
      </div>
    </div>
  );
}