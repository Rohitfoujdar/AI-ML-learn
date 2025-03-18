# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":  # Corrected: Two underscores
#     speak("Initializing jarvis...")
#     while True:
#         #listen for the wake word "Jarvis"
#         # obtain audio from the microphone
#         r = sr.Recognizer()

#         # recognize speech using Sphinx
#         print("recognizing...")
#         try:
#             with sr.Microphone() as source:
#                print("Listening...")
#                r.adjust_for_ambient_noise(source, duration=1)
#                audio = r.listen(source, timeout=5, phrase_time_limit=3)
#             command = r.recognize_google(audio)  # Corrected method name
#             print(command)
#         except sr.RequestError as e:
#             print("error; {0}".format(e))

# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     print(c)


# if __name__ == "__main__":  
#     speak("Initializing Jarvis...")
#     while True:
#         print("Recognizing...")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
#                 audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

#             word = recognizer.recognize_google(audio)  
#             if(word.lower() == "jarvis"):
#                 speak("Yes sir")
#                 #Listen for command
#                 with sr.Microphone() as source:
#                     print("Jarvis active...")
#                     audio = recognizer.listen(source,  timeout=5, phrase_time_limit=3)
#                     command = recognizer.recognize_google(audio)  
#                     processCommand(command)
#         except sr.UnknownValueError:
#             print("I could not understand your voice, please try again.")
#         except sr.RequestError:
#             print("Could not connect to Google, please check your internet connection.")

import speech_recognition as sr
import pyttsx3
import webbrowser
import music_library

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    # Add your command processing logic here
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
        speak("Opening YouTube")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com/")
        speak("Opening facebook")
    elif "open github" in command.lower():
        webbrowser.open("https://www.github.com/")
        speak("Opening github")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        print("_________command--", command, song)
        link = music_library.music[song]
        webbrowser.open(link)
    elif "stop" in command.lower() or "exit" in command.lower():
        speak("Goodbye sir, shutting down")
        exit()  # Exit the program

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=2)  # Reduce background noise
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            word = recognizer.recognize_google(audio, language="en-IN")  # Use English (India)
            if "jarvis" in word.lower():
                speak("Yes sir")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active... Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio, language="en-IN")
                    processCommand(command)
        except sr.UnknownValueError:
            print("I could not understand your voice, please try again.")
            speak("I could not understand your voice, please try again.")
        except sr.RequestError:
            print("Could not connect to Google, please check your internet connection.")
            speak("Could not connect to Google, please check your internet connection.")