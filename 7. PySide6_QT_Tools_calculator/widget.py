from PySide6.QtWidgets import QMainWindow, QPushButton

from ui import Ui_MainWindow


class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn0.clicked.connect(self.button_clicked)
        self.btn_1.clicked.connect(self.button_clicked)
        self.btn_2.clicked.connect(self.button_clicked)
        self.btn_3.clicked.connect(self.button_clicked)
        self.btn_4.clicked.connect(self.button_clicked)
        self.btn_5.clicked.connect(self.button_clicked)
        self.btn_6.clicked.connect(self.button_clicked)
        self.btn_7.clicked.connect(self.button_clicked)
        self.btn_8.clicked.connect(self.button_clicked)
        self.btn_9.clicked.connect(self.button_clicked)
        self.btn_C.clicked.connect(self.button_clicked)
        self.btn_div.clicked.connect(self.button_clicked)
        self.btn_dot.clicked.connect(self.button_clicked)
        self.btn_plus.clicked.connect(self.button_clicked)
        self.btn_multip.clicked.connect(self.button_clicked)
        self.btn_equal.clicked.connect(self.button_clicked)
        self.btn_minus.clicked.connect(self.button_clicked)

    def button_clicked(self, ):
        button: str = self.sender().text()
        text2 = self.lbl_2.text()
        text1 = self.lbl_1.text()
        if button == '=':
            self.calculate(text2, text1)
        elif button == 'C':
            text = '0'
            self.lbl_1.setText('')
            self.lbl_2.setText(text)
        elif button in '+*-/':
            self.lbl_1.setText(text2 + button.replace('*', '×').replace('/', '÷'))
            print(self.lbl_1.text())
            text2 = ""
            self.lbl_2.setText(text2)
        else:
            if text2 == '0':
                text2 = ''
            text2 += button
            self.lbl_2.setText(text2.replace('=', ''))
        # print(button.text())

    def calculate(self, text2, text1):
        print('text2:', text2)
        print('text1:', text1)
        txt = text1 + text2
        ans = eval(txt.replace('×', '*').replace('÷', '/'))
        self.lbl_1.setText(str(ans))