import whisper
import openia
import os

openai.api_key = os.getenv("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")
def listening(audioMp3, modelType):
    model = whisper.load_model(modelType)
    result = model.transcribe(audioMp3)
    return result["text"]
def resume(text):
    return openai.Completion.create(model="text-davinci-003", promp = f"Resume este mensaje de voz: {text}", max_tokens=100, temperature=0.6, top_p=1, frequency_penalty=0.0, presence_penalty=0.6)



if __name__ == "__main__":
    nombre = input("Nombre del archivo: ")
    nombre_ex = nombre + ".mp3"
    with open(f"{nombre}.txt", "w") as file:
        text = listening(nombre_ex, "medium")
        file.write(text)
        print(resume(text))
