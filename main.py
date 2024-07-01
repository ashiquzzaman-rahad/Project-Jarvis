import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import musiclibrary
from dotenv import load_dotenv
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif 'news' in c.lower():
        r = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={os.getenv('NEWSAPI')}')
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    

if __name__ == '__main__':
    load_dotenv()
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing...")
        #recognize speech using sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == 'jarvis':
                speak("Yes!")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            print("could not understand audio.")
        except Exception as e:
            print(f"error: {e}")