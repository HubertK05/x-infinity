# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wordlists.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(897, 461)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.word_pages = QStackedWidget(self.centralwidget)
        self.word_pages.setObjectName(u"word_pages")
        self.entry_not_selected = QWidget()
        self.entry_not_selected.setObjectName(u"entry_not_selected")
        self.horizontalLayout_5 = QHBoxLayout(self.entry_not_selected)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.entry_not_selected_label = QLabel(self.entry_not_selected)
        self.entry_not_selected_label.setObjectName(u"entry_not_selected_label")
        self.entry_not_selected_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.entry_not_selected_label)

        self.word_pages.addWidget(self.entry_not_selected)
        self.entry_selected = QWidget()
        self.entry_selected.setObjectName(u"entry_selected")
        self.horizontalLayout_7 = QHBoxLayout(self.entry_selected)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.entry = QListWidget(self.entry_selected)
        self.entry.setObjectName(u"entry")

        self.horizontalLayout_7.addWidget(self.entry)

        self.word_pages.addWidget(self.entry_selected)

        self.gridLayout.addWidget(self.word_pages, 1, 2, 1, 1)

        self.wordlist_pages = QStackedWidget(self.centralwidget)
        self.wordlist_pages.setObjectName(u"wordlist_pages")
        self.wordlist_not_selected = QWidget()
        self.wordlist_not_selected.setObjectName(u"wordlist_not_selected")
        self.horizontalLayout_4 = QHBoxLayout(self.wordlist_not_selected)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.wordlist_not_selected_label = QLabel(self.wordlist_not_selected)
        self.wordlist_not_selected_label.setObjectName(u"wordlist_not_selected_label")
        self.wordlist_not_selected_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.wordlist_not_selected_label)

        self.wordlist_pages.addWidget(self.wordlist_not_selected)
        self.wordlist_selected = QWidget()
        self.wordlist_selected.setObjectName(u"wordlist_selected")
        self.horizontalLayout_6 = QHBoxLayout(self.wordlist_selected)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.wordlist = QListWidget(self.wordlist_selected)
        self.wordlist.setObjectName(u"wordlist")

        self.horizontalLayout_6.addWidget(self.wordlist)

        self.wordlist_pages.addWidget(self.wordlist_selected)

        self.gridLayout.addWidget(self.wordlist_pages, 1, 1, 1, 1)

        self.selected_entry_title = QLabel(self.centralwidget)
        self.selected_entry_title.setObjectName(u"selected_entry_title")

        self.gridLayout.addWidget(self.selected_entry_title, 0, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 2, 1, 1)

        self.wordlists = QListWidget(self.centralwidget)
        self.wordlists.setObjectName(u"wordlists")

        self.gridLayout.addWidget(self.wordlists, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)

        self.wordlist_title = QLabel(self.centralwidget)
        self.wordlist_title.setObjectName(u"wordlist_title")

        self.gridLayout.addWidget(self.wordlist_title, 0, 0, 1, 1)

        self.selected_wordlist_title = QLabel(self.centralwidget)
        self.selected_wordlist_title.setObjectName(u"selected_wordlist_title")

        self.gridLayout.addWidget(self.selected_wordlist_title, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout.addWidget(self.pushButton_8)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 897, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.word_pages.setCurrentIndex(0)
        self.wordlist_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.entry_not_selected_label.setText(QCoreApplication.translate("MainWindow", u"Select a word first", None))
        self.wordlist_not_selected_label.setText(QCoreApplication.translate("MainWindow", u"Select a wordlist first", None))
        self.selected_entry_title.setText(QCoreApplication.translate("MainWindow", u"Selected word", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit entry", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete entry", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Use this wordlist", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"New entry", None))
        self.wordlist_title.setText(QCoreApplication.translate("MainWindow", u"Your wordlists", None))
        self.selected_wordlist_title.setText(QCoreApplication.translate("MainWindow", u"Selected wordlist", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"New wordlist", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Save wordlist", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Load wordlist", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Delete wordlist", None))
    # retranslateUi

