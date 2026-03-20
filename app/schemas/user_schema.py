from pydantic import BaseModel


# Request (input)
class UserCreate(BaseModel):
    name: str
    email: str
    age: int


# Response (output)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int

    class Config:
        from_attributes = True
