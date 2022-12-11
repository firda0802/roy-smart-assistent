import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import webbrowser
import time
from selenium import webdriver
from time import sleep

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening ......")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)
    return data

def response(text):
    print(text)

    tts = gTTS(text=text, lang="en")
    audio ="Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)
    os.remove(audio)

def call(text):
    action_call = "Assistant"
    text = text.lower()
    if action_call in text:
        return True
    return False

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return f'Today is {week_now}, {months[month_now -1]} the {ordinals[day_now -1]}.'

def say_hello(text):
    great =  ["hi", "Hello mam", "Hello sir", "Hola", "greetings", "wassup", "hello", "howdy", "what's good", "hey there"]
    response = ["hi", "Hello mam", "Hello sir", "Hola", "greetings", "wassup", "hello", "howdy", "what's good", "hey there"]

    for word in text.split():
        if word.lower() in great:
            return random.choice(response) + "."
    return ""

def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]

while True:
    try:
        text = rec_audio()
        speak = " "

        if call(text):
            speak = speak + say_hello(text)
            if "date" in text or "day" in text or "month" in text :
                get_today = today_date()
                speak = speak + " " + get_today
            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = " "
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour
                if now.minute < 10:
                    minute = "0" +str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."
            elif "who are you" in text or "define yourself" in text:
                speak = speak + """Hello i am your life assistant and you can call me roy.
                please order me according to your needs or become your confidant, I am very willing"""
            elif "what's your name" in text:
                speak = speak + "my name is Robot Roy"
            elif "who am I" in text:
                speak = speak + "you must probably be a human"
            elif "what do you like" in text:
                speak = speak + "I really love to eat as much as it has made me. I really like spicy meatballs"
            elif "why do you exist" in text or "why did you come" in text:
                speak = speak + "It is a secret"
            elif "how are you" in text:
                speak = speak + "I am fine, thank you"
                speak = speak + "\nHow are you?"
            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that you are fine"
            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Opening Google Chrome"
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )
                elif "share it" in text.lower():
                    speak = speak + "Opening Share It"
                    os.startfile(
                        r"E:\FILE_SHAREIT\SHAREit\SHAREit.exe"
                    )
                elif "vs code" in text.lower():
                    speak = speak + "Opening visual studio code"
                    os.startfile(
                        r"C:\Users\user\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                    )
                elif "youtube" in text.lower():
                    speak = speak + "Opening  Youtube"
                    webbrowser.open("https://youtube.com/")
                elif "google" in text.lower():
                    speak = speak + "Opening Google"
                    webbrowser.open("https://google.com")
                elif "stackoverflow" in text.lower():
                    speak = speak + "Opening StackOverFlow"
                    webbrowser.open("https://stackoverflow.com/")
                else:
                    speak = speak + "Application not available"
            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.youtube.com/results?search_query=" +
                    "+".join(search)
                )
                speak = speak + "Opening " + str(search) + "on youtube"
            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?g=" + "+".join(search)
                )
                speak = speak + "Searching" + str(search) + "on google"
            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?g=" + "+".join(search)
                )
                speak = speak + "Searching" + str(search) + "on google"
            elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
                talk("for how many second do you want me to sleep")
                a = int(rec_audio())
                time.sleep(a)
                speak = speak + str(a) + "seconds complated. Now you can ask me anything"
            elif "exit" in text or "quit" in text :
                exit()
            response(speak)
    except:
        talk("I don't know that")