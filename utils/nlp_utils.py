import datetime
import webbrowser
import os

def process_command(query, speak):
    """Basic intent handling."""
    if "time" in query:
        speak(f"The time is {datetime.datetime.now().strftime('%H:%M')}")
    elif "date" in query:
        speak(f"Today is {datetime.datetime.now().strftime('%d %B %Y')}")
    elif "open youtube" in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open google" in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    else:
        speak("I am not sure how to handle that yet.")
