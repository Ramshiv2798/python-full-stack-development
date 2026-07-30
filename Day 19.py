import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception:
        print("Sorry, please say that again.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning \nI am your Virtual Assistant")

    elif hour < 18:
        speak("Good Afternoon \nI am your Virtual Assistant")

    else:
        speak("Good Evening \nI am your Virtual Assistant")


wish_user()


while True:

    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com/in/srirama-ganesh-korubilli-045924267/")   


    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 2)
        print(info)
        speak(info)

    elif "exit" in command:
        speak("Goodbye")
        break





















