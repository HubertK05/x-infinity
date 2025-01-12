import PySide6.QtWidgets as widgets

from backend.entry import Entry
from backend.util import ConflictingEntryNameError, EmptyEntryError
from ui_widgets.new_entry_ui import Ui_new_entry_dialog


class NewEntryDialog(widgets.QDialog):
    """A dialog window used in entry creation."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_new_entry_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)

    def __on_accepted(self):
        """Creates a new entry."""
        try:
            entry = Entry(self.ui.word.text(), self.ui.definition.text())
            self.parent().add_entry(entry)
        except (EmptyEntryError, ConflictingEntryNameError) as e:
            widgets.QMessageBox.critical(self, "Error", str(e))
