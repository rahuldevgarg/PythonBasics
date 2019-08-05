"""This is Speech Recognition using python"""
import speech_recognition as s
a = s.Recognizer()
with s.Microphone() as source:
    print("Speak Anything")
    audio = a.listen(source)
    try:
        text = a.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print("Couldn't recognize")
