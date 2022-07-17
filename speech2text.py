import speech_recognition as sr


class Speech2Text():
    def __init__(self, recognizer_name):
        self.recognizer_name = recognizer_name
        self.recognizer = self.get_recognizer()
        self.text = ''

    def get_recognizer(self):
        if self.recognizer_name == 'google':
            return sr.Recognizer()


    def speech_to_text(self):
        
        with sr.Microphone() as mic:
            print("listening...")
            audio = self.recognizer.listen(mic)
        try:
            self.text = self.recognizer.recognize_google(audio)
            print("me --> " + self.text)
            return self.text
        except:
            print("me -->  ERROR")
            return self.text