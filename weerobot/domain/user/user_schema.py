from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    station_id: int
    password: str
    name: str
    role: str

    class Config:
        from_attributes: bool = True


class UserCreate(BaseModel):
    station_id: int
    password: str
    name: str
    role: str


class UserUpdate(UserCreate):
    user_id: int