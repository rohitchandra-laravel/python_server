from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.deps import get_db
from app.schemas.user_schema import UserCreate
from app.services.user_service import create_user, get_users

router = APIRouter()


@router.get("/users")
async def fetch_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)


@router.post("/users")
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db=db, user_data=user)
