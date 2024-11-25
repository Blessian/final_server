from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Sequence, Optional, Union, cast

from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from domain.station import station_schema


def create_station(session: Session, station: station_schema.StationCreate) -> None:
    session.add(models.Station(
        name=station.name,
        latitude=station.latitude,
        longitude=station.longitude
    ))
    session.commit()

def read_all_stations(session: Session) -> List[models.Station]:
    return session.query(models.Station).all()

def read_one_station(session: Session, station_id: int) -> models.Station:
    station_obj: models.Station = session.get_one(models.Station, station_id)
    if not station_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return station_obj

def update_station(session: Session, station: station_schema.StationUpdate) -> models.Station:
    station_obj: models.Station = read_one_station(session, station.station_id)
    for field, value in station.model_dump(exclude_unset=True).items():
        setattr(station_obj, field, value)
    session.add(station_obj)
    session.commit()
    session.refresh(station_obj)
    return station_obj

def delete_station(session: Session, station_id: int) -> None:
    station_obj: models.Station = read_one_station(session, station_id)
    session.delete(station_obj)
    session.commit()