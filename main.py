import PySide6.QtWidgets as widgets
import sys

from ui.crossword_window import CrosswordWindow


def main(argv: list[str]):
    app = widgets.QApplication(argv)
    application = CrosswordWindow()
    application.show()
    app.exec()


if __name__ == "__main__":
    main(sys.argv)
