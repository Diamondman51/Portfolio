from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout, QPushButton, QSizePolicy


class Keyboard(QGridLayout):
    bosildi = Signal(str)
    def __init__(self):
        super().__init__()
        self.places = [(j, i) for j in range(5) for i in range(4)]
        self.buttons = ['(', ')', 'C', '/', '7', '8', '9', 'X', '4', '5', '6', '+', '1', '2', '3', '-', '0', '.', '<--', '=']
        self.setkeys()


    tugmalar = {}

    def setkeys(self):
        for (row, col), key in zip(self.places, self.buttons):
            # for key in self.buttons:
            # for row, col in row_col:
            self.tugmalar[key] = QPushButton(key)
            self.tugmalar[key].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.addWidget(self.tugmalar[key], row, col)
            self.tugmalar[key].setObjectName('QPushButton')
            self.tugmalar[key].setFixedSize(65, 35)
            self.tugmalar[key].clicked.connect(self.bosilganda(self.tugmalar[key]))
        # self.tugmalar['='] = QPushButton('=')
        self.tugmalar['='].setObjectName('equal')
        self.addWidget(self.tugmalar['='], 4, 3)

    def bosilganda(self, button: QPushButton):

        def yubor():
            self.bosildi.emit(button.text())

        return yubor