#libraries
import ollama as ai
import pyttsx3
import speech_recognition as sr
import playsound

#variables
engine = pyttsx3.init()
r = sr.Recognizer()
time = None
response = None
answer = None
r = sr.Recognizer()
trigger = ""

def main_part(source):
    audio = r.listen(source, phrase_time_limit=3)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        response = ai.chat(model="llama3.2:1b", messages=[{"role": "user", "content": text}], options={
            "num_predict" : 60,
            "temperature" : 0.47
        })
        answer = response['message']['content']
        print(answer)
        engine.say(answer) #speaks the response
        engine.runAndWait()

    except sr.UnknownValueError: #error handling
        engine.say("Sorry, I cannot understand")
        engine.runAndWait()

    except Exception as e:
        print(f"error {e}")

    finally:
        print("done")

def wake_up():
    global trigger
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source,duration= 2)
        print("adjustment done")

        while True:
            try:
                audio = r.listen(source, timeout=1, phrase_time_limit=3)
                audio_text = r.recognize_google(audio).lower()

                if trigger in audio_text:
                    playsound.playsound("effect.wav")
                    main_part(source)
            except (sr.UnknownValueError, sr.WaitTimeoutError):
                continue

            except Exception as e:
                print(f"error{e}")

def trigger_setup():
    global trigger
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source,duration= 2)
        print("speak your desired trigger word now")
        playsound.playsound("effect.wav")
        trigger_sound = r.listen(source, timeout=1, phrase_time_limit=3)
        trigger = r.recognize_google(trigger_sound).lower()

trigger_setup()
wake_up()