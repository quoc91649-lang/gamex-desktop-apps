import os
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class UserDialog(QDialog):
    def __init__(self, parent=None, account=None):
        super().__init__(parent)
        # UI path relative to this file's position (widgets/user_dialog.py)
        ui_path = os.path.join(os.path.dirname(__file__), "..", "gui", "user_dialog.ui")
        uic.loadUi(ui_path, self)
        self.account = account

        if self.account:
            self.txtUsername.setText(self.account.username)
            self.txtEmail.setText(self.account.email)
            self.txtPassword.setText(self.account.password)

    def get_data(self):
        return {
            "username": self.txtUsername.text().strip(),
            "email": self.txtEmail.text().strip(),
            "password": self.txtPassword.text().strip(),
        }