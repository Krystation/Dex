#. venv/bin/activate 
#uvicorn main:app --reload
#Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai
#import os

#Initiate App
app = FastAPI()

#url = "https://api.elevenlabs.io/v1/text-to-speech/XxAi7JopeFxuS44x948s"

#CORS
origins = ["*", "http://127.0.0.1:8000/", "http://localhost:3000/"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#custom functions
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech


@app.get("/openai")
async def root():
    resp = {"role": "user", "content": "What is your purpose?"}
    return resp

@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "Conversation Reset"}

@app.get("/post-audio-get/")
async def get_audio():
    audio_input = open("voice.mp3", "rb")
    message = convert_audio_to_text(audio_input)
    if not message:
        return HTTPException(status_code=400, detail="Failed to transcribe audio")

    chat_response = get_chat_response(message)
    if not chat_response:
        return HTTPException(status_code=400, detail="Failed to get chat response")

    store_messages(message, chat_response)

    audio_output = convert_text_to_speech(chat_response)
    if not audio_output:
        return HTTPException(status_code=400, detail="Failed to get response from Eleven Labs")

    def iterfile():
        yield audio_output

    return StreamingResponse(iterfile(), media_type="audio/mpeg")

    return "Done"

#Posting bot response
#@app.post("/post-audio/")
#async def post_audio(file: UploadFile = File(...)):
#    print("hello")

