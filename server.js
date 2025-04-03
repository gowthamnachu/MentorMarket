const express = require('express');
const axios = require('axios');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
const port = 3000;

app.use(express.json());

// API endpoint to receive user message and get AI response
app.post('/get_response', async (req, res) => {
    const userMessage = req.body.message;

    try {
        // Call OpenAI GPT API (replace with your own OpenAI API key)
        const response = await axios.post('https://api.openai.com/v1/completions', {
            model: 'text-davinci-003', // Or other GPT models
            prompt: `Answer this question about MentorMarket: ${userMessage}`,
            max_tokens: 150,
            temperature: 0.7,
        }, {
            headers: {
                'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
            }
        });

        // Send the AI response back to the frontend
        const aiResponse = response.data.choices[0].text.trim();
        res.json({ response: aiResponse });
    } catch (error) {
        console.error('Error from OpenAI API:', error);
        res.status(500).send('Error getting response from AI');
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
