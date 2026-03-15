from datetime import datetime
from bson import ObjectId

from module.HistoryChat.model.ChatSessionModel import ChatSession

class ChatSessionRepository:
    def __init__(self, db):
        self.collection = db.ChatSession
    
    async def get(self, userId: str, keyword: str | None = None, limit: int = 20, cursor: datetime | None = None):
        query = {
            "userId": userId,
            "status": True,
            }
        
        if keyword:
            query["title"] = {
                "$regex": keyword,
                "$options": "i"
            }

        if cursor:
            query["updateAt"] = {"$lt": cursor}

        cursor_db = (
            self.collection
            .find(query)
            .sort("updateAt", -1)
            .limit(limit)
        )

        return await cursor_db.to_list(length=limit)

    # async def getById(self, id: str):
    #     return await cursor_db.to_list(length=limit)

    async def create(self, model: ChatSession) -> ChatSession:
        document = model.model_dump(
            exclude={"id"},      # loại id vì đang None
            exclude_none=True    # bỏ field None
        )

        document["user_id"] = ObjectId(document["user_id"])

        result = await self.collection.insert_one(document)

        model.id = str(result.inserted_id)
        return model
    
    async def update(self, session_id: str, update_data: dict):
        await self.collection.update_one(
            {"_id": ObjectId(session_id)},
            {"$set": update_data}
        )

        return await self.get_by_id(session_id)