import os
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from utils import get_resource_path

class UserDialog(QDialog):
    def __init__(self, parent=None, account=None):
        super().__init__(parent)
        ui_path = get_resource_path("gui/user_dialog.ui")
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