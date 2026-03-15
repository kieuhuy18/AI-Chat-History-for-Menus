from fastapi import APIRouter

from module.HistoryChat.service.ChatSessionService import ChatSessionService
from module.HistoryChat.schema.ChatSessionResponseSchema import ChatSessionListResponse, ChatSessionResponse
from module.HistoryChat.schema.BaseResponse import ApiResponse
from module.HistoryChat.schema.ChatSessionRequestSchema import ChatSessionRequest


from core.security import create_access_token
from core.dependencies import get_current_user, get_chat_session_service
from fastapi import Depends, Query
from core.code import Code


router = APIRouter(prefix="/menus", tags=["Menus"])

@router.get("/test")
async def getTest(UserId: str):
    token = create_access_token(id = UserId, subject="pho", role="admin")
    return token

@router.get("/chat/session", response_model=ChatSessionListResponse)
async def getChat(
    keyword: str,
    id: str | None = None,
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    cursor: str | None = None,
    service: ChatSessionService = Depends(get_chat_session_service),
    current_user = Depends(get_current_user)
    ):
    data, nextCursor = await service.get_chat_by_id(userId=current_user["id"], keyword=keyword, limit=limit, cursor=cursor)
    response_data = [ChatSessionResponse.from_model(model) for model in data]
    response = ChatSessionListResponse(code=Code.SUCCESS, message="Success", data=response_data, nextCursor=nextCursor)
    return response

@router.post("/chat/session", response_model=ApiResponse)
async def createChat(
    request: ChatSessionRequest,
    service: ChatSessionService = Depends(get_chat_session_service),
    current_user = Depends(get_current_user)
    ):
    model = await service.create(userId=current_user["id"], request = request)
    response = ApiResponse(code=Code.SUCCESS, message="Thêm dữ liệu thành công", data=ChatSessionResponse.from_model(model))
    return response

@router.patch("/chat/session/{id}", response_model=ApiResponse)
async def updateChat(
    id: str,
    request: ChatSessionRequest,
    service: ChatSessionService = Depends(get_chat_session_service),
    current_user = Depends(get_current_user)
    ):
    model = await service.create(userId=current_user["id"], sessionId = id, request = request)
    response = ApiResponse(code=Code.SUCCESS, message="Thêm dữ liệu thành công", data=ChatSessionResponse.from_model(model))
    return response