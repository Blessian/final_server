from datetime import datetime

from pydantic import BaseModel


class CCTVLog(BaseModel):
    log_id: int
    cctv_id: int
    vidio_address: str
    registered: datetime

    class Config:
        from_attributes: bool = True


class CCTVLogCreate(BaseModel):
    cctv_id: int


class CCTVLogUpdate(CCTVLogCreate):
    log_id: int
    vidio_address: str