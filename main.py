import speech_recognition as sr
import pyttsx3
import os
import webbrowser
from datetime import datetime

# Text-to-speech setup
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Take voice input from microphone
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Could not understand your voice. Try again.")
        return "None"
    return query.lower()

# Map commands to actions
def perform_task(query):
    if "open notepad" in query:
        speak("Opening Notepad")
        os.system("notepad")
    
    elif "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif "what is the time" in query or "tell me time" in query:
        time = datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
    
    elif "exit" in query or "quit" in query:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your voice assistant.")
    while True:
        query = take_command()
        if query != "None":
            perform_task(query)