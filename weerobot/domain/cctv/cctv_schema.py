from pydantic import BaseModel


class CCTV(BaseModel):
    cctv_id: int
    station_id: int
    cctv_idx: int

    class Config:
        from_attributes: bool = True


class CCTVCreate(BaseModel):
    station_id: int
    cctv_idx: int


class CCTVUpdate(CCTVCreate):
    cctv_id: int