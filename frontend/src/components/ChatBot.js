import React, { useState } from 'react';
import axios from 'axios';

const ChatBot = () => {
  const [file, setFile] = useState(null);
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');

  const handleFileUpload = (e) => {
    setFile(e.target.files[0]);
  };

  const handleFileSubmit = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/upload_pdf', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      console.log(response.data.message);
    } catch (error) {
      console.error('Error uploading PDF:', error);
    }
  };

  const handleQuerySubmit = async () => {
    try {
      const response = await axios.post('http://localhost:5000/ask_question', { query });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error fetching answer:', error);
    }
  };

  return (
    <div>
      <h1>Advanced PDF Reader Chatbot</h1>

      <div>
        <input type="file" onChange={handleFileUpload} />
        <button onClick={handleFileSubmit}>Upload PDF</button>
      </div>

      <div>
        <input 
          type="text" 
          value={query} 
          onChange={(e) => setQuery(e.target.value)} 
          placeholder="Ask a question based on the PDF" 
        />
        <button onClick={handleQuerySubmit}>Ask Question</button>
      </div>

      {answer && (
        <div>
          <h3>Answer:</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
};

export default ChatBot;
