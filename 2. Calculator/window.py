import os.path
import sys
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import Qt, QRegion
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit

from keyboard import Keyboard


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        w = 200
        h = 100
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(w, h)
        self.setObjectName('widget')
        self.vbox = QVBoxLayout()
        # self.vbox.setObjectName('widget')
        self.label = QTextEdit()
        self.label.setObjectName("qlabel")
        self.label.setFixedHeight(30)
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)
        self.setFixedSize(300, 250)
        keys = Keyboard()
        self.setStyleSheet(open(self.path_file('style.css')).read())
        self.vbox.addLayout(keys)
        keys.bosildi.connect(self.format)

        self.bosilganlar = ''

    def format(self, text):
        if text == '=':
            self.evaluate()
        elif text == 'C':
            self.label.clear()
        elif text == '<--':
            txt = self.label.toPlainText()
            txt = txt[:-1]
            self.set_text(txt)
        else:
            txt = self.label.toPlainText()
            txt += text
            self.set_text(txt)


    def set_text(self, txt:str):
        self.label.setText(txt.replace('++', '+').replace('--', '-').replace('//', '/').replace('X', '*').replace('**', '*').replace(
                '..', '.').replace('<--<--', '<--'))
    def evaluate(self):
        try:
            txt = self.label.toPlainText()
            ev = eval(txt)
            # self.bosilganlar = str(ev)
            self.label.setText(str(ev))
        except ZeroDivisionError:
            self.label.setText('На ноль делить нельзя')

    def path_file(self, relative_path):
        path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
        return os.path.join(path, relative_path)