from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from core.config import db_client
from jose import JWTError
import logging
from bson import ObjectId

from core.security import decode_access_token
from module.HistoryChat.Repo.UserRepo import get_menu_by_id
from module.HistoryChat.Repo.ChatSessionRepo import ChatSessionRepository
from module.HistoryChat.service.ChatSessionService import ChatSessionService
from module.User.Repo.PermissionRepo import PermissionRepository
from module.User.service.PermissionService import PermissionService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token_data = decode_access_token(token)
    except JWTError:
        raise credentials_exception

    user_id = token_data.id
    if not user_id:
        raise credentials_exception

    user = await get_menu_by_id(user_id)
    if user is None:
        raise credentials_exception
    return user

def get_chat_session_service():
    repo = ChatSessionRepository(db_client.db)    
    return ChatSessionService(repo)

def get_permission_service():
    repo = PermissionRepository(db_client.db)    
    return PermissionService(repo)