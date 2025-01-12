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
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(981, 558)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.selected_wordlist_title = QLabel(self.centralwidget)
        self.selected_wordlist_title.setObjectName(u"selected_wordlist_title")

        self.gridLayout.addWidget(self.selected_wordlist_title, 0, 2, 1, 1)

        self.wordlist_pages = QStackedWidget(self.centralwidget)
        self.wordlist_pages.setObjectName(u"wordlist_pages")
        self.wordlist_not_selected = QWidget()
        self.wordlist_not_selected.setObjectName(u"wordlist_not_selected")
        self.verticalLayout_2 = QVBoxLayout(self.wordlist_not_selected)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wordlist_not_selected_label = QLabel(self.wordlist_not_selected)
        self.wordlist_not_selected_label.setObjectName(u"wordlist_not_selected_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordlist_not_selected_label.sizePolicy().hasHeightForWidth())
        self.wordlist_not_selected_label.setSizePolicy(sizePolicy)
        self.wordlist_not_selected_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.wordlist_not_selected_label)

        self.wordlist_pages.addWidget(self.wordlist_not_selected)
        self.wordlist_selected = QWidget()
        self.wordlist_selected.setObjectName(u"wordlist_selected")
        self.verticalLayout_3 = QVBoxLayout(self.wordlist_selected)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.wordlist = QListWidget(self.wordlist_selected)
        self.wordlist.setObjectName(u"wordlist")

        self.verticalLayout_3.addWidget(self.wordlist)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.use_wordlist_button = QPushButton(self.wordlist_selected)
        self.use_wordlist_button.setObjectName(u"use_wordlist_button")

        self.horizontalLayout_4.addWidget(self.use_wordlist_button)

        self.update_wordlist_button = QPushButton(self.wordlist_selected)
        self.update_wordlist_button.setObjectName(u"update_wordlist_button")

        self.horizontalLayout_4.addWidget(self.update_wordlist_button)

        self.delete_wordlist_button = QPushButton(self.wordlist_selected)
        self.delete_wordlist_button.setObjectName(u"delete_wordlist_button")

        self.horizontalLayout_4.addWidget(self.delete_wordlist_button)

        self.generate_definitions_button = QPushButton(self.wordlist_selected)
        self.generate_definitions_button.setObjectName(u"generate_definitions_button")

        self.horizontalLayout_4.addWidget(self.generate_definitions_button)

        self.new_entry_button = QPushButton(self.wordlist_selected)
        self.new_entry_button.setObjectName(u"new_entry_button")

        self.horizontalLayout_4.addWidget(self.new_entry_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.wordlist_pages.addWidget(self.wordlist_selected)

        self.gridLayout.addWidget(self.wordlist_pages, 1, 2, 1, 1)

        self.wordlist_title = QLabel(self.centralwidget)
        self.wordlist_title.setObjectName(u"wordlist_title")

        self.gridLayout.addWidget(self.wordlist_title, 0, 0, 1, 1)

        self.selected_entry_title = QLabel(self.centralwidget)
        self.selected_entry_title.setObjectName(u"selected_entry_title")

        self.gridLayout.addWidget(self.selected_entry_title, 0, 3, 1, 1)

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
        self.verticalLayout_4 = QVBoxLayout(self.entry_selected)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.word_label = QLabel(self.entry_selected)
        self.word_label.setObjectName(u"word_label")
        self.word_label.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.word_label)

        self.definition_label = QLabel(self.entry_selected)
        self.definition_label.setObjectName(u"definition_label")
        self.definition_label.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.definition_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.edit_entry_button = QPushButton(self.entry_selected)
        self.edit_entry_button.setObjectName(u"edit_entry_button")

        self.horizontalLayout_3.addWidget(self.edit_entry_button)

        self.delete_entry_button = QPushButton(self.entry_selected)
        self.delete_entry_button.setObjectName(u"delete_entry_button")

        self.horizontalLayout_3.addWidget(self.delete_entry_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.word_pages.addWidget(self.entry_selected)

        self.gridLayout.addWidget(self.word_pages, 1, 3, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.wordlists = QListWidget(self.page)
        self.wordlists.setObjectName(u"wordlists")

        self.verticalLayout_7.addWidget(self.wordlists)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.generate_wordlist_button = QPushButton(self.page)
        self.generate_wordlist_button.setObjectName(u"generate_wordlist_button")

        self.horizontalLayout.addWidget(self.generate_wordlist_button)

        self.new_wordlist_button = QPushButton(self.page)
        self.new_wordlist_button.setObjectName(u"new_wordlist_button")

        self.horizontalLayout.addWidget(self.new_wordlist_button)


        self.verticalLayout_7.addLayout(self.horizontalLayout)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.wordlist_pages.setCurrentIndex(0)
        self.word_pages.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wordlist Selection", None))
        self.selected_wordlist_title.setText(QCoreApplication.translate("MainWindow", u"Selected wordlist", None))
        self.wordlist_not_selected_label.setText(QCoreApplication.translate("MainWindow", u"Select a wordlist first", None))
        self.use_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"Use this wordlist", None))
        self.update_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"Update wordlist", None))
        self.delete_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"Delete wordlist", None))
        self.generate_definitions_button.setText(QCoreApplication.translate("MainWindow", u"Generate definitions", None))
        self.new_entry_button.setText(QCoreApplication.translate("MainWindow", u"New entry", None))
        self.wordlist_title.setText(QCoreApplication.translate("MainWindow", u"Your wordlists", None))
        self.selected_entry_title.setText(QCoreApplication.translate("MainWindow", u"Selected word", None))
        self.entry_not_selected_label.setText(QCoreApplication.translate("MainWindow", u"Select a word first", None))
        self.word_label.setText(QCoreApplication.translate("MainWindow", u"Word: <word>", None))
        self.definition_label.setText(QCoreApplication.translate("MainWindow", u"Definition: <definition>", None))
        self.edit_entry_button.setText(QCoreApplication.translate("MainWindow", u"Edit entry", None))
        self.delete_entry_button.setText(QCoreApplication.translate("MainWindow", u"Delete entry", None))
        self.generate_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.new_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"New wordlist", None))
    # retranslateUi

