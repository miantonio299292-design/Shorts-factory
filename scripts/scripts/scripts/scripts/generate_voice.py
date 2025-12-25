from gtts import gTTS
import uuid
import os

def generate_voice(text):
    os.makedirs("temp", exist_ok=True)
    filename = f"temp/{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang="pt")
    tts.save(filename)
    return filename
  
