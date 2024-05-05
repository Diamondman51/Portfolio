# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convertermkLyBu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(334, 195)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"\n"
"border-radius: 10px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#widget {\n"
"background-color: rgba(240, 233, 255, 0.7);\n"
"border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"margin: 2px, 10px;\n"
"font-size: 20px;\n"
"padding: 2px;\n"
"border-radius: 15px;\n"
"padding:4px;\n"
"background-color:rgb(77, 77, 77);\n"
"color:white;\n"
"margin:5px;\n"
"}\n"
"#pushButton {\n"
"background-color: rgb(255, 238, 175);\n"
"color: rgb(0, 255, 255);\n"
"padding:5px;\n"
"background: black;\n"
"font-size: 20px\n"
"}\n"
"#pushButton:hover {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(175, 196, 255, 0.5));\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"padding: 5px;\n"
"background-color:rgb(77, 77, 77);\n"
"color:white;\n"
"}\n"
"#centralwidget {\n"
"border-radius: 15px;\n"
"\n"
"}\n"
"QComboBox {\n"
"padding:2px;\n"
"background-color:rgb(77, 77, 77);\n"
"color:white;\n"
"margin:2px;\n"
"}\n"
"*{border-radius:10px;}\n"
"QLabel {\n"
"padding:2px;\n"
"margin:2px;\n"
"}\n"
"gridLayout {\n"
"background-color: rgb(151, 167,"
                        " 255);\n"
"}")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 140, 111, 41))
        font = QFont()
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 311, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.currency2 = QLineEdit(self.gridLayoutWidget)
        self.currency2.setObjectName(u"currency2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.currency2.sizePolicy().hasHeightForWidth())
        self.currency2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.currency2, 1, 1, 1, 1)

        self.comboBox_currency1 = QComboBox(self.gridLayoutWidget)
        self.comboBox_currency1.addItem("")
        self.comboBox_currency1.addItem("")
        self.comboBox_currency1.addItem("")
        self.comboBox_currency1.setObjectName(u"comboBox_currency1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_currency1.sizePolicy().hasHeightForWidth())
        self.comboBox_currency1.setSizePolicy(sizePolicy2)
        self.comboBox_currency1.setMinimumSize(QSize(0, 0))
        self.comboBox_currency1.setMaximumSize(QSize(65, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        self.comboBox_currency1.setFont(font1)

        self.gridLayout.addWidget(self.comboBox_currency1, 0, 0, 1, 1)

        self.currency1 = QLineEdit(self.gridLayoutWidget)
        self.currency1.setObjectName(u"currency1")
        sizePolicy1.setHeightForWidth(self.currency1.sizePolicy().hasHeightForWidth())
        self.currency1.setSizePolicy(sizePolicy1)
        self.currency1.setFont(font)
        self.currency1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.currency1, 0, 1, 1, 1)

        self.comboBox_currency2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_currency2.addItem("")
        self.comboBox_currency2.addItem("")
        self.comboBox_currency2.addItem("")
        self.comboBox_currency2.addItem("")
        self.comboBox_currency2.setObjectName(u"comboBox_currency2")
        sizePolicy2.setHeightForWidth(self.comboBox_currency2.sizePolicy().hasHeightForWidth())
        self.comboBox_currency2.setSizePolicy(sizePolicy2)
        self.comboBox_currency2.setMinimumSize(QSize(0, 0))
        self.comboBox_currency2.setMaximumSize(QSize(65, 16777215))
        self.comboBox_currency2.setFont(font1)

        self.gridLayout.addWidget(self.comboBox_currency2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Chiqish", None))
        self.currency2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_currency1.setItemText(0, QCoreApplication.translate("MainWindow", u"USD", None))
        self.comboBox_currency1.setItemText(1, QCoreApplication.translate("MainWindow", u"RUB", None))
        self.comboBox_currency1.setItemText(2, QCoreApplication.translate("MainWindow", u"EUR", None))

        self.currency1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_currency2.setItemText(0, QCoreApplication.translate("MainWindow", u"UZS", None))
        self.comboBox_currency2.setItemText(1, QCoreApplication.translate("MainWindow", u"USD", None))
        self.comboBox_currency2.setItemText(2, QCoreApplication.translate("MainWindow", u"RUB", None))
        self.comboBox_currency2.setItemText(3, QCoreApplication.translate("MainWindow", u"EUR", None))

    # retranslateUi

