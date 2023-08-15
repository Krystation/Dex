import requests

from decouple import config

ELEVEN_LABS_KEY = config("ELEVEN_LABS_KEY")

def convert_text_to_speech(message):
    body = {
        "text": message,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": .15,
            "similarity_boost": .7
        }
    }

    voice_dex = "XxAi7JopeFxuS44x948s"

    headers = {"xi-api-key": ELEVEN_LABS_KEY, "Content-Type": "application/json", "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_dex}"
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        return
    if response.status_code == 200:
        return response.content
    else:
        return