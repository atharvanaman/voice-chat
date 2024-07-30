import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        process_query(query)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Sorry, I'm having trouble recognizing your voice.")

def process_query(query):
    # Implement your logic for processing user queries here
    # You can use if-else statements, natural language processing, or other techniques

    # Example: Simple greeting response
    if "hello" in query:
        respond("Hello! How can I assist you?")
    elif "goodbye" in query:
        respond("Goodbye!")

def respond(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    listen()
