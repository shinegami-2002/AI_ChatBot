

```markdown
# AI ChatBot

A simple AI ChatBot built with FastAPI as the backend and Streamlit as the frontend. This project uses Python 3.11 and integrates with Groq, OpenAI, and Tavily APIs. Sensitive API keys are stored securely in a `.env` file.

## Overview

- **Backend:** FastAPI application deployed on Render.
- **Frontend:** Streamlit app hosted on Streamlit Community Cloud.
- **API Keys:** Managed using a `.env` file (not tracked in source control).

## Features

- **Chat Endpoint:** FastAPI handles chat requests at the `/chat` endpoint.
- **Interactive Frontend:** Streamlit UI for chatting with the AI agent.
- **API Integrations:** Supports Groq, OpenAI, and Tavily APIs.
- **Secure Configuration:** All API keys and secrets are stored in a `.env` file.

## Live Demo

Try out the AI ChatBot frontend hosted on Streamlit Community Cloud:

[View Demo](https://ai--agent--chatbot.streamlit.app)

## Quick Start

### Local Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/AI_ChatBot.git
   cd AI_ChatBot
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the project root and add your API keys:

   ```ini
   GROQ_API_KEY="your_groq_api_key"
   OPENAI_API_KEY="your_openai_api_key"
   TAVILY_API_KEY="your_tavily_api_key"
   ```

5. **Run the Backend Locally:**

   Navigate to the folder containing `backend.py` (if needed, adjust your commands according to your project layout):

   ```bash
   uvicorn backend:app --host 127.0.0.1 --port 9999
   ```

6. **Run the Frontend Locally:**

   In the project root, run:

   ```bash
   streamlit run frontend.py
   ```

   Make sure the `API_URL` in your `frontend.py` points to your local backend (e.g., `http://127.0.0.1:9999/chat`).

### Deployment

#### Deploying the Backend on Render

1. **Repository Setup:**

   - Push your project to GitHub.
   - In Render’s dashboard, create a new web service.
   - Set the **Root Directory** to the folder that contains your `backend.py` (if needed).

2. **Configure Build & Start Commands:**

   - **Build Command:**  
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:**  
     ```bash
     uvicorn backend:app --host 0.0.0.0 --port $PORT
     ```

3. **Environment Variables:**

   - Add your API keys in the Render dashboard using the environment variable settings (or upload them via your `.env` file using Render's secret files feature).

4. **Deploy:**

   Once configured, trigger a deploy. Your backend will be available at a public URL (e.g., `https://your-backend.onrender.com/chat`).

#### Deploying the Frontend on Streamlit Community Cloud

1. **Push Your Code to GitHub:**  
   Ensure that the repository (or a branch) containing `frontend.py` is available.

2. **Create a New App on Streamlit Cloud:**

   - Connect your GitHub repository.
   - Set up any necessary secrets using Streamlit's secrets management (if needed).

3. **Update API URL:**

   - In `frontend.py`, update `API_URL` to point to your deployed backend URL (e.g., `https://your-backend.onrender.com/chat`).

4. **Deploy:**

   Your Streamlit app will automatically build and deploy on the community cloud.

## (Optional) Project Structure

Including a project structure can help others understand your code organization. Below is an example structure:

```
AI_ChatBot/
├── AGENTIC_CHATBOT/
│   ├── backend.py       # FastAPI backend application
│   ├── frontend.py      # Streamlit frontend application
├   └── requirements.txt # Python dependencies
└── .env                 # Environment variables (not tracked in Git)

