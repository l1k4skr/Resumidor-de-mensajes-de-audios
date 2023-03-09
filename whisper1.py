import openai
import os

openai.api_key = "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"


def listening(audioMp3):
    audio = open(audioMp3, "rb")
    transcription = openai.Audio.transcribe("whisper-1", audio)
    return transcription.text


def resume(text):
    roles = ["user", "system", "assistant"]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": roles[0], "content": f"Resume esto: {text}"},
        ]
    )
    return response.choices[0].message['content'].lstrip()



# print(resume(listening("audios/audioAng2.mp3")))
if __name__ == "__main__":
    nombre = input("Nombre del archivo con extension: ")
    nombre_ex = "audios/"+nombre
    path = os.getcwd()
    file_path = os.path.join(path+"/AudiosTXT", f"{nombre}.txt")
    with open(file_path, "w", encoding="UTF-8") as file:
        text = listening(nombre_ex)
        file.write(text)
    file_path = os.path.join(path+"/resumenes", f"{nombre}_resumen.txt")

    with open(file_path, "w", encoding="UTF-8") as res:
        res.write(str(resume(text)))
