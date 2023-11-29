import os

from google.cloud import texttospeech

text = "Hola Andrés qué más qué hace todo bien o qué"
language_code = "es-MX"  # Puedes cambiar esto a "es-AR" u otros códigos de idioma

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=text)

voice = texttospeech.VoiceSelectionParams(
    language_code=language_code, name="es-MX-Standard-A", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.wav", "wb") as out:
    out.write(response.audio_content)

# Reproduce el archivo de audio (puedes usar diferentes métodos dependiendo de tu sistema)
os.system("start output.wav")
