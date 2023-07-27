from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_KEY")
url = "https://api.elevenlabs.io/v1/text-to-speech/<voice-id>"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": os.getenv("ELEVEN_LABS_KEY")
}

app = FastAPI()

origins = ["*", "http://127.0.0.1:8000/", "http://localhost:3000/"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_response():
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0.2,
        max_tokens = 1000,
        messages = [
            {"role": "system", "content": "You are a pokedex. You are here to help me win battles and identify which pokemon from my team i should use."},
            {"role": "user", "content": "What is your purpose?"},
        ]
    )
    print(response.choices[0].message)
    return(response.choices[0].message.content)

@app.get("/openai")
async def root():
    resp = get_response()
    return resp

#@app.post("/post-audio/")
#async def post_audio(file: UploadFile = File(...)):
#    print("hello")