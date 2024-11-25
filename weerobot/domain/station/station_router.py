from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Sequence, Optional, Union, cast

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from database import get_session
from domain.station import station_schema, station_crud


router: APIRouter = APIRouter(prefix="/weerobot/api/station")

@router.post("/")
def create_station(station: station_schema.StationCreate, session: Session=Depends(get_session)) -> None:
    station_crud.create_station(session, station)

@router.get("/", response_model=List[station_schema.Station])
def read_all_stations(session: Session=Depends(get_session)) -> List[station_schema.Station]:
    return station_crud.read_all_stations(session)

@router.get("/{station_id}", response_model=station_schema.Station)
def read_one_station(station_id: int, session: Session=Depends(get_session)) -> station_schema.Station:
    return station_crud.read_one_station(session, station_id)

@router.put("/", response_model=station_schema.Station)
def update_station(station: station_schema.StationUpdate, session: Session=Depends(get_session)) -> station_schema.Station:
    return station_crud.update_station(session, station)

@router.delete("/{station_id}")
def delete_station(station_id: int, session: Session=Depends(get_session)) -> None:
    station_crud.delete_station(session, station_id)