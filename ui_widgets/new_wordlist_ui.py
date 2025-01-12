# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_wordlist_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_new_wordlist_dialog(object):
    def setupUi(self, new_wordlist_dialog):
        if not new_wordlist_dialog.objectName():
            new_wordlist_dialog.setObjectName(u"new_wordlist_dialog")
        new_wordlist_dialog.resize(400, 96)
        new_wordlist_dialog.setMinimumSize(QSize(400, 96))
        new_wordlist_dialog.setMaximumSize(QSize(400, 96))
        new_wordlist_dialog.setBaseSize(QSize(400, 96))
        self.verticalLayout = QVBoxLayout(new_wordlist_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(new_wordlist_dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.name = QLineEdit(new_wordlist_dialog)
        self.name.setObjectName(u"name")

        self.verticalLayout.addWidget(self.name)

        self.buttonBox = QDialogButtonBox(new_wordlist_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(new_wordlist_dialog)
        self.buttonBox.accepted.connect(new_wordlist_dialog.accept)
        self.buttonBox.rejected.connect(new_wordlist_dialog.reject)

        QMetaObject.connectSlotsByName(new_wordlist_dialog)
    # setupUi

    def retranslateUi(self, new_wordlist_dialog):
        new_wordlist_dialog.setWindowTitle(QCoreApplication.translate("new_wordlist_dialog", u"New wordlist", None))
        self.label.setText(QCoreApplication.translate("new_wordlist_dialog", u"Name", None))
    # retranslateUi

