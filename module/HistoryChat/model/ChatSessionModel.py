from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class ChatMessage(BaseModel):
    _id: str
    sessionId: str
    sender: bool #true: user, false: AI
    content: str

class ChatSession(BaseModel):
    id: str | None = None
    user_id: str
    title: str
    contextSumary: str | None = None
    createdAt: datetime
    updateAt: datetime | None = None
    status: bool | None = None

    @staticmethod
    def from_mongo(doc: dict) -> "ChatSession":
        return ChatSession(
            _id=str(doc["_id"]),
            user_id=str(doc["userId"]),   
            title=doc["title"],
            contextSumary=doc["contextSummary"],
            createdAt=doc["createdAt"],
            updateAt=doc["updateAt"],
            status=doc["status"]
        )

