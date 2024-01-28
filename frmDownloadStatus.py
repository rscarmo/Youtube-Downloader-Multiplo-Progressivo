# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmDownloadStatus.ui'
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
from PySide6.QtWidgets import (QApplication, QProgressBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_frmDownloadStatus(object):
    def setupUi(self, frmDownloadStatus):
        if not frmDownloadStatus.objectName():
            frmDownloadStatus.setObjectName(u"frmDownloadStatus")
        frmDownloadStatus.resize(397, 120)
        self.progressBar = QProgressBar(frmDownloadStatus)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 30, 361, 23))
        self.progressBar.setValue(24)
        self.btCancelar = QPushButton(frmDownloadStatus)
        self.btCancelar.setObjectName(u"btCancelar")
        self.btCancelar.setGeometry(QRect(200, 70, 91, 31))
        self.btPausar = QPushButton(frmDownloadStatus)
        self.btPausar.setObjectName(u"btPausar")
        self.btPausar.setGeometry(QRect(100, 70, 91, 31))

        self.retranslateUi(frmDownloadStatus)

        QMetaObject.connectSlotsByName(frmDownloadStatus)
    # setupUi

    def retranslateUi(self, frmDownloadStatus):
        frmDownloadStatus.setWindowTitle(QCoreApplication.translate("frmDownloadStatus", u"Download", None))
        self.btCancelar.setText(QCoreApplication.translate("frmDownloadStatus", u"Cancelar", None))
        self.btPausar.setText(QCoreApplication.translate("frmDownloadStatus", u"Pausar", None))
    # retranslateUi

