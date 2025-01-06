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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1211, 809)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)

        self.crossword = QTableWidget(self.centralwidget)
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
        font = QFont()
        font.setFamilies([u"Monospace"])
        font.setPointSize(30)
        self.crossword.setFont(font)
        self.crossword.setLayoutDirection(Qt.LeftToRight)
        self.crossword.setStyleSheet(u"")
        self.crossword.setWordWrap(False)
        self.crossword.setRowCount(10)
        self.crossword.setColumnCount(21)
        self.crossword.horizontalHeader().setVisible(False)
        self.crossword.horizontalHeader().setDefaultSectionSize(40)
        self.crossword.horizontalHeader().setHighlightSections(True)
        self.crossword.verticalHeader().setDefaultSectionSize(52)

        self.verticalLayout_2.addWidget(self.crossword)

        self.definitions = QListWidget(self.centralwidget)
        self.definitions.setObjectName(u"definitions")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.definitions.sizePolicy().hasHeightForWidth())
        self.definitions.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Monospace"])
        font1.setPointSize(16)
        self.definitions.setFont(font1)

        self.verticalLayout_2.addWidget(self.definitions)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.generate_button = QPushButton(self.centralwidget)
        self.generate_button.setObjectName(u"generate_button")

        self.verticalLayout.addWidget(self.generate_button)

        self.solution_input = QLineEdit(self.centralwidget)
        self.solution_input.setObjectName(u"solution_input")

        self.verticalLayout.addWidget(self.solution_input)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1211, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Crossword based on wordlist <wordlist>", None))

        __sortingEnabled = self.crossword.isSortingEnabled()
        self.crossword.setSortingEnabled(False)
        self.crossword.setSortingEnabled(__sortingEnabled)

        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"New crossword", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select wordlist", None))
    # retranslateUi

