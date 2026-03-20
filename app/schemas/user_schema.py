from typing import Optional
from pydantic import BaseModel


# Request (input)
class UserCreate(BaseModel):
    name: str
    email: str
    age: int


# Update Request (intput)
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None


# Response (output)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int

    class Config:
        from_attributes = True
