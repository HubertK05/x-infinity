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
        MainWindow.resize(795, 462)
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
        self.edit_entry_button = QPushButton(self.centralwidget)
        self.edit_entry_button.setObjectName(u"edit_entry_button")

        self.horizontalLayout_3.addWidget(self.edit_entry_button)

        self.delete_entry_button = QPushButton(self.centralwidget)
        self.delete_entry_button.setObjectName(u"delete_entry_button")

        self.horizontalLayout_3.addWidget(self.delete_entry_button)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 2, 1, 1)

        self.wordlists = QListWidget(self.centralwidget)
        self.wordlists.setObjectName(u"wordlists")

        self.gridLayout.addWidget(self.wordlists, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.use_wordlist_button = QPushButton(self.centralwidget)
        self.use_wordlist_button.setObjectName(u"use_wordlist_button")

        self.horizontalLayout_2.addWidget(self.use_wordlist_button)

        self.update_wordlist_button = QPushButton(self.centralwidget)
        self.update_wordlist_button.setObjectName(u"update_wordlist_button")

        self.horizontalLayout_2.addWidget(self.update_wordlist_button)

        self.delete_wordlist_button = QPushButton(self.centralwidget)
        self.delete_wordlist_button.setObjectName(u"delete_wordlist_button")

        self.horizontalLayout_2.addWidget(self.delete_wordlist_button)

        self.save_wordlist_button = QPushButton(self.centralwidget)
        self.save_wordlist_button.setObjectName(u"save_wordlist_button")

        self.horizontalLayout_2.addWidget(self.save_wordlist_button)

        self.new_entry_button = QPushButton(self.centralwidget)
        self.new_entry_button.setObjectName(u"new_entry_button")

        self.horizontalLayout_2.addWidget(self.new_entry_button)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)

        self.wordlist_title = QLabel(self.centralwidget)
        self.wordlist_title.setObjectName(u"wordlist_title")

        self.gridLayout.addWidget(self.wordlist_title, 0, 0, 1, 1)

        self.selected_wordlist_title = QLabel(self.centralwidget)
        self.selected_wordlist_title.setObjectName(u"selected_wordlist_title")

        self.gridLayout.addWidget(self.selected_wordlist_title, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.new_wordlist_button = QPushButton(self.centralwidget)
        self.new_wordlist_button.setObjectName(u"new_wordlist_button")

        self.horizontalLayout.addWidget(self.new_wordlist_button)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 20))
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
        self.edit_entry_button.setText(QCoreApplication.translate("MainWindow", u"Edit entry", None))
        self.delete_entry_button.setText(QCoreApplication.translate("MainWindow", u"Delete entry", None))
        self.use_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"Use this wordlist", None))
        self.update_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"Update wordlist", None))
        self.delete_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"Delete wordlist", None))
        self.save_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"Save wordlist", None))
        self.new_entry_button.setText(QCoreApplication.translate("MainWindow", u"New entry", None))
        self.wordlist_title.setText(QCoreApplication.translate("MainWindow", u"Your wordlists", None))
        self.selected_wordlist_title.setText(QCoreApplication.translate("MainWindow", u"Selected wordlist", None))
        self.new_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"New wordlist", None))
    # retranslateUi

