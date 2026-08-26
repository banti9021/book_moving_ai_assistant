from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.chatbot import get_bot_response
from backend.database import create_database


app = FastAPI(
    title="Moving AI Agent",
    description="AI Moving Reservation Chatbot",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


create_database()


@app.get("/")
def home():

    return {
        "message": "Moving AI Agent is running!"
    }


@app.get("/health")
def health():

    return {
        "status": "OK"
    }


@app.post("/chat")
def chat(
    message: str,
    session_id: str = "default"
):

    response = get_bot_response(
        session_id,
        message
    )

    return {
        "session_id": session_id,
        "user_message": message,
        "bot_response": response
    }