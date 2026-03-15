from typing import Optional
from pydantic import BaseModel, Field, field_validator

class ChatSessionRequest(BaseModel):
    title: str = Field(
        ..., # ký hiệu ... ám chỉ đây là trường bắt buộc
        min_length=1,
        max_length=80
    )

    # Đăng ký hàm xóa khoảng trắng đầu và cuối title, đồng thời kiểm tra title có rỗng không
    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str):
        cleaned = v.strip()

        if not cleaned:
            raise ValueError("Title cannot be empty or whitespace")

        return cleaned
    