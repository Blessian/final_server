from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Sequence, Optional, Union, cast

from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from domain.robot import robot_schema
from domain.robot.log import robot_log_crud


def create_robot(session: Session, robot: robot_schema.RobotCreate) -> None:
    robot_created: models.Robot = models.Robot()
    session.add(robot_created)
    session.commit()
    session.refresh(robot_created)
    robot_log_crud.create_log(session, robot_created)

def read_all_robots(session: Session) -> List[models.Robot]:
    return session.query(models.Robot).all()

def read_one_robot(session: Session, robot_id: int) -> models.Robot:
    robot_obj: models.Robot = session.get_one(models.Robot, robot_id)
    if not robot_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return robot_obj

def update_robot(session: Session, robot: robot_schema.RobotUpdate) -> models.Robot:
    robot_obj: models.Robot = read_one_robot(session, robot.robot_id)
    for field, value in robot.model_dump(exclude_unset=True).items():
        setattr(robot_obj, field, value)
    session.add(robot_obj)
    session.commit()
    session.refresh(robot_obj)
    return robot_obj

def delete_Robot(session: Session, robot_id: int) -> None:
    robot_obj: models.Robot = read_one_robot(session, robot_id)
    session.delete(robot_obj)
    session.commit()

def get_available_robot_id(session: Session) -> int:
    robot: models.Robot = session.query(models.Robot).order_by(models.Robot.status.asc()).first()
    return robot.robot_id