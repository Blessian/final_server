from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Sequence, Optional, Union, cast

from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from domain.robot.log import robot_log_schema


def create_log(session: Session, robot_log: robot_log_schema.RobotLogCreate) -> None:
    session.add(models.RobotLog(
        robot_id=robot_log.robot_id
    ))
    session.commit()

def read_all_logs(session: Session) -> List[robot_log_schema.RobotLog]:
    return session.query(models.RobotLog).all()

def read_robot_logs(session: Session, robot_id: int) -> List[robot_log_schema.RobotLog]:
    return session.query(models.RobotLog).filter(models.RobotLog.robot_id==robot_id).all()

def read_one_log(session: Session, log_id: int) -> models.RobotLog:
    log_obj: models.RobotLog = session.get_one(models.RobotLog, log_id)
    if not log_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return log_obj

def update_log(session: Session, robot_log: robot_log_schema.RobotLogUpdate) -> models.RobotLog:
    log_obj: models.RobotLog = read_one_log(session, robot_log.log_id)
    for field, value in robot_log.model_dump(exclude_unset=True).items():
        setattr(log_obj, field, value)
    session.add(log_obj)
    session.commit()
    session.refresh(log_obj)
    return log_obj

def delete_log(session: Session, log_id: int) -> None:
    log_obj: models.RobotLog = read_one_log(session, log_id)
    session.delete(log_obj)
    session.commit()