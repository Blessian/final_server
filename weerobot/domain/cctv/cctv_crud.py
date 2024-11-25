from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Sequence, Optional, Union, cast

from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from domain.cctv import cctv_schema


def create_cctv(session: Session, cctv: cctv_schema.CCTV) -> None:
    session.add(models.CCTV(
        station_id=cctv.station_id,
        cctv_idx=cctv.cctv_idx
    ))
    session.commit()

def read_all_cctvs(session: Session) -> List[cctv_schema.CCTV]:
    return session.query(models.CCTV).all()

def read_station_cctvs(session: Session, station_id: int) -> List[cctv_schema.CCTV]:
    return session.query(models.CCTV).filter(models.CCTV.station_id==station_id).all()

def read_one_cctv(session: Session, cctv_id: int) -> models.CCTV:
    cctv_obj: models.CCTV = session.get_one(models.CCTV, cctv_id)
    if not cctv_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return cctv_obj

def update_cctv(session: Session, cctv: cctv_schema.CCTVUpdate) -> models.CCTV:
    cctv_obj: models.CCTV = read_one_cctv(session, cctv.cctv_id)
    for field, value in cctv.model_dump(exclude_unset=True).items():
        setattr(cctv_obj, field, value)
    session.add(cctv_obj)
    session.commit()
    session.refresh(cctv_obj)
    return cctv_obj

def delete_cctv(session: Session, cctv_id: int) -> None:
    cctv_obj: models.CCTV = read_one_cctv(session, cctv_id)
    session.delete(cctv_obj)
    session.commit()