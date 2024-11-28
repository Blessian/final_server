from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Sequence, Optional, Union, cast

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session
from domain.robot import robot_schema, robot_crud


router: APIRouter = APIRouter(prefix="/weerobot/api/robot")

@router.post("/")
def create_robot(robot: robot_schema.RobotCreate, session: Session=Depends(get_session)) -> None:
    robot_crud.create_robot(session, robot)

@router.get("/", response_model=List[robot_schema.Robot])
def read_all_robots(session: Session=Depends(get_session)) -> List[robot_schema.Robot]:
    return robot_crud.read_all_robots(session)

@router.get("/{robot_id}", response_model=robot_schema.Robot)
def read_one_robot(robot_id: int, session: Session=Depends(get_session)) -> robot_schema.Robot:
    return robot_crud.read_one_robot(session, robot_id)

@router.put("/", response_model=robot_schema.Robot)
def update_robot(robot: robot_schema.RobotUpdate, session: Session=Depends(get_session)) -> robot_schema.Robot:
    return robot_crud.update_robot(session, robot)

@router.delete("/{robot_id}")
def delete_robot(robot_id: int, session: Session=Depends(get_session)) -> None:
    robot_crud.delete_robot(session, robot_id)