class ChatSessionRepository:
    def __init__(self, db):
        self.collection = db.ChatSession

    async def get_all(self, limit: int = 100):
        doc = await self.collection.find().to_list(length=limit)
        return doc
