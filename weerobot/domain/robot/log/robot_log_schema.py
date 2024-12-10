from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class RobotLog(BaseModel):
    log_id: int
    robot_id: int
    video_address: Optional[str]
    status: int
    registered: datetime

    class Config:
        from_attributes: bool = True


class RobotLogCreate(BaseModel):
    robot_id: int


class RobotLogUpdate(RobotLogCreate):
    log_id: int
    video_address: str
    status: int