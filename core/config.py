import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "FastAPI")
SECRET_KEY = os.getenv("SECRET_KEY", "secret")

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

db_client = MongoDB()

async def connect_to_mongo():
    try:
        db_client.client = AsyncIOMotorClient(
            MONGODB_URL,
            serverSelectionTimeoutMS=3000  # timeout 3s
        )

        # 🔍 ping MongoDB
        await db_client.client.admin.command("ping")

        db_client.db = db_client.client[DATABASE_NAME]
        print("✅ MongoDB connected & ping success")

    except Exception as e:
        print("❌ MongoDB connection failed:", e)
        raise e

async def close_mongo_connection():
    db_client.client.close()
    print("--- Đã đóng kết nối MongoDB ---")