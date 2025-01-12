# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crosswords.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTableWidgetItem, QVBoxLayout, QWidget)

from ui.crossword_table import CrosswordTable

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1330, 1099)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.crossword_pages = QStackedWidget(self.centralwidget)
        self.crossword_pages.setObjectName(u"crossword_pages")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.no_crossword_label = QLabel(self.page)
        self.no_crossword_label.setObjectName(u"no_crossword_label")
        font = QFont()
        font.setPointSize(30)
        self.no_crossword_label.setFont(font)
        self.no_crossword_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.no_crossword_label)

        self.crossword_pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title = QLabel(self.page_2)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.title)

        self.crossword = CrosswordTable(self.page_2)
        if (self.crossword.columnCount() < 21):
            self.crossword.setColumnCount(21)
        if (self.crossword.rowCount() < 10):
            self.crossword.setRowCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.crossword.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.crossword.setItem(1, 0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.crossword.setItem(2, 0, __qtablewidgetitem2)
        self.crossword.setObjectName(u"crossword")
        self.crossword.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Monospace"])
        font1.setPointSize(30)
        self.crossword.setFont(font1)
        self.crossword.setLayoutDirection(Qt.LeftToRight)
        self.crossword.setStyleSheet(u"")
        self.crossword.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.crossword.setWordWrap(False)
        self.crossword.setRowCount(10)
        self.crossword.setColumnCount(21)
        self.crossword.horizontalHeader().setVisible(False)
        self.crossword.horizontalHeader().setDefaultSectionSize(40)
        self.crossword.horizontalHeader().setHighlightSections(True)
        self.crossword.verticalHeader().setDefaultSectionSize(52)

        self.verticalLayout_3.addWidget(self.crossword)

        self.definitions = QListWidget(self.page_2)
        self.definitions.setObjectName(u"definitions")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.definitions.sizePolicy().hasHeightForWidth())
        self.definitions.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Monospace"])
        font2.setPointSize(16)
        self.definitions.setFont(font2)
        self.definitions.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.definitions)

        self.check_answer_button = QPushButton(self.page_2)
        self.check_answer_button.setObjectName(u"check_answer_button")

        self.verticalLayout_3.addWidget(self.check_answer_button)

        self.crossword_pages.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.crossword_pages)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.generate_button = QPushButton(self.centralwidget)
        self.generate_button.setObjectName(u"generate_button")

        self.verticalLayout.addWidget(self.generate_button)

        self.solution_input = QLineEdit(self.centralwidget)
        self.solution_input.setObjectName(u"solution_input")

        self.verticalLayout.addWidget(self.solution_input)

        self.select_wordlist_button = QPushButton(self.centralwidget)
        self.select_wordlist_button.setObjectName(u"select_wordlist_button")

        self.verticalLayout.addWidget(self.select_wordlist_button)

        self.selected_wordlist_label = QLabel(self.centralwidget)
        self.selected_wordlist_label.setObjectName(u"selected_wordlist_label")
        self.selected_wordlist_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.selected_wordlist_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.crossword_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Crossword", None))
        self.no_crossword_label.setText(QCoreApplication.translate("MainWindow", u"Select a wordlist and create a crossword", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Crossword based on wordlist <wordlist>", None))

        __sortingEnabled = self.crossword.isSortingEnabled()
        self.crossword.setSortingEnabled(False)
        self.crossword.setSortingEnabled(__sortingEnabled)

        self.check_answer_button.setText(QCoreApplication.translate("MainWindow", u"Check your answer", None))
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"New crossword", None))
        self.solution_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Solution word to base the crossword on...", None))
        self.select_wordlist_button.setText(QCoreApplication.translate("MainWindow", u"Select wordlist", None))
        self.selected_wordlist_label.setText(QCoreApplication.translate("MainWindow", u"Selected wordlist: None", None))
    # retranslateUi

