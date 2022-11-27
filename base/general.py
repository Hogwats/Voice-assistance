import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import pyaudio 


def takeconvo():
                    #It takes microphone input from the user and returns string output

                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Listening For The Query")
                        r.pause_threshold = 1
                        audio = r.listen(source)

                    try:
                        print("Recognizing...")
                        conver = r.recognize_google(audio, language='en-in')
                        print(f"User said: {conver}\n")

                    except Exception as e:
                        # print(e)
                        print("Say that again please...")
                        return "None"
                    return conver
def ytvideo():
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Listening For The Query")
                        r.pause_threshold = 1
                        audio = r.listen(source)

                    try:
                        print("Recognizing...")
                        ytquery = r.recognize_google(audio, language='en-in')
                        print(f"User said: {conver}\n")

                    except Exception as e:
                        # print(e)
                        print("Say that again please...")
                        return "None"
                    return ytquery
    
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('speed',1)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()
 
