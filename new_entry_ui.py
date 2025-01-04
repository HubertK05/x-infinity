# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_entry_dialog.ui'
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

class Ui_new_entry_dialog(object):
    def setupUi(self, new_entry_dialog):
        if not new_entry_dialog.objectName():
            new_entry_dialog.setObjectName(u"new_entry_dialog")
        new_entry_dialog.resize(400, 150)
        new_entry_dialog.setMinimumSize(QSize(400, 150))
        new_entry_dialog.setMaximumSize(QSize(400, 150))
        new_entry_dialog.setBaseSize(QSize(400, 150))
        self.verticalLayout = QVBoxLayout(new_entry_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(new_entry_dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.word = QLineEdit(new_entry_dialog)
        self.word.setObjectName(u"word")

        self.verticalLayout.addWidget(self.word)

        self.label_2 = QLabel(new_entry_dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.definition = QLineEdit(new_entry_dialog)
        self.definition.setObjectName(u"definition")

        self.verticalLayout.addWidget(self.definition)

        self.buttonBox = QDialogButtonBox(new_entry_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(new_entry_dialog)
        self.buttonBox.accepted.connect(new_entry_dialog.accept)
        self.buttonBox.rejected.connect(new_entry_dialog.reject)

        QMetaObject.connectSlotsByName(new_entry_dialog)
    # setupUi

    def retranslateUi(self, new_entry_dialog):
        new_entry_dialog.setWindowTitle(QCoreApplication.translate("new_entry_dialog", u"New entry", None))
        self.label.setText(QCoreApplication.translate("new_entry_dialog", u"Word", None))
        self.label_2.setText(QCoreApplication.translate("new_entry_dialog", u"Definition", None))
    # retranslateUi

