import os
import random
import time
import uuid
import webbrowser

import playsound
import segno
import speech_recognition as sr
from gtts import gTTS


def respond(text):
    print("Assistant:", text)

    filename = f"Speech_{uuid.uuid4()}.mp3"

    try:
        tts = gTTS(text=text, lang="en")
        tts.save(filename)
        playsound.playsound(filename)

    except Exception as e:
        print("Voice error:", e)

    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except OSError:
                pass


def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                phrase_time_limit=10
            )

    except Exception as e:
        print("Microphone error:", e)
        return ""

    try:
        data = recognizer.recognize_google(audio)

        print("You said:", data)

        return data.lower().strip()

    except sr.UnknownValueError:
        print("I couldn't understand you.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""

    except Exception as e:
        print("Speech recognition error:", e)
        return ""


def number_game():
    respond("Let's play the number guessing game.")

    number = random.randint(1, 10)

    print("\nGuess a number between 1 and 10.")
    respond("Guess a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            if guess == number:
                respond("Correct! You win!")
                break

            if guess < number:
                print("Wrong guess. Try a higher number.")
            else:
                print("Wrong guess. Try a lower number.")

            another = input("Try again? yes/no: ").lower().strip()

            if another != "yes":
                respond(
                    f"Okay. The correct number was {number}."
                )
                break

        except ValueError:
            print("Invalid input! Please enter a number.")


def rock_paper_scissors():
    respond("Let's play Rock Paper Scissors.")

    choices = ["rock", "paper", "scissors"]

    while True:
        p1 = input(
            "Enter Rock, Paper, or Scissors: "
        ).lower().strip()

        if p1 not in choices:
            respond(
                "Invalid choice. Please choose rock, paper, or scissors."
            )
            continue

        p2 = random.choice(choices)

        print(f"\nYou chose: {p1}")
        print(f"p2 chose: {p2}")

        respond(
            f"You chose {p1}. "
            f"I chose {p2}."
        )

        if p1 == p2:
            respond("It's a tie!")

        elif (
            (p1 == "rock" and p2 == "scissors")
            or
            (p1 == "paper" and p2 == "rock")
            or
            (p1 == "scissors" and p2 == "paper")
        ):
            respond("You win!")

        else:
            respond("I win!")

        again = input(
            "\nDo you want to play again? yes/no: "
        ).lower().strip()

        if again != "yes":
            respond("Okay. Thanks for playing!")
            break


def create_qr():
    respond(
        "Tell me the text or URL you want to convert into a QR code."
    )

    data = input("Enter text or URL: ").strip()

    if not data:
        respond("You did not enter any text.")
        return

    try:
        qr = segno.make(data)

        qr.save(
            "qrcode.png",
            scale=10
        )

        print("QR Code created successfully!")
        print("Saved as: qrcode.png")

        respond("QR code created successfully.")

    except Exception as e:
        print(f"Error creating QR code: {e}")
        respond("Sorry, I couldn't create the QR code.")


def open_website(data):
    if "youtube" in data:
        respond("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
        return True

    elif "whatsapp" in data:
        respond("Opening WhatsApp.")
        webbrowser.open("https://web.whatsapp.com")
        return True

    elif "google maps" in data or "maps" in data:
        respond("Opening Google Maps.")
        webbrowser.open("https://www.google.com/maps")
        return True

    elif "google" in data:
        respond("Opening Google.")
        webbrowser.open("https://www.google.com")
        return True

    return False


def handle_command(data):
    if not data:
        return True

    if "how are you" in data:
        respond("I'm fine, Rama. How are you?")
        return True

    elif "what are your plans" in data:
        respond("My plan is to help you get a good job.")
        return True

    elif "time" in data:
        current_time = time.strftime("%I:%M %p")
        respond(
            f"The current time is {current_time}."
        )
        return True

    elif "number game" in data:
        number_game()
        return True

    elif (
        "rock paper scissors" in data
        or "rock paper scissor" in data
        or "play rock paper scissors" in data
        or "play rock paper scissor" in data
    ):
        rock_paper_scissors()
        return True

    elif "qr code" in data:
        create_qr()
        return True

    elif (
        "stop talking" in data
        or "goodbye" in data
        or "exit" in data
    ):
        respond("Okay Rama. Goodbye!")
        return False

    elif open_website(data):
        return True

    else:
        respond(
            "Sorry, I don't understand that command."
        )
        return True


def virtual_assistant():
    respond(
        "Hi Rama. I am your virtual assistant. "
        "Tell me what you want to do."
    )

    listening = True

    while listening:
        data = listen()

        if data:
            listening = handle_command(data)
        else:
            print("Waiting for your command...")


if __name__ == "__main__":
    virtual_assistant()
