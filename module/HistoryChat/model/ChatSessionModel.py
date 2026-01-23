from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class ChatMessage(BaseModel):
    _id: str
    sessionId: str
    sender: bool #true: user, false: AI
    content: str

class ChatSession(BaseModel):
    _id: str
    user_id: str
    title: str
    contextSumary: str
    createdAt: datetime

    @staticmethod
    def from_mongo(doc: dict) -> "ChatSession":
        return ChatSession(
            _id=str(doc["_id"]),
            user_id=str(doc["userId"]),   
            title=doc["title"],
            contextSumary=doc.get("contextSumary", ""),
            createdAt=doc["createdAt"]
        )

