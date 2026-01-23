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