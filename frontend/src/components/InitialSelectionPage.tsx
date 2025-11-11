import { User, Users } from 'lucide-react';

interface InitialSelectionPageProps {
  onSelect: (queryingFor: 'myself' | 'someone-else') => void;
}

export function InitialSelectionPage({ onSelect }: InitialSelectionPageProps) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50 flex items-center justify-center px-4">
      <div className="max-w-3xl w-full">
        {/* Header Section */}
        <div className="text-center mb-16">
          <div className="inline-block mb-6">
            <div className="flex items-center justify-center gap-3">
              <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg shadow-blue-200">
                <svg 
                  className="w-8 h-8 text-white" 
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
              <h1 className="text-4xl tracking-tight bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                TriageMD
              </h1>
            </div>
          </div>
          
          <h2 className="text-3xl text-gray-800 mb-4">
            Are you here to query for yourself,<br />or for someone else?
          </h2>
          
          <p className="text-lg text-gray-600 max-w-xl mx-auto">
            A Health chatbot that is reliable and interpretable
          </p>
        </div>

        {/* Selection Buttons */}
        <div className="grid md:grid-cols-2 gap-6 max-w-2xl mx-auto">
          {/* Myself Button */}
          <button
            onClick={() => onSelect('myself')}
            className="group relative bg-white rounded-3xl p-10 shadow-xl shadow-blue-100/50 border border-gray-100 hover:border-blue-300 transition-all duration-300 hover:shadow-2xl hover:shadow-blue-200/50 hover:-translate-y-1"
          >
            <div className="flex flex-col items-center gap-6">
              <div className="w-20 h-20 bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl flex items-center justify-center shadow-lg shadow-blue-200 group-hover:shadow-xl group-hover:shadow-blue-300 transition-all">
                <User className="w-10 h-10 text-white" strokeWidth={2.5} />
              </div>
              <div className="text-center">
                <h3 className="text-2xl text-gray-900 mb-2">Myself</h3>
                <p className="text-sm text-gray-600">
                  Get health guidance for your own symptoms
                </p>
              </div>
            </div>
            <div className="absolute inset-0 rounded-3xl bg-gradient-to-br from-blue-500/0 to-purple-500/0 group-hover:from-blue-500/5 group-hover:to-purple-500/5 transition-all pointer-events-none" />
          </button>

          {/* Someone Else Button */}
          <button
            onClick={() => onSelect('someone-else')}
            className="group relative bg-white rounded-3xl p-10 shadow-xl shadow-purple-100/50 border border-gray-100 hover:border-purple-300 transition-all duration-300 hover:shadow-2xl hover:shadow-purple-200/50 hover:-translate-y-1"
          >
            <div className="flex flex-col items-center gap-6">
              <div className="w-20 h-20 bg-gradient-to-br from-purple-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg shadow-purple-200 group-hover:shadow-xl group-hover:shadow-purple-300 transition-all">
                <Users className="w-10 h-10 text-white" strokeWidth={2.5} />
              </div>
              <div className="text-center">
                <h3 className="text-2xl text-gray-900 mb-2">Someone Else</h3>
                <p className="text-sm text-gray-600">
                  Help a family member or friend
                </p>
              </div>
            </div>
            <div className="absolute inset-0 rounded-3xl bg-gradient-to-br from-blue-500/0 to-purple-500/0 group-hover:from-blue-500/5 group-hover:to-purple-500/5 transition-all pointer-events-none" />
          </button>
        </div>

        {/* Trust Indicators */}
        <div className="mt-16 text-center">
          <div className="flex items-center justify-center gap-8 text-sm text-gray-500">
            <div className="flex items-center gap-2">
              <svg className="w-5 h-5 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              AMA Compliant
            </div>
            <div className="flex items-center gap-2">
              <svg className="w-5 h-5 text-purple-500" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clipRule="evenodd" />
              </svg>
              Secure & Private
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
