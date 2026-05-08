import os
import sys

def get_resource_path(relative_path):
    """
    Lấy đường dẫn tài nguyên (tệp UI, hình ảnh) tương thích với cả lúc code lẫn lúc build EXE (PyInstaller).
    Khi chạy exe, PyInstaller sẽ bung data vào thư mục sys._MEIPASS.
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # Vì utils.py nằm ở ngoài nên base_path chỉ cần dirname(__file__) là ra SPCK-Sample
        base_path = os.path.abspath(os.path.dirname(__file__))

    return os.path.join(base_path, relative_path)

def get_data_path(relative_path):
    """
    Lấy đường dẫn dữ liệu json/db.
    Trong exe, thay vì dùng thư mục tạm (bị xóa khi tắt), nó lưu cạnh file exe.
    """
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))
        
    data_dir = os.path.join(base_path, "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    return os.path.join(base_path, relative_path)
