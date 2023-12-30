import speech_recognition as sr
import pyttsx3
import os

r= sr.Recognizer()







def Speak(command):
    too = pyttsx3.init()
    too.say(command)
    voice = too.getProperty('voices')
    too.setProperty('voice',voice[0].id)
    too.runAndWait()

while True:

    

    with sr.Microphone() as source2:
        print("Getting_Noise......")
        r.adjust_for_ambient_noise(source2,duration=1)
        print("Listening......")

        audio2 = r.listen(source2)

        myword = r.recognize_google(audio2)
        mw = myword.lower()


        print("You : " + mw)
        if "16" in mw:
            dir = "\\Voices\\Proxy_16"
            songs = os.listdir(dir)
            print(songs)
            os.startfile(os.path.join(dir,songs[1]))

