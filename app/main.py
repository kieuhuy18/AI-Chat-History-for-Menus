from fastapi import FastAPI, HTTPException
from core.config import APP_NAME
from module.HistoryChat.Router import ChatSessionRouter
from core.config import connect_to_mongo, close_mongo_connection
from fastapi.exceptions import RequestValidationError
from core.exceptions import BusinessException
from core.error_handler import business_exception_handler, server_exception_handler, validation_exception_handler, http_exception_handler

app = FastAPI(title = APP_NAME)

app.add_exception_handler(BusinessException, business_exception_handler)
app.add_exception_handler(Exception, server_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)


app.include_router(ChatSessionRouter.router)

@app.on_event("startup")
async def startup_db():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db():
    await close_mongo_connection()


