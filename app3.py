#   Kütüphanelerin eklenmesi

from dotenv import load_dotenv
import os
from flask import Flask,render_template,request
from moviepy.editor import *
import time
import whisper
import openai



#   Frontend için Flask tanımlanması

app = Flask(__name__)


#   Sayfa yönlendirmelerinin yapılması

@app.route('/') # Başlangıçtaki yolun belirtilmesi



#   Anasayfanın projeye dahil edilmesi

def index():
    return render_template('index.html')

#   Video dosyasını POST edilmesi ve burada request yapılması

@app.route('/upload',methods=["POST"])

#   Dosyanın işlenmesi ve fonksiyonların çağırılması
def upload():
    if "video" not in request.files:
        return "Video not found in the request"
    
    video=request.files["video"]
    
    if video.filename=="":
        return "No selected file"

    video.save("static/uploaded_video.mp4")
    
    video_to_audio("static/uploaded_video.mp4")
    audio_to_text()
    return render_template("index.html",video_filename="uploaded_video.mp4",text=text_read(),title=create_title(text_read()+ " Bana bu Metin için Bir haber başlığı verir misin? "))



#   Videdan çıkarılan metinin okunması

def text_read():    
    with open("transcription.txt","r")as f:
        text=f.read()
        text=text.split("Bu dizinin betimlemesi")[0]
        return str(text)




      
#   MP3 formatına çevirilen videonun metine dönüştürülmesi

def audio_to_text():
    model=whisper.load_model("base")
    result=model.transcribe("audio.mp3")
    with open("transcription.txt","w")as f:
        f.write(result["text"])
        




#   Videonun işlenebilmesi için mp3 formatına dönüştürülmesi

def video_to_audio(video):
    video_file=f"{video}"
    audio_file="audio.mp3"
    video_clip=VideoFileClip(video_file)
    audio_clip=video_clip.audio
    audio_clip.write_audiofile(audio_file)
    audio_clip.close()
    video_clip.close()





#   Başlık Çıkarma işlemi API kullanımı

load_dotenv()
ak=os.getenv("API_KEY")
openai.api_key=ak
def create_title(prompt):
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




# Programı Hata Ayıklama modunda başlatma 

if __name__ == '__main__':
    app.run(debug=True)
