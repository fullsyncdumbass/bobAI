# -----------------------------
# HTMLBob 1.0 Backend Setup Instructions
# -----------------------------
# This file contains setup instructions for the Node.js backend.
# The actual backend implementation is in server.js

"""
HTMLBob 1.0 Backend Setup Guide

OVERVIEW:
- Backend is Node.js/Express server that connects to OpenAI API
- Server runs on http://localhost:5174
- Frontend (bob.html) sends requests to /api/bob endpoint

PREREQUISITES:
1. Node.js installed (https://nodejs.org)
2. OpenAI API key (https://platform.openai.com/api-keys)

SETUP STEPS:
1. Install dependencies:
   npm install

2. Set up your OpenAI API key:
   Edit .env file and replace 'your_openai_api_key_here' with your actual API key

3. Start the backend server:
   npm start
   # OR
   node server.js

4. Open bob.html in browser and toggle "Use LLM" checkbox

FILES:
- server.js: Main backend server code (OpenAI integration)
- package.json: Node.js dependencies and scripts
- .env: Environment variables (API key)
- bob.html: Frontend application

ENVIRONMENT VARIABLES (.env file):
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo

API ENDPOINT:
POST /api/bob
{
  "userText": "Hello Bob",
  "trustBefore": 50,
  "wasDefensive": false,
  "triggered": false,
  "backedOff": false,
  "liked": null,
  "stateBefore": "Neutral"
}

RESPONSE:
{
  "reply": "Bob's response text",
  "state": "Neutral|Trusting|Defensive",
  "trustDelta": -10 to +20
}

MODELS:
- gpt-3.5-turbo: Cheapest, good for testing (~$0.002 per conversation)
- gpt-4: More expensive but better responses (~$0.06 per conversation)
- gpt-4-turbo-preview: Latest model, good balance

TROUBLESHOOTING:
- If API calls fail, check your OpenAI API key in .env file
- If no API key, server falls back to enhanced rule-based responses
- Check console for "OpenAI unavailable" messages
"""