import PySide6.QtWidgets as widgets

from backend.util import InvalidWordlistNameError
from ui_widgets.update_wordlist_ui import Ui_update_wordlist_dialog


class UpdateWordlistDialog(widgets.QDialog):
    """A dialog window used in wordlist update."""

    def __init__(self, name: str, parent=None):
        super().__init__(parent)
        self.ui = Ui_update_wordlist_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)
        self.ui.old_name.setText(f"Update wordlist \"{name}\"")

    def __on_accepted(self):
        """Updates the wordlist's name."""
        try:
            self.parent().rename_wordlist(self.parent().selected_wordlist.name, self.ui.new_name.text())
        except InvalidWordlistNameError as e:
            widgets.QMessageBox.critical(self, "Error", str(e))
