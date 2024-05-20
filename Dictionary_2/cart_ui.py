# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form - untitled 2UPlKyf.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(417, 129)
        Form.setStyleSheet(u"\n"
"QFrame {\n"
"background-color: rgb(60,132,215);\n"
"border-top-left-radius: 0;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"QLabel {\n"
"padding: 5 4 3 3\n"
"}")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 401, 111))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.title_lbl = QLabel(self.frame)
        self.title_lbl.setObjectName(u"title_lbl")
        self.title_lbl.setGeometry(QRect(9, 9, 391, 21))
        self.define_lbl = QLabel(self.frame)
        self.define_lbl.setObjectName(u"define_lbl")
        self.define_lbl.setGeometry(QRect(9, 40, 381, 61))
        self.define_lbl.setLayoutDirection(Qt.LeftToRight)
        self.define_lbl.setAutoFillBackground(True)
        self.define_lbl.setTextFormat(Qt.PlainText)
        self.define_lbl.setScaledContents(True)
        self.define_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.define_lbl.setWordWrap(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.define_lbl.setText(QCoreApplication.translate("Form", u"Define", None))
    # retranslateUi

