import os
from data import data_io
from utils import get_data_path


class LibraryItem:
    def __init__(self, id, title, author, category):
        self.id = id
        self.title = title
        self.author = author
        self.category = category


class LibraryDatabase:
    def __init__(self):
        self.library_item_list = []
        self.data_file = get_data_path("data/Library.json")

    def load_data(self):
        self.library_item_list = []
        library_dict_data = data_io.load_json_data(self.data_file)

        for item_dict in library_dict_data:
            item = LibraryItem(
                id=item_dict.get("id"),
                title=item_dict.get("title", ""),
                author=item_dict.get("author", ""),
                category=item_dict.get("category", ""),
            )
            self.library_item_list.append(item)
        return self.library_item_list

    def add_item(self, title, author, category):
        title = title.strip()
        author = author.strip()
        category = category.strip()

        if not title:
            return False, "Tiêu đề không được để trống."

        items_data = data_io.load_json_data(self.data_file)
        
        max_id = 0
        for item in items_data:
            id_val = item.get("id", 0)
            if isinstance(id_val, int) and id_val > max_id:
                max_id = id_val

        new_item = {
            "id": max_id + 1,
            "title": title,
            "author": author,
            "category": category,
        }
        items_data.append(new_item)
        data_io.write_json_data(items_data, self.data_file)
        self.load_data()
        return True, "Thêm thành công."

    def update_item(self, item_id, title, author, category):
        items_data = data_io.load_json_data(self.data_file)
        found = False
        for i, item in enumerate(items_data):
            if item.get("id") == item_id:
                items_data[i]["title"] = title.strip()
                items_data[i]["author"] = author.strip()
                items_data[i]["category"] = category.strip()
                found = True
                break
        
        if found:
            data_io.write_json_data(items_data, self.data_file)
            self.load_data()
            return True, "Cập nhật thành công."
        return False, "Không tìm thấy vật phẩm."

    def delete_item(self, item_id):
        items_data = data_io.load_json_data(self.data_file)
        new_items_data = [item for item in items_data if item.get("id") != item_id]
        
        if len(new_items_data) < len(items_data):
            data_io.write_json_data(new_items_data, self.data_file)
            self.load_data()
            return True, "Xóa thành công."
        return False, "Không tìm thấy vật phẩm."
