from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Optional, Union, cast

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session
from domain.cctv import cctv_schema, cctv_crud


router: APIRouter = APIRouter(prefix="/weerobot/api/cctv")

@router.post("/")
def create_cctv(cctv: cctv_schema.CCTVCreate, session: Session=Depends(get_session)) -> None:
    cctv_crud.create_cctv(session, cctv)

@router.get("/", response_model=List[cctv_schema.CCTV])
def read_all_cctvs(session: Session=Depends(get_session)) -> List[cctv_schema.CCTV]:
    return cctv_crud.read_all_cctvs(session)

@router.get("/{station_id}", response_model=List[cctv_schema.CCTV])
def read_station_cctvs(station_id: int, session: Session=Depends(get_session)) -> List[cctv_schema.CCTV]:
    return cctv_crud.read_station_cctvs(session, station_id)

@router.get("/{cctv_id}", response_model=cctv_schema.CCTV)
def read_one_cctv(cctv_id: int, session: Session=Depends(get_session)) -> cctv_schema.CCTV:
    return cctv_crud.read_one_cctv(session, cctv_id)

@router.put("/", response_model=cctv_schema.CCTV)
def update_cctv(cctv: cctv_schema.CCTVUpdate, session: Session=Depends(get_session)) -> cctv_schema.CCTV:
    return cctv_crud.update_cctv(session, cctv)

@router.delete("/{cctv_id}")
def delete_cctv(cctv_id: int, session: Session=Depends(get_session)) -> None:
    cctv_crud.delete_cctv(session, cctv_id)