import os
from gtts import gTTS
import pyttsx3


class Text2Speech():
    def __init__(self, method):
        self.text = ''
        self.method = method

    def speak(self, text):
        self.text = text
        if self.method == 'pyttzx3':
            self.pyttsx3_engine()
        elif self.method == 'google':
            self.gTTS_engine()

    def pyttsx3_engine(self):
        print("Roxy --> ", self.text)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 140)
        engine.say(self.text)
        engine.runAndWait()

    def gTTS_engine(self):
        speaker = gTTS(text=self.text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3")  #if you have a macbook->afplay or for windows use->start
        # os.remove("res.mp3")
