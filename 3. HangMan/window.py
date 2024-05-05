from functools import lru_cache
import os.path
import random
import sys

from PyInstaller.compat import system
from PySide6.QtCore import QSize
from PySide6.QtGui import QWindow, Qt, QFont, QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, \
    QMessageBox


from Klaviatura import Klaviatura
from uzwords import words

class Window(QWidget):
    def __init__(self):
        self.bosilgan_harflar = []
        QWidget.__init__(self)

        self.vbox = QVBoxLayout()
        self.mistake = QLabel()
        self.score = QLabel()
        self.word = QLabel()
        self.vbox.addWidget(self.mistake)
        self.vbox.addWidget(self.score)
        self.vbox.addWidget(self.word)
        self.scores = 0
        self.mistakes = 0
        self.mistake.setText('Xatolar ' + str(self.mistakes))
        self.score.setText('Natija ' + str(self.scores))
        self.mistake.setObjectName('mistake')
        self.score.setObjectName('score')

        self.setWindowTitle('Hangman')
        self.grid = QGridLayout()
        self.label_img = QLabel()
        # self.word = QLabel()
        self.setFixedSize(800, 600)
        self.word.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word.setObjectName('yozuv')
        self.setLayout(self.grid)
        self.grid.addWidget(self.label_img, 0, 0)
        self.grid.addLayout(self.vbox, 0, 1)
        # self.setObjectName('Qlabel')
        self.grid.setRowStretch(0, 0)
        self.label_img.setFixedSize(200, 300)
        self.label_img.setScaledContents(True)
        self.setStyleSheet(open(self.source_path('style.css')).read())
        self.label_img.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.show_img()
        self.set_klaviatura()
        self.choose_word()
        self.setWindowIcon(QIcon(self.source_path('images/icon.png')))
        self.setObjectName('window')

        # self.set_klaviatura()

    def show_img(self):
        pixmap = QPixmap(self.source_path(f'images/stage{self.mistakes + 1}.png'))
        # self.label_text.setText(self.choose_word())
        self.label_img.setPixmap(pixmap)

    def choose_word(self):
        self.random_word = random.choice(words)
        print(self.random_word)
        self.word.setText(len(self.random_word) * '+')

    def set_klaviatura(self):
        self.klaviatura = Klaviatura()
        self.klaviatura.bosildi.connect(self.klaviatura_bosildi)
        self.grid.addLayout(self.klaviatura, 1, 0, 1, 2)

    def klaviatura_bosildi(self, text: str):
        self.bosilgan_harflar.append(text)
        self.show_word()
        if text not in self.random_word:
            self.mistakes += 1
            self.mistake.setText('Xatolar ' + str(self.mistakes))
            self.klaviatura.xato(text)
            self.show_img()
            if self.mistakes == 5:
                self.habar_ber('Siz yutqazdingiz. Yana o\'ynaysizmi?')
        else:
            self.klaviatura.togri(text)
            if '+' not in self.word.text():
                self.scores += 1
                self.score.setText('Natija ' + str(self.scores))
                self.habar_ber('Tabriklaymiz. Siz yutdingiz. Yana o\'naysizmi?')
        self.setStyleSheet(open(self.source_path('style.css')).read())


    def show_word(self):
        soz = ''
        for letter in self.random_word:
            if letter in self.bosilgan_harflar:
                soz += letter
            else:
                soz += '+'
        self.word.setText(soz)

    def habar_ber(self, habar):
        button = QMessageBox.question(self, 'Savol', habar)

        if button == QMessageBox.Yes:
            self.qayta_ishga_tushirish()
        else:
            sys.exit()

    def qayta_ishga_tushirish(self):
        self.mistakes = 0
        self.bosilgan_harflar = []
        self.mistake.setText('Xatolar ' + str(self.mistakes))
        self.show_img()
        self.choose_word()
        self.klaviatura.boshlangich_holatga_otkaz()

    def source_path(self, relative_path):
        path = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
        return os.path.join(path, relative_path)