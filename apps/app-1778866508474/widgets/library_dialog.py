import os
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from utils import get_resource_path


class LibraryDialog(QDialog):
    def __init__(self, parent=None, item=None):
        super().__init__(parent)
        ui_path = get_resource_path("gui/library_dialog.ui")
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
