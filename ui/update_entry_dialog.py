import PySide6.QtWidgets as widgets

from backend.entry import Entry
from backend.util import ConflictingEntryNameError, EmptyEntryError
from ui_widgets.update_entry_ui import Ui_update_entry_dialog


class UpdateEntryDialog(widgets.QDialog):
    """A dialog window used in entry update."""

    def __init__(self, word: str, parent=None):
        super().__init__(parent)
        self.ui = Ui_update_entry_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)
        self.ui.name.setText(f"Update entry \"{word}\"")

    def __on_accepted(self):
        """Updates the entry's definition."""
        try:
            name = self.parent().selected_entry.word
            definition = self.ui.definition.text()
            entry = Entry(name, definition)
            self.parent().update_entry(entry)
        except (EmptyEntryError, ConflictingEntryNameError) as e:
            widgets.QMessageBox.critical(self, "Error", str(e))
