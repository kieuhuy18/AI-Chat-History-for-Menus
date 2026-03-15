from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from module.HistoryChat.model.ChatSessionModel import ChatSession
from module.HistoryChat.schema.BaseResponse import ApiResponse

# Response cho chat session
class ChatSessionResponse(BaseModel):
    id: str
    title: str
    createdAt: datetime

    @staticmethod
    def from_model(model: ChatSession):
        return ChatSessionResponse(
            id=model.id,
            title=model.title,
            createdAt=model.createdAt
        )

# Response cho get list chat sessions (có pagination)
class ChatSessionListResponse(ApiResponse[List[ChatSessionResponse]]):
    nextCursor: Optional[str] = None