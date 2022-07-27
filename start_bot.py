from typing import Text
import numpy as np
import os
from io import BytesIO
import transformers
from speech2text import Speech2Text
from text2speech import Text2Speech


class ChatBot():
    def __init__(self, name):
        print(f"---Starting up {name}---")
        self.name=name
        self.text = ''
    def wake_up(self, text):
        print(text)
        return True if self.name in text.lower() else False



if __name__ == "__main__":
    print('Rock on')
    ai = ChatBot(name="roxy")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    S2T = Speech2Text(recognizer_name = 'google')
    T2S = Text2Speech(method = 'pyttzx3')
    while True:
        input_query = S2T.speech_to_text()
        if ai.wake_up(input_query) is True:
            initial_res = "Hello, what can I do for you?"
            T2S.speak(initial_res)
            while True:
                input_query = S2T.speech_to_text()

                if 'shutdown' in input_query.lower() or 'shut down' in input_query.lower():
                    T2S.speak('Thank you. Cheers')
                    exit()

                ## conversation
                else:
                    if 'name' in input_query.lower():
                        T2S.speak("I'm roxy your personal assistant")
                    else:
                        chat = nlp(transformers.Conversation(input_query), pad_token_id=50256)
                        res = str(chat)
                        res = res[res.find("bot >> ")+6:].strip()
                        T2S.speak(res)
