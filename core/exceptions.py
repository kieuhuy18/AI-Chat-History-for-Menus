from core.code import Code

class BusinessException(Exception):
    def __init__(self, error_enum: Code, message: str = None, data: any = None):
        self.code = error_enum.value
        self.message = message or "Đã có lỗi xảy ra" 
        super().__init__(self.message)