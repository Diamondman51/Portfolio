from re import S
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QTextEdit, QLabel, QVBoxLayout
import os

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.label = QLabel()
        self.tetx_edit = QTextEdit()
        self.tetx_edit.setFixedHeight(30)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.tetx_edit)
        self.setLayout(self.vbox)
        self.label.setText(os.getcwd() + '>')
        self.tetx_edit.textChanged.connect(self.text_to_label)
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName('label')
        self.tetx_edit.setObjectName('txt_edit')
        self.setStyleSheet(open('style.css').read())
        self.setMinimumSize(700, 400)
        # self.tetx_edit

    def text_to_label(self):
        lb = self.label.text()
        text = self.tetx_edit.toPlainText()
        cd = os.getcwd()
        if '\n' in text:
            txt = text.strip()
            print(txt)
            self.label.setText(f'{lb}{txt}\n{cd}>')
            self.tetx_edit.clear()