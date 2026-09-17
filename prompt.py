'''
gTTS --> Google text to speech
playsound --> pip install playsound==1.2.2
pyaudio --> pip install pyaudio

3 functions:
Listen (SpeechRecognition)
respond (gtts)
assistant (conditions) --> conversation,greeting,datetime,locate a place,open a browser, play a youtube video
'''

'''
text = gTTS("Hello ekanth, what are u doing?")
text.save("audio.mp3")
playsound.playsound("audio.mp3")
'''
#imort the libraries
from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os

#let us create listen function
def listen():
    """Function for Speech Recognition"""
    r = sr.Recognizer()
    #we will take micro phone as source
    with sr.Microphone() as source:
        print("Ika modaledadamma")
        audio = r.listen(source,phrase_time_limit = 10)
    #we need to give our text as voice
    data = ""
    #here we will give exceptions (try,except)
    try:
        data = r.recognize_google(audio)
        print("You said: ",data)
    except sr.UnknownValueError as e:
        print("Request Failed")
    except sr.RequestError as e:
        print("sariga matladu , nuvvu chepindi ardhamkale")
    return data

def respond(String):
    """Function to respond back"""
    print(String)
    tts = gTTS(String)
    tts.save("Speech.mp3")
    #we are using uuid --> to randomize the content in the
    #audio file
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#here we will amke our virtual assistant into action

def va(data):
    """Our Virtual Assistant with the actions"""
    if "how are you" in data:
        listening = True
        respond("I'm fine, nuvvu ala vunav")
    elif "what are your plans" in data:
        listening = True
        respond(" manchi job ravali ")
    elif "time" in data:
        listening = True
        respond(time.ctime())
    elif "stop talking" in data:
        listening = False
        respond("sare malli kaludham emundile")
    elif "open YouTube" in data:
        listening = True
        respond("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open WhatsApp" in data:
        listening = True
        respond("Opening Whatsapp")
        webbrowser.open("https://web.whatsapp.com")
    elif "open Google" in data:
        listening = True
        respond("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open maps" in data:
        listening = True
        respond("Opening Maps")
        webbrowser.open("https://www.google.com/maps")
    try:
        return listening
    except UnboundLocalError as e:
        print("sariga matladu koncham")
        
respond("hi rama .. , chepu em chedham")
listening = True
while listening:
    data = listen()
    print(data)
    listening = va(data)
