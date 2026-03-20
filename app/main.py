from fastapi import FastAPI

from app.handlers import register_exception_handlers
from app.routers.user_router import router as user_router

app = FastAPI()

register_exception_handlers(app)
app.include_router(user_router)
