from pydantic import BaseModel


class Robot(BaseModel):
    robot_id: int
    station_id: int
    hostname: str

    class Config:
        from_attributes: bool = True


class RobotCreate(BaseModel):
    station_id: int
    hostname: str


class RobotUpdate(RobotCreate):
    robot_id: int