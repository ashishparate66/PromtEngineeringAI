const express = require('express');
const OpenAI = require('openai');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 5000;

// Set up the OpenAI API client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

app.use(express.json());

// API endpoint for generating shayari
app.get('/generate-shayari', async (req, res) => {
  const { keyword } = req.query;

  try {
    // Generate shayari using ChatGPT
    const response = await openai.complete({
      engine: 'davinci',
      prompt: `Write a shayari about ${keyword}`,
      maxTokens: 50,
      temperature: 0.7,
      n: 1,
      stop: '\n',
    });

    const shayari = response.choices[0].text.trim();
    res.json({ shayari });
  } catch (error) {
    console.error('Error generating shayari:', error);
    res.status(500).json({ error: 'Failed to generate shayari' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
