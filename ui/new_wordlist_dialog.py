import PySide6.QtWidgets as widgets

from backend.util import InvalidWordlistNameError
from ui_widgets.new_wordlist_ui import Ui_new_wordlist_dialog


class CreateWordlistDialog(widgets.QDialog):
    """A dialog window used in wordlist creation."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_new_wordlist_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)

    def __on_accepted(self):
        """Creates a new wordlist."""
        try:
            self.parent().create_wordlist(self.ui.name.text())
        except InvalidWordlistNameError as e:
            widgets.QMessageBox.critical(self, "Error", str(e))
