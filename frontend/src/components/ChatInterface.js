import React, { useState } from 'react';
import { MessageSquare } from 'lucide-react';
import { sendQuery } from '../services/api';

const ChatInterface = ({ files, messages, setMessages }) => {
  const [question, setQuestion] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSendMessage = async () => {
    if (!question.trim() || loading) return;

    const newMessage = { text: question, sender: 'user', timestamp: new Date() };
    setMessages([...messages, newMessage]);
    setQuestion('');
    setLoading(true);

    try {
      const response = await sendQuery(question);
      setMessages(prev => [...prev, {
        text: response.response,
        sender: 'ai',
        timestamp: new Date(),
        tokens: response.tokens_used
      }]);
    } catch (error) {
      console.error('Query failed:', error);
      alert('Failed to get response');
    } finally {
      setLoading(false);
    }
  };

  if (files.length === 0) {
    return (
      <div className="bg-white rounded-xl shadow-sm p-6 min-h-[600px] flex items-center justify-center">
        <div className="text-center">
          <MessageSquare className="h-12 w-12 text-gray-400 mx-auto mb-4" />
          <p className="text-gray-500">
            Select or upload a document to start a conversation
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl shadow-sm p-6 min-h-[600px] flex flex-col">
      <div className="flex-1 overflow-y-auto space-y-4">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-[70%] rounded-lg p-3 ${
                message.sender === 'user' 
                  ? 'bg-blue-500 text-white' 
                  : 'bg-gray-100'
              }`}
            >
              <p>{message.text}</p>
              {message.tokens && (
                <p className="text-xs mt-1 opacity-75">
                  Tokens used: {message.tokens}
                </p>
              )}
            </div>
          </div>
        ))}
      </div>

      <div className="mt-4">
        <div className="flex space-x-4">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
            placeholder="Ask a question about your document..."
            className="flex-1 rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            disabled={loading}
          />
          <button
            onClick={handleSendMessage}
            disabled={loading}
            className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors disabled:bg-blue-300"
          >
            {loading ? 'Sending...' : 'Send'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;