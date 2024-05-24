import json

import pyttsx3

from difflib import get_close_matches

from PySide6 import QtCore
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox

import speech_recognition as sr

from Read_thread import Read_thread
from Speech_recognition_thread import Speech_recognition_thread
from cart import Cart
from glossary_ui import Ui_MainWindow


class Glossary(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_file()
        self.num = 100
        # self.widget = self.list_widget_for_cart.itemWidget
        # self.widgets = {self.widget(self.list_widget_for_cart.item(item)).title_lbl.tex(): self.widget(self.list_widget_for_cart.item(item)).define_lbl.text() for item in
        #                 range(self.list_widget_for_cart.count())}
        # self.items = [item for item in self.list_widget_for_cart.selectedItems()]
        self.add_first_items()
        self.list_widget_for_cart.itemSelectionChanged.connect(self.put_title_definition)
        self.bnt_read.clicked.connect(self.read_the_text)
        # self.btn_voice.clicked.connect(self.recognize_the_speech_google)
        self.btn_voice.clicked.connect(self.recognize_the_speech_sphinx)
        self.edit_btn.clicked.connect(self.edit_btn_clicked)
        self.add_btn.clicked.connect(self.add_btn_clicked)
        self.delete_btn.clicked.connect(self.detele_choosen_word)
        # self.search_btn.clicked.connect(self.search_btn_clicked)
        self.search_btn.clicked.connect(self.search_btn_clicked)
        self.speech_recognition_thread = Speech_recognition_thread()
        self.read_thread = Read_thread(text=None)

    def recognize_the_speech_sphinx(self):
        if not self.speech_recognition_thread.isRunning():
            self.speech_recognition_thread.start()
        self.speech_recognition_thread.start.connect(lambda: (self.btn_voice.setDisabled(True)))
        self.search_paneli.clear()
        self.speech_recognition_thread.start.connect(lambda: self.label.setText('Started'))
        self.speech_recognition_thread.end.connect(lambda: self.label.setText('Recognized'))
        self.speech_recognition_thread.signal.connect(lambda text: self.search_paneli.setText(text))
        self.speech_recognition_thread.end.connect(self.search_btn_clicked)
        # print(123)
        self.speech_recognition_thread.end.connect(lambda: (self.btn_voice.setDisabled(False)))

        # print(self.speech_recognition_thread.signal())


    def keyPressEvent(self, event: QKeyEvent) -> None:
        # self.search_clicked()
        # print(event.text())
        # print(event.key())
        if event.key() == QtCore.Qt.Key_Enter and self.search_paneli.text():
            self.search_btn_clicked()
            # print(event.key() == QtCore.Qt.Key_Enter)

    def item_to_widget(self):
        item = self.list_widget_for_cart.currentItem()
        widget = self.list_widget_for_cart.itemWidget(item)
        return item, widget

    def read_the_text(self):

        item, widget = self.item_to_widget()

        # engine = pyttsx3.init()
        #
        # # Text to be spoken
        # rate = engine.getProperty('rate')  # getting details of current speaking rate
        # # print(rate)  # printing current voice rate
        # engine.setProperty('rate', 125)  # setting up new voice rate
        #
        # """VOLUME"""
        # volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        # # print(volume)  # printing current volume level
        # engine.setProperty('volume', 1)  # setting up volume level  between 0 and 1
        #
        # """VOICE"""
        # voices = engine.getProperty('voices')  # getting details of current voice
        # # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        # engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        #
        # if self.list_widget_for_cart.currentItem():
        #     engine.say(widget.title_lbl.text())
        # # engine.say('My current speaking rate is ' + str(rate))
        # engine.runAndWait()

        if not self.read_thread.isRunning():
            self.read_thread.text = widget.title_lbl.text()
            self.read_thread.start()

    def recognize_the_speech_google(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as mic:
                audio = recognizer.listen(mic)
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                text = recognizer.recognize_google(audio, language='uz-UZ')
            self.search_paneli.setText(text)
        except sr.UnknownValueError:
            self.search_paneli.setText('Ovozni tanib bo\'lmadi')

    def upload_json(self):
        file = open('data_2.json', 'w')
        json.dump(self.data, file)

    def search_btn_clicked(self):
        # self.widgets = {self.widget(item).title_lbl.tex(): self.widget(item).define_lbl.text() for item in range(self.list_widget_for_cart.count())}
        # self.items = [self.list_widget_for_cart.itemWidget(self.list_widget_for_cart.item(item)) for item in range(self.list_widget_for_cart.count())]
        # self.items = [self.dictt[widget(item).title_lbl.tex()] = widget.define_lbl.text() for item in range(self.list_widget_for_cart.count())]

        # print(self.items)
        # if not self.search_paneli.text():
        #     if self.list_widget_for_cart.count() > 20:
        #         print(self.list_widget_for_cart.count())
            # else:
                # self.list_widget_for_cart.clear()
                # print(self.list_widget_for_cart.count())
                # self.search_btn.clicked.connect(self.add_first_items)
        # else:
        if self.search_paneli.text():
            self.list_widget_for_cart.clear()
            close_words = get_close_matches(self.search_paneli.text(), self.data)
            for word in close_words:
                # print(word)
                self.create_cart(word)


    def create_cart(self, word):
        cart = Cart()
        cart.title_lbl.setText(word)
        cart.define_lbl.setText(self.data[word][:self.num] if len(self.data[word]) < self.num else self.data[word][:self.num] + '...')
        item = QListWidgetItem()
        item.setSizeHint(cart.size())
        self.list_widget_for_cart.addItem(item)
        self.list_widget_for_cart.setItemWidget(item, cart)

    def detele_choosen_word(self):
        item, widget = self.item_to_widget()
        word: str = widget.title_lbl.text().lower()
        del self.data[word]
        # рабочий(удаляет)
        # self.list_widget_for_cart.takeItem(self.list_widget_for_cart.currentRow())
        self.list_widget_for_cart.takeItem(self.list_widget_for_cart.row(item))
        self.upload_json()

        # рабочий(удаляет)
        # self.list_widget_for_cart.takeItem(self.list_widget_for_cart.row())

        msb = QMessageBox()
        msb.information(self, 'Deleted', f'The word {word.title()} was successfully deleted')

        # self.list_widget_for_cart.removeItemWidget(item)

    # тоже работает(удаляет)
    # def detele_choosen_word(self):
    #     item = self.list_widget_for_cart.currentItem()
    #     try:
    #         if item:
    #             widget = self.list_widget_for_cart.itemWidget(item)
    #             word = widget.title_lbl.text().lower()
    #             del self.data[word]
    #             self.list_widget_for_cart.takeItem(self.list_widget_for_cart.row(item))
    #             # self.list_widget_for_cart.removeItemWidget(item)
    #     except Exception as error:
    #         QMessageBox.warning(self, "No Word Selected", error)

    # добавление новых слов в глоссарий(Title, definition)
    def add_btn_clicked(self):
        if self.change_word_structure.text() and self.set_definition.toPlainText():
            if self.change_word_structure.text().lower() not in self.data:
                text = self.set_definition.toPlainText().strip()
                self.data[self.change_word_structure.text().lower().strip()] = text
                cart = Cart()
                cart.title_lbl.setText(self.change_word_structure.text())
                # print(self.data)
                cart.define_lbl.setText(text[:self.num] if len(text) < self.num else text[:self.num] + '...')
                item = QListWidgetItem()
                item.setSizeHint(cart.size())
                self.list_widget_for_cart.addItem(item)
                self.list_widget_for_cart.setItemWidget(item, cart)
                self.upload_json()
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Alert')
                msgBox.setText("This word is already exists")
                msgBox.exec()

                # msgBox = QMessageBox()
                # msgBox.setWindowTitle('')
                # msgBox.setText("The document has been modified.")
                # msgBox.setInformativeText("Do you want to save your changes?")
                # msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
                # msgBox.setDefaultButton(QMessageBox.Save)
                # ret = msgBox.exec()

    # введение изменения на выделенную слову
    def edit_btn_clicked(self):
        item = self.list_widget_for_cart.currentItem()
        widget = self.list_widget_for_cart.itemWidget(item)
        if self.change_word_structure.text() and self.set_definition.toPlainText():
            widget.title_lbl.setText(self.change_word_structure.text().strip())
            widget.define_lbl.setText(self.set_definition.toPlainText()[:self.num].strip() if len(
                self.set_definition.toPlainText()) < self.num else self.set_definition.toPlainText()[:self.num] + '...')
            self.list_widget_for_cart.setItemWidget(item, widget)
            self.upload_json()

    # вставка названия и определения в редактор
    def put_title_definition(self):
        item = self.list_widget_for_cart.currentItem()
        if item:
            widget = self.list_widget_for_cart.itemWidget(item)
            self.change_word_structure.setText(widget.title_lbl.text())
            try:
                # вставка слова с json файла
                self.set_definition.setText(self.data[widget.title_lbl.text().lower()])
            except KeyError:
                # вставка слова с карты(если в json файле этого слова нет)
                # self.set_definition.setText(widget.define_lbl.text())
                print('dda')
                pass

    # с json файла в dict
    def load_file(self):
        file = open("data_2.json", 'r')
        self.data = json.load(file)
        # print(self.data)

    # добавение первый n-ых слов, продолжение
    def adding_first_items(self, title, define):
        item = QListWidgetItem()

        # widgetni yasash
        widget = Cart()
        widget.title_lbl.setText(title.title())
        widget.define_lbl.setText(define[:self.num] if len(define) < self.num else define[:self.num] + '...')

        # item qo'shish
        self.list_widget_for_cart.addItem(item)
        item.setSizeHint(widget.size())
        # itemga widgetni o'rmnatish
        self.list_widget_for_cart.setItemWidget(item, widget)


    # добавение первый n-ых слов
    def add_first_items(self):
        i = 0
        for key, value in self.data.items():
            if i == 100:
                break
            else:
                i += 1
                self.adding_first_items(key, value)

