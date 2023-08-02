#uvicorn main:app --reload
#Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from dotenv import load_dotenv
import openai
import os

#Initiate App
app = FastAPI()

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_KEY")
url = "https://api.elevenlabs.io/v1/text-to-speech/XxAi7JopeFxuS44x948s"

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
# ...


@app.get("/openai")
async def root():
    resp = {"role": "user", "content": "What is your purpose?"}
    return resp

#Posting bot response
#@app.post("/post-audio/")
#async def post_audio(file: UploadFile = File(...)):
#    print("hello")

