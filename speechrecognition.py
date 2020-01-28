import speech_recognition as sr
def parler():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('speak anything : ')
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio,language='fr-FR')
            print('you said : {}'.format(text))
            return text
        except:
            print("sorry could not recognize your voice")
            return "désolé je n'ai pas bien compris"