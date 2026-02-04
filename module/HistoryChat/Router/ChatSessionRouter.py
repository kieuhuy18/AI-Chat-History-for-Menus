from fastapi import APIRouter
from module.HistoryChat.service.ChatSessionService import ChatSessionService
from module.HistoryChat.schema.ChatSessionSchema import ChatSessionListResponse
from module.HistoryChat.model.ChatSessionModel import ChatSession
from core.code import Code


router = APIRouter(prefix="/menus", tags=["Menus"])

@router.get("/", response_model=ChatSessionListResponse)
async def getAll():
    data = await ChatSessionService.get_all_chats()

    response = ChatSessionListResponse(code=Code.SUCCESS, message="Success", data=[ChatSession.from_mongo(item) for item in data])
    return response

@router.get("/test-error")
async def test_error():
    # Chủ động gây lỗi chia cho 0 để kích hoạt Exception
    division_by_zero = 1 / 0 
    return {"message": "Dòng này sẽ không bao giờ chạy"}