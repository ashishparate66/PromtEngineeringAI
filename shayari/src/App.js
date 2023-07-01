import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [keyword, setKeyword] = useState('');
  const [shayari, setShayari] = useState('');
  const apiUrl = 'https://api.openai.com/v1/chat/completions';
  const apiKey = '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';

  const generateShayari = async () => {
    try {
      const response = await axios.post(apiUrl, {
        messages: [
          {
            role: 'system',
            content: `You are a poet.`,
          },
          {
            role: 'user',
            content: `Generate a shayari about ${keyword}`,
          },
        ],
      }, {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json',
        },
      });

      const generatedShayari = response.data.choices[0].message.content;
      setShayari(generatedShayari);
    } catch (error) {
      console.error('Failed to generate shayari:', error);
      setShayari('Error: Failed to generate shayari');
    }
  };

  return (
    <div className="App">
      <h1>Shayari Generator</h1>
      <input
        type="text"
        placeholder="Enter a keyword"
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
      />
      <button onClick={generateShayari}>Generate</button>
      {shayari && <p className="shayari">{shayari}</p>}
    </div>
  );
}

export default App;
