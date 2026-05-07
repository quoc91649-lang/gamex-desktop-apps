import os
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog


class LibraryDialog(QDialog):
    def __init__(self, parent=None, item=None):
        super().__init__(parent)
        # UI path relative to this file's position (widgets/library_dialog.py)
        ui_path = os.path.join(os.path.dirname(__file__), "..", "gui", "library_dialog.ui")
        uic.loadUi(ui_path, self)
        self.item = item

        if self.item:
            self.txtTitle.setText(self.item.title)
            self.txtAuthor.setText(self.item.author)
            self.txtCategory.setText(self.item.category)

    def get_data(self):
        return {
            "title": self.txtTitle.text().strip(),
            "author": self.txtAuthor.text().strip(),
            "category": self.txtCategory.text().strip(),
        }
