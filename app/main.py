from fastapi import FastAPI
from core.config import APP_NAME
from module.HistoryChat.Router import ChatSessionRouter
from core.config import connect_to_mongo, close_mongo_connection

app = FastAPI(title = APP_NAME)

app.include_router(ChatSessionRouter.router)

@app.on_event("startup")
async def startup_db():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db():
    await close_mongo_connection()

# @app.get("/")
# def home():
#     return {"message": "Chào mừng đến với ứng dụng Menus!"}

