import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

from utils.nlp_utils import process_command

# Initialize recognizer + TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio and convert to text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand.")
            return ""
        except sr.RequestError:
            speak("Network error. Try again later.")
            return ""

def main():
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        query = listen()
        if "exit" in query or "quit" in query:
            speak("Goodbye!")
            break
        process_command(query, speak)

if __name__ == "__main__":
    main()
