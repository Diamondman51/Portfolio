import functools
import json

from difflib import get_close_matches
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton

from UI import Ui_MainWindow


class Widget(QMainWindow, Ui_MainWindow):
    file = open('data.json', 'r')
    data = json.load(file)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.set_word)
        # self.pushButton.clicked.connect(functools.partial(self.set_word, self.lineEdit.text))
        self.pushButton.setIcon(QIcon('loupe.png'))
        # self.pushButton.clicked.connect(self.set_word)

    # def set_word(self, text):
    #     words = []
    #     try:
    #         # print(self.data)
    #         # text = self.lineEdit.text()
    #         self.textEdit.setText(self.data[text])
    #         additional_words = get_close_matches(text, self.data, 5)
    #         print(additional_words)
    #         for word in additional_words[:5]:
    #             self.wordd = QPushButton(word)
    #             words.append(self.wordd)
    #             self.horizontalLayout.addWidget(self.wordd)
    #         if len(words) >= 5:
    #             self.horizontalLayout.removeWidget(words[0])
    #             del words[0]
    #     except KeyError:
    #         pass

    def set_word(self, text):
        try:
            self.textEdit.setText(self.data[text])
            additional_words = get_close_matches(text, self.data, 5)
            self.clear_additional_word_buttons()
            for word in additional_words[:5]:
                button = QPushButton(word)
                button.clicked.connect(lambda cheked, word=word: self.set_word(word))
                # button.clicked(self.lineEdit.setText(word))
                self.horizontalLayout.addWidget(button)
        except KeyError:
            self.clear_additional_word_buttons()

    def clear_additional_word_buttons(self):
        while self.horizontalLayout.count() > 0:
            item = self.horizontalLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()


