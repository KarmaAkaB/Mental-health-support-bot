import React, { useState } from 'react';
import axios from 'axios';

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);

    try {
      const response = await axios.post('http://localhost:8000/chat', {
        message: input,
      });

      const botMessage = { role: 'bot', content: response.data.response };
      setMessages(prev => [...prev, botMessage]);
    } catch (err) {
      const errorMsg = { role: 'bot', content: 'Error reaching the server.' };
      setMessages(prev => [...prev, errorMsg]);
    }

    setInput('');
  };

  return (
    <div>
      <div style={{ maxHeight: '300px', overflowY: 'auto', border: '1px solid #ccc', padding: '10px', marginBottom: '10px' }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{ textAlign: msg.role === 'user' ? 'right' : 'left' }}>
            <strong>{msg.role === 'user' ? 'You' : 'Bot'}:</strong> {msg.content}
          </div>
        ))}
      </div>
      <input
        style={{ width: '80%', padding: '8px' }}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your message..."
      />
      <button style={{ padding: '8px 12px' }} onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chatbot;
