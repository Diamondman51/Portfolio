import sys

from PySide6 import QtCore
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QWidget

from getcurrency import get_currency
from ui import Ui_MainWindow


class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(exit)
        self.gridLayoutWidget.setObjectName('qWidget')
        self.setStyleSheet(open('style.css').read())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.currency1.textChanged.connect(self.change)
        self.currency1.setFocus()

    currency = get_currency()
    cur = {}
    for i in range(3):
        cur[currency[i]['Ccy']] = currency[i]['Rate']
    cur['UZS'] = currency[0]['Rate']

    def change(self):
        currency1_text = self.currency1.text()
        # print(currency1_text)
        if self.comboBox_currency2.currentText() == 'UZS' and self.comboBox_currency1.currentText() != 'UZS':
            self.currency2.setText(f"{float(self.cur['UZS']) * float(currency1_text):,}")
        else:
            self.currency2.setText(str(float(self.cur[self.comboBox_currency1.currentText()]) * float(currency1_text) / float(self.cur[self.comboBox_currency2.currentText()])))