import React from 'react';
import Chatbot from './components/Chatbot';

function App() {
  return (
    <div className="bg-blue-50 min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold text-blue-700 mb-6">Mental Health Support Bot</h1>
      <div className="w-full max-w-2xl bg-white shadow-lg rounded-lg p-6">
        <Chatbot />
      </div>
    </div>
  );
}

export default App;