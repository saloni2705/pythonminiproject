import googletrans
import speech_recognition as sr


recognizer = sr.Recognizer()
translator = googletrans.Translator()


try:
    with sr.Microphone() as source:
        print('Speak now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice)
        print(text)

except:
    print('speak again')

translated = translator.translate(text , dest='en')
print(translated.text)

print(googletrans.LANGUAGES)

