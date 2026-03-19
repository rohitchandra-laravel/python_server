from sqlalchemy import select

from app.models.user import Post, User


async def get_users(db):
    result = await db.execute(select(User))
    return result.scalars().all()


async def create_user(db, user_data):
    user = User(name=user_data.name, email=user_data.email, age=user_data.age)

    if user.age < 18:
        return {"error": "User must be 18+"}

    dummy_post = Post(title="This Post is written by Kishan")
    user.posts.append(dummy_post)

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user
