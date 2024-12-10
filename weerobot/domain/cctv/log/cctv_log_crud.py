from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Sequence, Optional, Union, cast

from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from domain.cctv.log import cctv_log_schema
from domain.robot import robot_crud


def create_log(session: Session, cctv_log: cctv_log_schema.CCTVLogCreate) -> Dict[str, Union[int, float]]:
    cctv_log: models.CCTVLog = models.CCTVLog(
        cctv_id=cctv_log.cctv_id,
        x=cctv_log.x,
        y=cctv_log.y,
    )
    session.add(cctv_log)
    session.commit()
    session.refresh(cctv_log)
    robot_id: int = robot_crud.get_available_robot_id(session)
    return {"robot_id": robot_id, "x": cctv_log.x, "y": cctv_log.y}

def read_all_logs(session: Session) -> List[cctv_log_schema.CCTVLog]:
    return session.query(models.CCTVLog).order_by(models.CCTVLog.registered.desc()).all()

def read_cctv_logs(session: Session, cctv_id: int) -> List[cctv_log_schema.CCTVLog]:
    return session.query(models.CCTVLog).filter(models.CCTVLog.cctv_id==cctv_id).all()

def read_one_log(session: Session, log_id: int) -> models.CCTVLog:
    log_obj: models.CCTVLog = session.get_one(models.CCTVLog, log_id)
    if not log_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return log_obj

def update_log(session: Session, cctv_log: cctv_log_schema.CCTVLogUpdate) -> models.CCTVLog:
    log_obj: models.CCTVLog = read_one_log(session, cctv_log.log_id)
    for field, value in cctv_log.model_dump(exclude_unset=True).items():
        setattr(log_obj, field, value)
    session.add(log_obj)
    session.commit()
    session.refresh(log_obj)
    return log_obj

def delete_log(session: Session, log_id: int) -> None:
    log_obj: models.CCTVLog = read_one_log(session, log_id)
    session.delete(log_obj)
    session.commit()