#libraries
import ollama as ai
import pyttsx3
import speech_recognition as sr
from datetime import datetime as dt

#variables
engine = pyttsx3.init()
r = sr.Recognizer()
time = None
response = None
answer = None

while True:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Okay, say something!")

        # Listen for the user's input
        audio = r.listen(source)

    # 3. Recognize the speech
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        response = ai.chat(model="llama3.2:1b", messages=[{"role": "user", "content": text}])
        answer = response['message']['content']
        print(answer)
        engine.say(answer)
        engine.runAndWait()

    except Exception as e:
        print("error")

    finally:
        print("done")

