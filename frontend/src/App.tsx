import { useState } from 'react';
import { LandingPage } from './components/LandingPage';
import { ChatPage } from './components/ChatPage';

export interface PatientInfo {
  name: string;
  sex: string;
  age: string;
  isForSomeoneElse: boolean;
}

export default function App() {
  const [currentPage, setCurrentPage] = useState<'landing' | 'chat'>('landing');
  const [patientInfo, setPatientInfo] = useState<PatientInfo | null>(null);

  const handleStartChat = (info: PatientInfo) => {
    setPatientInfo(info);
    setCurrentPage('chat');
  };

  const handleBackToHome = () => {
    setCurrentPage('landing');
    setPatientInfo(null);
  };

  return (
    <>
      {currentPage === 'landing' ? (
        <LandingPage onStartChat={handleStartChat} />
      ) : (
        <ChatPage patientInfo={patientInfo!} onBackToHome={handleBackToHome} />
      )}
    </>
  );
}
