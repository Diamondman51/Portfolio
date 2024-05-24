from PySide6.QtCore import QThread
import pyttsx3

class Read_thread(QThread):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.setProperty('volume', 1)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(self.text)
        engine.runAndWait()