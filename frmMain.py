# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmMain.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import youtube

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(479, 318)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btDownload = QPushButton(self.centralwidget)
        self.btDownload.setObjectName(u"btDownload")
        self.btDownload.setGeometry(QRect(280, 240, 101, 31))
        font = QFont()
        font.setPointSize(12)
        self.btDownload.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 130, 49, 16))
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 189, 49, 16))
        self.label_2.setFont(font)
        self.txtLink = QLineEdit(self.centralwidget)
        self.txtLink.setObjectName(u"txtLink")
        self.txtLink.setGeometry(QRect(90, 127, 361, 22))
        font1 = QFont()
        font1.setPointSize(10)
        self.txtLink.setFont(font1)
        self.txtTitulo = QLineEdit(self.centralwidget)
        self.txtTitulo.setObjectName(u"txtTitulo")
        self.txtTitulo.setGeometry(QRect(90, 187, 361, 22))
        self.txtTitulo.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 30, 141, 61))
        font2 = QFont()
        font2.setPointSize(22)
        self.label_3.setFont(font2)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 17, 241, 91))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 227, 111, 58))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rbMp3 = QRadioButton(self.layoutWidget)
        self.rbMp3.setObjectName(u"rbMp3")
        self.rbMp3.setFont(font)
        self.rbMp3.setChecked(False)

        self.verticalLayout.addWidget(self.rbMp3)

        self.rbMp4 = QRadioButton(self.layoutWidget)
        self.rbMp4.setObjectName(u"rbMp4")
        self.rbMp4.setFont(font)
        self.rbMp4.setChecked(True)

        self.verticalLayout.addWidget(self.rbMp4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Link:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/youtube/youtube.png\"/></p></body></html>", None))
        self.rbMp3.setText(QCoreApplication.translate("MainWindow", u"mp3", None))
        self.rbMp4.setText(QCoreApplication.translate("MainWindow", u"mp4", None))
    # retranslateUi

