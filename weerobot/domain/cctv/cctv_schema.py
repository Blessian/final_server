from pydantic import BaseModel


class CCTV(BaseModel):
    cctv_id: int
    cctv_idx: int
    latitude: float
    longitude: float

    class Config:
        from_attributes: bool = True


class CCTVCreate(BaseModel):
    cctv_idx: int
    latitude: float
    longitude: float


class CCTVUpdate(CCTVCreate):
    cctv_id: int