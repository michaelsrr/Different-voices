from gtts import gTTS
import os

text = "Hola Andrés qué más qué hace todo bien o qué"

language = "es" 

speech = gTTS(text = text, lang = language, slow = False)

speech.save("texto.mp3")

os.system("start texto.mp3")
