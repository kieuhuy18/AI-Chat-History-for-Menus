# Giả lập database bằng một danh sách
fake_db = [
    {"id": 1, "name": "Phở Bò", "price": 50000, "description": "Đặc sản Hà Nội"},
    {"id": 2, "name": "Bún Chả", "price": 45000, "description": "Bún chả nướng than"}
]

def get_menu_by_id(menu_id: int):
    # Trong thực tế, đây là nơi gọi db.query(...)
    return next((item for item in fake_db if item["id"] == menu_id), None)