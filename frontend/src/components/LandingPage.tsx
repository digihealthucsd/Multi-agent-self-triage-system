import { useState } from 'react';
import { InitialSelectionPage } from './InitialSelectionPage';
import { PatientIntakeForm } from './PatientIntakeForm';
import { PatientInfo } from '../App';
import { ArrowLeft } from 'lucide-react';
import { Button } from './ui/button';

interface LandingPageProps {
  onStartChat: (info: PatientInfo) => void;
}

export function LandingPage({ onStartChat }: LandingPageProps) {
  const [step, setStep] = useState<'initial' | 'form'>('initial');
  const [queryingFor, setQueryingFor] = useState<'myself' | 'someone-else'>('myself');

  const handleSelection = (selection: 'myself' | 'someone-else') => {
    setQueryingFor(selection);
    setStep('form');
  };

  const handleBack = () => {
    setStep('initial');
  };

  if (step === 'initial') {
    return <InitialSelectionPage onSelect={handleSelection} />;
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-white via-blue-50/30 to-purple-50/30">
      <div className="container mx-auto px-4 py-8 md:py-16">
        <div className="max-w-2xl mx-auto">
          {/* Back button */}
          <div className="mb-6">
            <Button
              variant="ghost"
              size="sm"
              onClick={handleBack}
              className="text-gray-600 hover:text-gray-900"
            >
              <ArrowLeft className="w-4 h-4 mr-2" />
              Back
            </Button>
          </div>

          {/* Header Section */}
          <div className="text-center mb-12">
            <div className="inline-block mb-4">
              <div className="flex items-center justify-center gap-2">
                <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center">
                  <svg 
                    className="w-6 h-6 text-white" 
                    fill="none" 
                    stroke="currentColor" 
                    viewBox="0 0 24 24"
                  >
                    {/* Chat bubble */}
                    <path 
                      strokeLinecap="round" 
                      strokeLinejoin="round" 
                      strokeWidth={2} 
                      d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" 
                    />
                    {/* Medical cross inside */}
                    <path 
                      strokeLinecap="round" 
                      strokeLinejoin="round" 
                      strokeWidth={2.5} 
                      d="M12 9v6M9 12h6" 
                    />
                  </svg>
                </div>
                <h1 className="text-3xl tracking-tight">TriageMD</h1>
              </div>
            </div>
            <p className="text-lg text-gray-600 max-w-xl mx-auto">
              A Virtual Assistant for Medical Inquiries
            </p>
            <p className="mt-3 text-gray-500">
              Get personalized health guidance in minutes
            </p>
          </div>

          {/* Main Form Card */}
          <PatientIntakeForm onSubmit={onStartChat} queryingFor={queryingFor} />

          {/* Trust Indicators */}
          <div className="mt-12 text-center">
            <p className="text-sm text-gray-500 mb-4">
              A Health chatbot that is reliable and interpretable
            </p>
            <div className="flex items-center justify-center gap-8 text-xs text-gray-400">
              <div className="flex items-center gap-2">
                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                AMA Compliant
              </div>
              <div className="flex items-center gap-2">
                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clipRule="evenodd" />
                </svg>
                Secure & Private
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
