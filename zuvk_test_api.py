import os
import openai
import locale

locale.setlocale(locale.LC_ALL, 'hr_HR.UTF-8')

os.environ["OPENAI_API_KEY"] = "tvoj_api_key"
openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file= open("OpenAi/audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

with open("transcript.txt", "w", encoding='utf-8') as f:
    f.write(transcript.text)