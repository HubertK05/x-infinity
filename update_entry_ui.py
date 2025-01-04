# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_entry_dialog.ui'
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

class Ui_update_entry_dialog(object):
    def setupUi(self, update_entry_dialog):
        if not update_entry_dialog.objectName():
            update_entry_dialog.setObjectName(u"update_entry_dialog")
        update_entry_dialog.resize(400, 135)
        update_entry_dialog.setMinimumSize(QSize(400, 135))
        update_entry_dialog.setMaximumSize(QSize(400, 135))
        update_entry_dialog.setBaseSize(QSize(400, 135))
        self.verticalLayout = QVBoxLayout(update_entry_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name = QLabel(update_entry_dialog)
        self.name.setObjectName(u"name")

        self.verticalLayout.addWidget(self.name)

        self.label_2 = QLabel(update_entry_dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.definition = QLineEdit(update_entry_dialog)
        self.definition.setObjectName(u"definition")

        self.verticalLayout.addWidget(self.definition)

        self.buttonBox = QDialogButtonBox(update_entry_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(update_entry_dialog)
        self.buttonBox.accepted.connect(update_entry_dialog.accept)
        self.buttonBox.rejected.connect(update_entry_dialog.reject)

        QMetaObject.connectSlotsByName(update_entry_dialog)
    # setupUi

    def retranslateUi(self, update_entry_dialog):
        update_entry_dialog.setWindowTitle(QCoreApplication.translate("update_entry_dialog", u"Dialog", None))
        self.name.setText(QCoreApplication.translate("update_entry_dialog", u"Updating word <word>", None))
        self.label_2.setText(QCoreApplication.translate("update_entry_dialog", u"Definition", None))
    # retranslateUi

