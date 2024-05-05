# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converterIVmPUQ.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(322, 181)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-40, 10, 401, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.verticalspacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalspacer, 3, 3, 1, 1)

        self.text_uzs = QPlainTextEdit(self.gridLayoutWidget)
        self.text_uzs.setObjectName(u"text_uzs")
        self.text_uzs.setMaximumSize(QSize(16777215, 2777215))
        font = QFont()
        font.setPointSize(16)
        self.text_uzs.setFont(font)
        self.text_uzs.setMouseTracking(True)
        self.text_uzs.setTabletTracking(True)
#if QT_CONFIG(tooltip)
        self.text_uzs.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.text_uzs.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.text_uzs.setAutoFillBackground(False)
        self.text_uzs.setTabChangesFocus(True)
        self.text_uzs.setUndoRedoEnabled(False)
        self.text_uzs.setReadOnly(True)

        self.gridLayout.addWidget(self.text_uzs, 1, 3, 1, 1)

        self.label_uzs = QLabel(self.gridLayoutWidget)
        self.label_uzs.setObjectName(u"label_uzs")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_uzs.setFont(font1)
        self.label_uzs.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_uzs.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_uzs, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setMinimumSize(QSize(60, 38))
        self.comboBox.setFont(font1)
        self.comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(109, 109, 109);\n"
"border-radius: 10px")

        self.gridLayout.addWidget(self.comboBox, 2, 1, 2, 1)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.text_usd = QPlainTextEdit(self.gridLayoutWidget)
        self.text_usd.setObjectName(u"text_usd")
        self.text_usd.setFont(font)
        self.text_usd.setMouseTracking(True)
        self.text_usd.setTabletTracking(True)
        self.text_usd.setFocusPolicy(Qt.ClickFocus)
        self.text_usd.setTabChangesFocus(True)
        self.text_usd.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.text_usd.setPlainText(u"1")
        self.text_usd.setOverwriteMode(True)
        self.text_usd.setBackgroundVisible(False)

        self.gridLayout.addWidget(self.text_usd, 2, 3, 1, 1)

        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(210, 140, 101, 31))
        self.exit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(97, 97, 97);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(accessibility)
        self.text_uzs.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.text_uzs.setPlainText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_uzs.setText(QCoreApplication.translate("MainWindow", u"UZS", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"USD", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"RUB", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"EUR", None))

        self.exit.setText(QCoreApplication.translate("MainWindow", u"Chiqish", None))
    # retranslateUi

