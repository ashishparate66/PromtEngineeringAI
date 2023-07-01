import './App.css';
import React, { useState } from 'react';

function App() {
  const [keyword, setKeyword] = useState('');
  const [shayari, setShayari] = useState('');

  const handleKeywordChange = (event) => {
    setKeyword(event.target.value);
  };

  const handleGenerateShayari = () => {
    fetch(`https://copper-fish-belt.cyclic.app/shayari?keyword=${keyword}`)
      .then((response) => response.json())
      .then((data) => setShayari(data.shayari))
      .catch((error) => console.log(error));
  };

  return (
    <div className="App">
      <input type="text" value={keyword} onChange={handleKeywordChange} />
      <button onClick={handleGenerateShayari}>Generate Shayari</button>
      {shayari && (
        <p className="shayari">{shayari}</p>
      )}
    </div>
  );
}

export default App;