import speech_recognition as sr
import pyttsx3

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble accessing the speech recognition service.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = "12:00 PM"  # Replace with actual time retrieval code
        speak(f"The current time is {current_time}.")
    else:
        speak("I'm sorry, I can't help with that.")

# Main loop
while True:
    command = listen().lower()
    process_command(command)
