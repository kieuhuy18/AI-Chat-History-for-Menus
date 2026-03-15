from bson import ObjectId
from bson.errors import InvalidId
from datetime import datetime

from core.code import Code
from core.exceptions import BusinessException

from module.HistoryChat.Repo.ChatSessionRepo import ChatSessionRepository
from module.HistoryChat.model.ChatSessionModel import ChatSession
from module.HistoryChat.schema.ChatSessionRequestSchema import ChatSessionRequest

class ChatSessionService:
    def __init__(self, repo: ChatSessionRepository):
        self.repo = repo
    
    async def get_chat_by_id(
        self,
        userId: str,
        keyword: str | None = None,
        limit: int = 20,
        cursor: str | None = None
    ):
        try:
            userId = ObjectId(userId)
        except InvalidId:
            raise BusinessException(
                error_enum=Code.NOT_FOUND,
                message="Không tìm thấy tài khoản"
            )
        
        if cursor:
            cursor = datetime.fromisoformat(cursor)

        data = await self.repo.get(
            userId=userId,
            keyword=keyword,
            limit=limit,
            cursor=cursor
        )

        result = [ChatSession.from_mongo(item) for item in data]

        next_cursor = None
        if data:
            next_cursor = data[-1]["updateAt"].isoformat()
        
        return result, next_cursor
    
    async def create(self, userId:str, request: ChatSessionRequest) -> ChatSession:
        model = ChatSession(
            user_id=userId,
            title=request.title,
            contextSumary=request.contextSumary, 
            createdAt=datetime.now(),
            updateAt=datetime.now(),
            status=True
        )
        return await self.repo.create(model)
    
    async def update(self, userId:str, sessionID:str, request: ChatSessionRequest) -> ChatSession:
        update_data = {
            "title": request.title,
            "updateAt": datetime.now()
        }
        return await self.repo.update(request.session_id, update_data)