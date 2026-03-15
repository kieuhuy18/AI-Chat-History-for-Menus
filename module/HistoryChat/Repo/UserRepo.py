import logging

# Giả lập database bằng một danh sách
fake_db = [
    {"id": "65e0f1a2b3c4d5e6f7a8b901", "name": "Phở Bò", "price": 50000, "description": "Đặc sản Hà Nội"},
    {"id": "bun", "name": "Bún Chả", "price": 45000, "description": "Bún chả nướng than"}
]

async def get_menu_by_id(menu_id: str):
    logging.info("Check menu id: %s", menu_id)
    if(menu_id == "65e0f1a2b3c4d5e6f7a8b901"):
        return fake_db[0]
    elif(menu_id == "bun"):
        return fake_db[1]
    else:
        return None

    #return next((item for item in fake_db if item["id"] == menu_id), None)