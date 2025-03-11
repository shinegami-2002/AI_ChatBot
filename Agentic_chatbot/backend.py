from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from typing import List


class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app = FastAPI(title="AI agent") 
@app.get("/")
def read_root():
    return {"message": "Backend is live!"}

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    just an endpoint for ai chatbot
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999) 
