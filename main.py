import PySide6.QtWidgets as widgets
from crosswords_ui import Ui_MainWindow
from wordlist_window import WordlistWindow


class CrosswordWindow(widgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = widgets.QApplication([])
    application = CrosswordWindow()
    application.show()
    app.exec()


if __name__ == "__main__":
    main()
