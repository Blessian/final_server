from datetime import datetime

from pydantic import BaseModel


class ChatLog(BaseModel):
    log_id: int
    robot_id: int
    registered: datetime
    content: str

    class Config:
        from_attributes: bool = True


class ChatLogCreate(BaseModel):
    robot_id: int
    content: str