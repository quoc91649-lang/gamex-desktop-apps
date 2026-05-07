import os
import sys

# Add the parent directory to sys.path to allow running this script directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data import data_io


class AccountItem:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password


class AccountDatabase:
    def __init__(self):
        self.account_item_list = []
        self.data_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "data", "Accounts.json")
        )

    def load_data(self):
        account_dict_data = data_io.load_json_data(self.data_file)
        self.account_item_list.clear() # Clear existing items before reloading
        for account_dict in account_dict_data:
            account = AccountItem(
                id=account_dict.get("id"),
                username=account_dict.get("username", ""),
                email=account_dict.get("email", ""),
                password=account_dict.get("password", ""),
            )
            self.account_item_list.append(account)


    def authenticate(self, email, password):
        self.load_data()
        email = email.strip().lower()
        password = password.strip()
        for account in self.account_item_list:
            if account.email.strip().lower() == email and account.password == password:
                return account
        return None

    def add_account(self, username, email, password):
        username = username.strip()
        email = email.strip()
        password = password.strip()

        account_dict_data = data_io.load_json_data(self.data_file)
        normalized_email = email.lower()

        for account_dict in account_dict_data:
            saved_email = str(account_dict.get("email", "")).strip().lower()
            if saved_email == normalized_email:
                return False, "Email đã tồn tại."

        max_id = 0
        for account_dict in account_dict_data:
            account_id = account_dict.get("id", 0)
            if isinstance(account_id, int) and account_id > max_id:
                max_id = account_id

        account_dict_data.append(
            {
                "id": max_id + 1,
                "username": username,
                "email": email,
                "password": password,
            }
        )

        data_io.write_json_data(account_dict_data, self.data_file)
        self.load_data()
        return True, "Đăng ký thành công."

    def update_account(self, account_id, username, email, password):
        account_dict_data = data_io.load_json_data(self.data_file)
        found = False
        for i, acc in enumerate(account_dict_data):
            if acc.get("id") == account_id:
                account_dict_data[i]["username"] = username.strip()
                account_dict_data[i]["email"] = email.strip()
                account_dict_data[i]["password"] = password.strip()
                found = True
                break
        
        if found:
            data_io.write_json_data(account_dict_data, self.data_file)
            self.load_data()
            return True, "Cập nhật thành công."
        return False, "Không tìm thấy tài khoản."

    def delete_account(self, account_id):
        account_dict_data = data_io.load_json_data(self.data_file)
        new_account_data = [acc for acc in account_dict_data if acc.get("id") != account_id]
        
        if len(new_account_data) < len(account_dict_data):
            data_io.write_json_data(new_account_data, self.data_file)
            self.load_data()
            return True, "Xóa thành công."
        return False, "Không tìm thấy tài khoản."