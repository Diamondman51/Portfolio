# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'glossaryWRSAWK.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(451, 638)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(451, 638))
        MainWindow.setMaximumSize(QSize(451, 638))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"QGreedLayout {\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QListWidget {\n"
"border: 1px solid blue;\n"
"opacity: 223;\n"
"}\n"
"\n"
"\n"
"QTextEdit {\n"
"border: 1px solid blue;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkblue;\n"
"}\n"
"\n"
"*{\n"
"margin: 1;\n"
"padding: 5;\n"
"border-radius: 5;\n"
"}\n"
"\n"
"QPushButton {\n"
"border-radius: 2px;\n"
"background-color: rgba(162, 162, 162, 0.4);\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color:rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{margin:1 0 0 1}")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 451, 641))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 451, 638))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.change_word_structure = QLineEdit(self.gridLayoutWidget)
        self.change_word_structure.setObjectName(u"change_word_structure")

        self.gridLayout.addWidget(self.change_word_structure, 5, 0, 1, 4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.add_btn = QPushButton(self.gridLayoutWidget)
        self.add_btn.setObjectName(u"add_btn")

        self.gridLayout_2.addWidget(self.add_btn, 0, 2, 1, 1)

        self.delete_btn = QPushButton(self.gridLayoutWidget)
        self.delete_btn.setObjectName(u"delete_btn")

        self.gridLayout_2.addWidget(self.delete_btn, 0, 0, 1, 1)

        self.bnt_read = QPushButton(self.gridLayoutWidget)
        self.bnt_read.setObjectName(u"bnt_read")
        icon = QIcon()
        icon.addFile(u"../../Dictionary_with_carts/read.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_read.setIcon(icon)

        self.gridLayout_2.addWidget(self.bnt_read, 0, 3, 1, 1)

        self.edit_btn = QPushButton(self.gridLayoutWidget)
        self.edit_btn.setObjectName(u"edit_btn")

        self.gridLayout_2.addWidget(self.edit_btn, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 4)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 15))
        self.label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"padding:1px;\n"
"}")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 4)

        self.set_definition = QTextEdit(self.gridLayoutWidget)
        self.set_definition.setObjectName(u"set_definition")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.set_definition.sizePolicy().hasHeightForWidth())
        self.set_definition.setSizePolicy(sizePolicy2)
        self.set_definition.setMinimumSize(QSize(0, 0))
        self.set_definition.setMaximumSize(QSize(16777215, 140))

        self.gridLayout.addWidget(self.set_definition, 6, 0, 1, 4)

        self.search_paneli = QLineEdit(self.gridLayoutWidget)
        self.search_paneli.setObjectName(u"search_paneli")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.search_paneli.sizePolicy().hasHeightForWidth())
        self.search_paneli.setSizePolicy(sizePolicy3)
        self.search_paneli.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.search_paneli, 0, 0, 1, 2)

        self.btn_voice = QPushButton(self.gridLayoutWidget)
        self.btn_voice.setObjectName(u"btn_voice")
        icon1 = QIcon()
        icon1.addFile(u"../../Dictionary_with_carts/record.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_voice.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_voice, 0, 3, 1, 1)

        self.list_widget_for_cart = QListWidget(self.gridLayoutWidget)
        self.list_widget_for_cart.setObjectName(u"list_widget_for_cart")
        sizePolicy2.setHeightForWidth(self.list_widget_for_cart.sizePolicy().hasHeightForWidth())
        self.list_widget_for_cart.setSizePolicy(sizePolicy2)
        self.list_widget_for_cart.setMinimumSize(QSize(0, 350))
        self.list_widget_for_cart.setMaximumSize(QSize(16777215, 500))

        self.gridLayout.addWidget(self.list_widget_for_cart, 2, 0, 1, 4)

        self.search_btn = QPushButton(self.gridLayoutWidget)
        self.search_btn.setObjectName(u"search_btn")

        self.gridLayout.addWidget(self.search_btn, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bnt_read.setText("")
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label.setText("")
        self.btn_voice.setText("")
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

