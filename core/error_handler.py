from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from core.code import Code
from core.exceptions import BusinessException
import logging

# Thiet lap log theo doi loi o server
logger = logging.getLogger(__name__)

# Bat loi nghiep vu
async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        status_code=200,
        content={
            "code": exc.code,
            "message": exc.message
        }
    )

# Bat loi server
async def server_exception_handler(request: Request, exc: Exception):
    logger.error(exc)
    return JSONResponse(
        status_code=200,
        content={
            "code": Code.SERVER_ERROR,
            "message": "Hệ thống đang bận vui lòng thử lại sau"
        }
    )

# Bat loi validation
async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=200,
        content={
            "code": Code.BAD_REQUEST,
            "message": str(exc)
        }
    )

# Bat loi xac thuc
async def http_exception_handler(request: Request, exc: HTTPException):
    code = Code.UNKNOWN
    message = "Lỗi không xác định, vui lòng thử lại sau"

    if exc.status_code == 401:
        code = Code.UNAUTHORIZED
        message = "Đã hết phiên đăng nhập"
    elif exc.status_code == 403:
        code = Code.PERMISSON_DENIED
        message = "Bạn không có quyền truy cập vào tài nguyên này"

    return JSONResponse(
        status_code=200,
        content={
            "code": code,
            "message": message
        }
    )