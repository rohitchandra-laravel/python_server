import asyncio

from app.database.connection import Base, engine
from app.models.user import Post, User

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(init_db())
