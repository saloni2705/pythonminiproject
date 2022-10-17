import googletrans
import speech_recognition as sr
import pyaudio
import pyttsx3

recognizer = sr.Recognizer()
translator = googletrans.Translator()
engine = pyttsx3.init()

#for microphone
try:
    with sr.Microphone() as source:
        print('Speak now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice)
        print(text)

except :
   print('speak again')

#for translation
langinput = input('Type the language you want to convert:')
translated = translator.translate(text,langinput)

print(translated.text)
