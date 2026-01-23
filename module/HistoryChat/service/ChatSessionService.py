from module.HistoryChat.Repo.ChatSessionRepo import ChatSessionRepository
from core.config import db_client
from fastapi import HTTPException

class ChatSessionService:
    @staticmethod
    def get_all_chats():
        listChat = ChatSessionRepository(db_client.db)
        return listChat.get_all()