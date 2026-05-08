import os
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget

from models.account_models import AccountDatabase
from manager_app import ManagerApp
from utils import get_resource_path


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        ui_path = get_resource_path("gui/login_ui.ui")
        uic.loadUi(ui_path, self)
        self.account_db = AccountDatabase()
        self.register_window = None
        self.manager_window = None

        self.btnLogin.clicked.connect(self.login_account)

    def set_register_window(self, register_window):
        self.register_window = register_window
        self.btnGoRegister.clicked.connect(self.open_register)

    def open_register(self):
        if self.register_window is not None:
            self.register_window.show()
            self.hide()

    def login_account(self):
        email = self.txtLoginEmail.text().strip()
        password = self.txtLoginPassword.text()

        if not email or not password:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập email và mật khẩu.")
            return

        # Kiểm tra đăng nhập admin
        if email == "admin@gmail.com" and password == "admin":
            self.manager_window = ManagerApp()
            self.manager_window.show()
            self.hide()
            return

        account = self.account_db.authenticate(email, password)
        if account is None:
            QMessageBox.warning(self, "Đăng nhập thất bại", "Email hoặc mật khẩu không đúng.")
            return

        QMessageBox.information(
            self,
            "Đăng nhập thành công",
            f"Xin chào {account.username} (ID: {account.id})",
        )


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        ui_path = get_resource_path("gui/register_ui.ui")
        uic.loadUi(ui_path, self)
        self.account_db = AccountDatabase()
        self.login_window = None

        self.btnRegister.clicked.connect(self.register_account)

    def set_login_window(self, login_window):
        self.login_window = login_window
        self.btnGoLogin.clicked.connect(self.open_login)

    def open_login(self):
        if self.login_window is not None:
            self.login_window.show()
            self.hide()

    def register_account(self):
        username = self.txtRegisterUsername.text().strip()
        email = self.txtRegisterEmail.text().strip()
        password = self.txtRegisterPassword.text().strip()

        if not username or not email or not password:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ username, email, password.")
            return

        if "@" not in email or "." not in email:
            QMessageBox.warning(self, "Cảnh báo", "Email không hợp lệ.")
            return

        success, message = self.account_db.add_account(username, email, password)
        if not success:
            QMessageBox.warning(self, "Đăng ký thất bại", message)
            return

        QMessageBox.information(self, "Thành công", message)

        self.txtRegisterUsername.clear()
        self.txtRegisterEmail.clear()
        self.txtRegisterPassword.clear()

        if self.login_window is not None:
            self.login_window.txtLoginEmail.setText(email)
            self.login_window.txtLoginPassword.clear()
            self.open_login()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    register_window = RegisterWindow()

    login_window.set_register_window(register_window)
    register_window.set_login_window(login_window)

    login_window.show()
    sys.exit(app.exec())
