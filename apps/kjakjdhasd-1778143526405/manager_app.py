from models.account_models import AccountDatabase
from widgets.user_dialog import UserDialog
import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic


class ManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Since manager_app.py is in root, path to gui/ is direct
        ui_path = os.path.join(os.path.dirname(__file__), "gui", "crud_main.ui")
        uic.loadUi(ui_path, self)

        # Databases
        self.account_db = AccountDatabase()

        # Navigation Connections
        self.btnNavUser.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btnNavLibrary.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        
        # Account Actions
        self.btnAddAcc.clicked.connect(self.add_account)
        self.btnEditAcc.clicked.connect(self.edit_account)
        self.btnDelAcc.clicked.connect(self.delete_account)


        # Initial Load
        self.refresh_accounts()

    def refresh_accounts(self):
        self.accountList.clear()
        self.account_db.load_data()
        for acc in self.account_db.account_item_list:
            display = f"ID: {acc.id} | {acc.username} ({acc.email})"
            self.accountList.addItem(display)

    # --- Account CRUD ---
    def add_account(self):
        dialog = UserDialog(self)
        if dialog.exec():
            data = dialog.get_data()
            success, message = self.account_db.add_account(data['username'], data['email'], data['password'])
            if success:
                QMessageBox.information(self, "Thành công", message)
                self.refresh_accounts()
            else:
                QMessageBox.warning(self, "Lỗi", message)

    def edit_account(self):
        row = self.accountList.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Chú ý", "Vui lòng chọn tài khoản.")
            return
        
        acc = self.account_db.account_item_list[row]
        dialog = UserDialog(self, acc)
        if dialog.exec():
            data = dialog.get_data()
            success, message = self.account_db.update_account(acc.id, data['username'], data['email'], data['password'])
            if success:
                QMessageBox.information(self, "Thành công", message)
                self.refresh_accounts()
            else:
                QMessageBox.warning(self, "Lỗi", message)

    def delete_account(self):
        row = self.accountList.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Chú ý", "Vui lòng chọn tài khoản.")
            return
        
        acc = self.account_db.account_item_list[row]
        if QMessageBox.question(self, "Xác nhận", f"Xóa tài khoản {acc.username}?") == QMessageBox.StandardButton.Yes:
            success, message = self.account_db.delete_account(acc.id)
            if success:
                QMessageBox.information(self, "Thành công", message)
                self.refresh_accounts()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManagerApp()
    window.show()
    sys.exit(app.exec())
