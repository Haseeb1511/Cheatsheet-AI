import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining....")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("your said :",text)
            return text
        except sr.UnknownValueError:
            print("sorry could not hear")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

def llm(text):
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")  # must match exactly
    response = model.generate_content(text)
    return response.text

def text_to_speech(text):
    tts = gTTS(text=text,lang="en")
    tts.save("speech.mp3")


# models = genai.list_models()
# for m in models:
#     print(m.name, m.supported_generation_methods)

