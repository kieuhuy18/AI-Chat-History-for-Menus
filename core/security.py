from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, status
import os

from pydantic import BaseModel
from typing import Optional

APP_NAME = os.getenv("APP_NAME", "FastAPI")

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCES_TOKEN_EXPIRE_MINUTES", 30))

class Token(BaseModel):
    id: Optional[str] = None
    exp: Optional[datetime] = None
    role: Optional[str] = None

def create_access_token(
    *,
    id: str,
    subject: str,
    role: str
) -> str:
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "id": id,
        "sub": subject,
        "iat": now,
        "exp": expire,
        "role": role
    }

    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Token:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("id")
        if id is None:
            raise JWTError

        return Token(
            id = id,
            exp = payload.get("exp"),
            role = payload.get("role")
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )