from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.exceptions.user import UserNotFoundError, UserValidationError
from app.models.user import Post, User


async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()


async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise UserNotFoundError()
    return user


async def create_user(db: AsyncSession, user_data):
    user = User(name=user_data.name, email=user_data.email, age=user_data.age)

    if user.age < 18:
        raise UserValidationError("User must be 18+")

    dummy_post = Post(title="This Post is written by Kishan")
    user.posts.append(dummy_post)

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user
