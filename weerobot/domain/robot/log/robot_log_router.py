from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Optional, Union, cast

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session
from domain.robot.log import robot_log_schema, robot_log_crud


router: APIRouter = APIRouter(prefix="/weerobot/api/robot/log")

@router.post("/")
def create_log(robot_log: robot_log_schema.RobotLogCreate, session: Session=Depends(get_session)) -> None:
    robot_log_crud.create_log(session, robot_log)

@router.get("/", response_model=List[robot_log_schema.RobotLog])
def read_all_logs(session: Session=Depends(get_session)) -> List[robot_log_schema.RobotLog]:
    return robot_log_crud.read_all_logs(session)

@router.get("/{log_id}", response_model=robot_log_schema.RobotLog)
def read_one_log(log_id: int, session: Session=Depends(get_session)) -> robot_log_schema.RobotLog:
    return robot_log_crud.read_one_log(session, log_id)

@router.put("/", response_model=robot_log_schema.RobotLog)
def update_log(robot_log: robot_log_schema.RobotLogUpdate, session: Session=Depends(get_session)) -> robot_log_schema.RobotLog:
    return robot_log_crud.update_log(session, robot_log)

@router.delete("/{log_id}")
def delete_log(log_id: int, session: Session=Depends(get_session)) -> None:
    robot_log_crud.delete_log(session, log_id)
    
@router.get("/at/{robot_id}", response_model=List[robot_log_schema.RobotLog])
def read_robot_logs(robot_id: int, session: Session=Depends(get_session)) -> List[robot_log_schema.RobotLog]:
    return robot_log_crud.read_cctv_logs(session, robot_id)