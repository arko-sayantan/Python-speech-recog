import pyttsx3  # python text to speech version 3 its convert text form speech.
import speech_recognition as lis # as use for renaming or surname.

lisn = lis.Recognizer() # Creat a object of lis
speaker = pyttsx3.init() # creat a object of pyttsx3
print('Talk with me!')
speaker.say('Talk with me!') #.say() --> use for speech the text
speaker.runAndWait()    
try:
    with lis.Microphone() as source:
        print('listening...')
        voice = lisn.listen(source)
        info = lisn.recognize_google(voice)
        print('I listen -->\n',info.upper())
        speaker.say(info)
        speaker.runAndWait()
except:
    pass
name = 0
