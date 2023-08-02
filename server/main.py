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
origins = ["http://127.0.0.1:8000/", "http://localhost:3000/"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#custom functions
from functions.openai_requests import convert_audio_to_text


@app.get("/openai")
async def root():
    resp = {"role": "user", "content": "What is your purpose?"}
    return resp

@app.get("/post-audio-get/")
async def get_audio():
    audio_input = open("voice.mp3", "rb")
    message = convert_audio_to_text(audio_input)
    print(message)
    return "Done"

#Posting bot response
#@app.post("/post-audio/")
#async def post_audio(file: UploadFile = File(...)):
#    print("hello")

