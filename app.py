from moviepy.editor import *
from dotenv import load_dotenv 
import whisper
import openai
import os

def audio_to_text():
    model=whisper.load_model("base")
    result=model.transcribe("audio.mp3")
    with open("transcription.txt","w")as f:
        f.write(result["text"])

        
def video_to_text():
    video_file="video.mp4"
    audio_file="audio.mp3"
    video_clip=VideoFileClip(video_file)
    audio_clip=video_clip.audio
    audio_clip.write_audiofile(audio_file)
    audio_clip.close()
    video_clip.close()

load_dotenv()
ak=os.getenv("API_KEY")
openai.api_key=ak
def create_header(prompt):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
         "role": "user",
         "content": prompt,
         }
        ]
    )
    return completion.choices[0].message.content.strip()

if __name__=="__main__":
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        response=create_header(user_input)
        print("Chatbot: ",response)