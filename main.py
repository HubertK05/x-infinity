import PySide6.QtWidgets as widgets
from wordlist_window import WordlistWindow


def main():
    app = widgets.QApplication([])
    application = WordlistWindow()
    application.show()
    app.exec()


if __name__ == "__main__":
    main()
