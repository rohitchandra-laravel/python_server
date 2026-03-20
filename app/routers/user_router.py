from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.deps import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import create_user, get_user_by_id, get_users

router = APIRouter()


@router.get("/users", response_model=List[UserResponse])
async def fetch_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)


@router.get("/users/{id}", response_model=UserResponse)
async def fetch_user_by_id(id: int, db: AsyncSession = Depends(get_db)):
    return await get_user_by_id(db, id)


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db=db, user_data=user)
