import os.path
import sys

from PySide6.QtGui import QTextCursor, Qt
from PySide6.QtWidgets import QMainWindow

from get_url import get_curency
from ui import Ui_MainWindow
import requests
import json
class Widget(QMainWindow, Ui_MainWindow):
    currency1 = get_curency()
    currency = {}
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file()

        self.text_uzs.setPlainText(f"{int(self.text_usd.toPlainText()) * float(self.currency[(self.comboBox.currentText())]):,} so'm")
        self.exit.clicked.connect(self.chiq)
        self.text_usd.textChanged.connect(self.change)
        # self.text_usd.textChanged.connect(self.change2)
        self.text_uzs.setObjectName('uzs')
        self.text_usd.setObjectName('usd')
        self.comboBox.setObjectName('uzs')
        self.gridLayout.setObjectName('ggrid')
        self.exit.setObjectName('exit')
        self.setObjectName('main')
        self.setWindowTitle('Converter')
        # self.text_usd.doSetTextCursor(QTextCursor.atEnd)
        self.comboBox.currentTextChanged.connect(self.change)
        self.setStyleSheet(open(self.get_path('style.css')).read())

    def chiq(self):
        sys.exit()


    def file(self):
        for i in range(3):

            Widget.currency[self.currency1[i]['Ccy']] = self.currency1[i]['Rate']

    def change(self):
        text_usd = self.text_usd.toPlainText()
        if text_usd == '':
            self.text_uzs.setPlainText('0')
        # if text_usd == '1':
        #     self.text_usd.setOverwriteMode(True)
            # self.text_usd.setPlainText('')
        # elif text_usd == '':
        #     self.text_usd.setOverwriteMode(False)
        #     self.text_usd.setPlainText('0')
        else:
            # text_usd.replace('0', '')
            self.text_uzs.setPlainText(f"{(float(text_usd) * float(self.currency[(self.comboBox.currentText())])):,} so'm")

    def get_path(self, relative_path):
        path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
        return os.path.join(path, relative_path)

    def get_path(self, relative_path):
        current_dir = os.path.dirname(__file__)
        return os.path.join(current_dir, relative_path)


# lb = Widget()
# path = lb.get_path2('main.py')
# print(path)
