from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    password: str
    name: str
    role: str

    class Config:
        from_attributes: bool = True


class UserCreate(BaseModel):
    password: str
    name: str
    role: str


class UserUpdate(UserCreate):
    user_id: int