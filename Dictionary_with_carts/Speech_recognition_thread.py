from PySide6.QtCore import QThread, Signal

import speech_recognition as sr

class Speech_recognition_thread(QThread):
    signal = Signal(str)
    start = Signal()
    end = Signal()
    def __init__(self):
        super().__init__()

    def run(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as mic:
                self.start.emit()
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, language='en-US')
                print(text)
                self.signal.emit(text)
        except sr.UnknownValueError:
            self.signal.emit('Google could not understand audio')
        except sr.RequestError as error:
            self.signal.emit("Google error: {0}".format(error))
        finally:
            self.end.emit()