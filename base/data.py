import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
# engine.setProperty('voice', voices[29].id)
# engine.setProperty('speed',)
engine.setProperty('rate',110)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

comment_datas = {"hello":["hi","hello","hi,how are you"],
                     "hi":['hi','hello','how are  you'],
                     'i love you':"i'm alredy in a relationship",
                     'with whom':'With You',
                     'who developed you':'by the team hogwarts',
                     'who is cringe in world':'no one except you',
                     'do you like to watch movie':'I wont watch but i can suggest you...',
                     'Do i look beautiful':'yes ofcourse',
                     'who is elon musk':'he is the ceo of tesla',
                     'how many languages do you know':'i know more languages than you',
                     'how well are your in maths ':'i can solve any problems',
                     "which country won 2018 world cup?" :'france',
                     'does monalisa have eyebrows': 'monalisa has no eyebrows',
                     'how many words are there in english?' : "171,476' words",
                     'which is the longest river?' : 'nile',
                     'who discovered solar system' :'copernicus',
                     'who developed python' :'guido van rossum',
                     'how old is the sun?' :"4.603 billion years",
                     'which animal milk is black?' :'female rhinoceros',
                     'which is the laziest day of the week' : 'monday',
                     'what is the lonliest number?' :"1",
                     'what is the most used world word': 'the',
                     'which is the easiest programming language?': 'python',
                     'which is the most intelligent animal after human ': 'dolphin',
                     'how many seconds  are there in a year': "31,556,926",
                     'who is the ceo of google' : 'mr sundar pichai',
                     'where the word google comes from? ':'googol',
}

def convo(qustion):
    speak(comment_datas[qustion])
