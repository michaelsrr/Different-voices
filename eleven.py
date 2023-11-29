import requests
from dotenv import load_dotenv
import os
from elevenlabs import generate, play, set_api_key, save


load_dotenv()
API_KEY = os.environ.get("ELEVENLABS_API_KEY")
set_api_key(API_KEY)

audio = generate(
    text="Hola Andres y Jeff qué más qué hacen, ¿bien o qué? El nuevo nombre es Sam",
    voice="Sam",
    model='eleven_multilingual_v1'
)
save(
    audio,
     "output.wav")