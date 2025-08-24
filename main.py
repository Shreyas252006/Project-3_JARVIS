import speech_recognition as sr
import webbrowser
import pyttsx3          # gTTS is from google. but only few free trails and after that paid API is required ( Use for Large scale to look professional and use it on large scale.)
import winsound
import pygame   
import musicLIbrary

speak = sr.Recognizer()
engine = pyttsx3.init()
pygame.mixer.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
# To open Websites
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "take me to code with harry channel" in c.lower():
        webbrowser.open("https://www.youtube.com/CodeWithHarry")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")

    # To play music
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLIbrary.music[song]
        webbrowser.open(link)
    
    else:
        # Let openAI handle the request
        pass



def beep():
    beep_sound = pygame.mixer.Sound(pygame.mixer.Sound('beep-07a.wav'))  # Make sure you have a '   .wav' file in the same folder
    beep_sound.play()

if __name__=="__main__":
    speak("Hello.")
    # winsound.Beep(1000, 500)
    beep()
    while True: 
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Google
        print("Recognizing....")
        beep()
        try:
            with sr.Microphone() as source:
                print("Listenining....")
                audio = r.listen(source, timeout=4, phrase_time_limit=2)

            word =  r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("Yaa...")
                # Listen for command
                with sr.Microphone() as source:
                    beep()
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    # For opening links and Music play (For now.)
                    processCommand(command) 


        except Exception as e:
            print("Error; {0}".format(e))