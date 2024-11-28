from pydantic import BaseModel


class Robot(BaseModel):
    robot_id: int
    status: int

    class Config:
        from_attributes: bool = True


class RobotCreate(BaseModel):
    pass


class RobotUpdate(RobotCreate):
    robot_id: int
    status: int