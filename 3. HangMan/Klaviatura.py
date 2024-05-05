import os
import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSizePolicy


class Klaviatura(QVBoxLayout):

    def __init__(self):
        super().__init__()
        row_1 = QHBoxLayout()
        row_2 = QHBoxLayout()
        row_3 = QHBoxLayout()
        self.addLayout(row_1)
        self.addLayout(row_2)
        self.addLayout(row_3)

        prujina = QLabel()
        self.addWidget(prujina)
        prujina.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.buttons = {}

        for letters, place in {'йцукенгшўзғхъ': row_1, 'фықвапролджэ': row_2, 'ячсмитьбюҳ': row_3}.items():
            for letter in letters:
                self.buttons[letter] = QPushButton(letter)
                place.addWidget(self.buttons[letter])
                self.buttons[letter].setFixedSize(50, 50)
                place.setAlignment(Qt.AlignmentFlag.AlignTop)
                # self.buttons[letter].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                self.buttons[letter].clicked.connect(self.bosilganda(self.buttons[letter]))
                self.buttons[letter].setObjectName('klaviatura')


    bosildi = Signal(str)

    def bosilganda(self, button: QPushButton):
        def yubor():
            self.bosildi.emit(button.text())

        return yubor

    def xato(self, text):
        self.buttons[text].setObjectName('notogri')
        self.buttons[text].setDisabled(True)

    def togri(self, text):
        self.buttons[text].setObjectName('togri')
        self.buttons[text].setDisabled(True)

    def boshlangich_holatga_otkaz(self):
        for letter, button in self.buttons.items():
            button.setObjectName('klaviatura')
            button.setDisabled(False)
            button.setStyleSheet(open(self.source_path('style.css')).read())


    def source_path(self, relative_path):
        path = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
        return os.path.join(path, relative_path)