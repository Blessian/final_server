from pydantic import BaseModel


class Station(BaseModel):
    station_id: int
    name: str
    latitude: float
    longitude: float

    class Config:
        from_attributes: bool = True


class StationCreate(BaseModel):
    name: str
    latitude: float
    longitude: float


class StationUpdate(StationCreate):
    station_id: int