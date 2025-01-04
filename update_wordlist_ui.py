# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_wordlist_dialog.ui'
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

class Ui_update_wordlist_dialog(object):
    def setupUi(self, update_wordlist_dialog):
        if not update_wordlist_dialog.objectName():
            update_wordlist_dialog.setObjectName(u"update_wordlist_dialog")
        update_wordlist_dialog.resize(400, 120)
        update_wordlist_dialog.setMinimumSize(QSize(400, 120))
        update_wordlist_dialog.setMaximumSize(QSize(400, 120))
        update_wordlist_dialog.setBaseSize(QSize(400, 120))
        self.verticalLayout = QVBoxLayout(update_wordlist_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.old_name = QLabel(update_wordlist_dialog)
        self.old_name.setObjectName(u"old_name")

        self.verticalLayout.addWidget(self.old_name)

        self.label = QLabel(update_wordlist_dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.new_name = QLineEdit(update_wordlist_dialog)
        self.new_name.setObjectName(u"new_name")

        self.verticalLayout.addWidget(self.new_name)

        self.buttonBox = QDialogButtonBox(update_wordlist_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(update_wordlist_dialog)
        self.buttonBox.accepted.connect(update_wordlist_dialog.accept)
        self.buttonBox.rejected.connect(update_wordlist_dialog.reject)

        QMetaObject.connectSlotsByName(update_wordlist_dialog)
    # setupUi

    def retranslateUi(self, update_wordlist_dialog):
        update_wordlist_dialog.setWindowTitle(QCoreApplication.translate("update_wordlist_dialog", u"Dialog", None))
        self.old_name.setText(QCoreApplication.translate("update_wordlist_dialog", u"Updating wordlist <name>", None))
        self.label.setText(QCoreApplication.translate("update_wordlist_dialog", u"New name", None))
    # retranslateUi

