#custom package

import datetime
from base.general import  *
from base.activaty import ( sendEmail, wiki, 
                           play_song, time_now, send_mail, conversation,weather )
from base.data import convo

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import pyaudio
import pywhatkit as py

#pip packages
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('speed',1)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Your Personal Voice Assistant Team HogWards. Please tell me how may I help you")

    
    
if __name__ == "__main__":
    wishMe()
    msg = "hello"
    conversation(msg)
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            wiki(query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music from youtube' in query:
            play_song()
            
        elif 'the time' in query:
            time_now()

        elif 'open code' in query:
            codePath = "D:\\voice assisstant\\voice.py"
            os.startfile(codePath)

        elif 'send email' in query:
            send_mail()
        elif 'weather' in query:
        	weather()
        elif  'conversation' in query:
            while True:            
                speak('Lets start conersation')
                conves =  takeconvo().lower()
                convo(conves)
                

        elif  'play on youtube' in query:
            video = ytvideo.lower()
            py.playonyt(video)
            
        elif 'shutdown' or 'exit' or 'stop' in query:
            speak("Good Bye We Will Talk Later")
            exit()
        else:
            speak("I Can't Able To Understand What You Are Speaking ")