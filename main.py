import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

#Initialize the FastAPI app
app = FastAPI()

#CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Incoming request data
class ChatInput(BaseModel):
    message: str

#API Endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, CityGPT!"}

@app.post("/chat")
def chat(request: ChatInput):
    user_message = request.message
    #Echo back response from user
    reply = f"You asked: '{user_message}'. CityGPT answers: '{user_message}'. CityGPT returns user's messages for demo purposes only."
    return {"reply": reply}