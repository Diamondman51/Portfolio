# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JavafUkXZs.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(381, 497)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_1 = QLabel(self.centralwidget)
        self.lbl_1.setObjectName(u"lbl_1")
        self.lbl_1.setGeometry(QRect(10, 30, 361, 71))
        font = QFont()
        font.setPointSize(25)
        self.lbl_1.setFont(font)
        self.lbl_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 200, 361, 301))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_plus = QPushButton(self.gridLayoutWidget)
        self.btn_plus.setObjectName(u"btn_plus")
        font1 = QFont()
        font1.setPointSize(20)
        self.btn_plus.setFont(font1)
        self.btn_plus.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.btn_plus, 0, 3, 1, 1)

        self.btn_8 = QPushButton(self.gridLayoutWidget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setFont(font1)
        self.btn_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)

        self.btn_1 = QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setFont(font1)
        self.btn_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)

        self.btn_div = QPushButton(self.gridLayoutWidget)
        self.btn_div.setObjectName(u"btn_div")
        self.btn_div.setFont(font1)
        self.btn_div.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.btn_div, 3, 3, 1, 1)

        self.btn_9 = QPushButton(self.gridLayoutWidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setFont(font1)
        self.btn_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setFont(font1)
        self.btn_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)

        self.btn_5 = QPushButton(self.gridLayoutWidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setFont(font1)
        self.btn_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_7 = QPushButton(self.gridLayoutWidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setFont(font1)
        self.btn_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_6 = QPushButton(self.gridLayoutWidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setFont(font1)
        self.btn_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_multip = QPushButton(self.gridLayoutWidget)
        self.btn_multip.setObjectName(u"btn_multip")
        self.btn_multip.setFont(font1)
        self.btn_multip.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.btn_multip, 2, 3, 1, 1)

        self.btn_minus = QPushButton(self.gridLayoutWidget)
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setFont(font1)
        self.btn_minus.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.btn_minus, 1, 3, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setFont(font1)
        self.btn_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_2 = QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setFont(font1)
        self.btn_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)

        self.btn_dot = QPushButton(self.gridLayoutWidget)
        self.btn_dot.setObjectName(u"btn_dot")
        self.btn_dot.setFont(font1)
        self.btn_dot.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn_dot, 3, 2, 1, 1)

        self.btn0 = QPushButton(self.gridLayoutWidget)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setFont(font1)
        self.btn0.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.btn0, 3, 0, 1, 2)

        self.btn_equal = QPushButton(self.gridLayoutWidget)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setFont(font1)
        self.btn_equal.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_equal, 4, 2, 1, 2)

        self.btn_C = QPushButton(self.gridLayoutWidget)
        self.btn_C.setObjectName(u"btn_C")
        self.btn_C.setFont(font1)
        self.btn_C.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_C, 4, 0, 1, 2)

        self.lbl_2 = QLabel(self.centralwidget)
        self.lbl_2.setObjectName(u"lbl_2")
        self.lbl_2.setGeometry(QRect(10, 110, 361, 71))
        font2 = QFont()
        font2.setPointSize(45)
        self.lbl_2.setFont(font2)
        self.lbl_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_1.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_multip.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.lbl_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

