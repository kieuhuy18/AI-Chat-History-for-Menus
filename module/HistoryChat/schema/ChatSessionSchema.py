from typing import List
from module.HistoryChat.model.ChatSessionModel import ChatSession
from module.HistoryChat.schema.BaseResponse import ApiResponse

class ChatSessionListResponse(ApiResponse[List[ChatSession]]):
    pass