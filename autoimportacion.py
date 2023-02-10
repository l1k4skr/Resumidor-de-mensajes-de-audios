# Description: Autoimportacion de modulos
import pytube 
from main import *

url = input("Ingrese la url del video: ")
yt = pytube.YouTube(url)
audio = yt.streams.filter(only_audio=True).first().download()
text = listening(audio, "large")
print(text)
with open("audio.txt", "wb") as f:
    f.write(text.encode("utf-8"))