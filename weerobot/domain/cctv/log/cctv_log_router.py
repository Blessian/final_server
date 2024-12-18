from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Optional, Union, cast

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session
from domain.cctv.log import cctv_log_schema
from domain.cctv.log import cctv_log_crud
from utilities.mqtt_connection import fast_mqtt


router: APIRouter = APIRouter(prefix="/weerobot/api/cctv/log")

@router.post("/")
async def create_log(cctv_log: cctv_log_schema.CCTVLogCreate, session: Session=Depends(get_session)) -> int:
    result_dict: Dict[str, Union[int, float]] = cctv_log_crud.create_log(session, cctv_log)
    fast_mqtt.publish("/weerobot/robot_id/goal", f"{result_dict['x']} {result_dict['y']}", 0)
    return result_dict["robot_id"]

@router.get("/", response_model=List[cctv_log_schema.CCTVLog])
def read_all_logs(session: Session=Depends(get_session)) -> List[cctv_log_schema.CCTVLog]:
    return cctv_log_crud.read_all_logs(session)

@router.get("/{log_id}", response_model=cctv_log_schema.CCTVLog)
def read_one_log(log_id: int, session: Session=Depends(get_session)) -> cctv_log_schema.CCTVLog:
    return cctv_log_crud.read_one_log(session, log_id)

@router.put("/", response_model=cctv_log_schema.CCTVLog)
def update_log(cctv_log: cctv_log_schema.CCTVLogUpdate, session: Session=Depends(get_session)) -> cctv_log_schema.CCTVLog:
    return cctv_log_crud.update_log(session, cctv_log)

@router.delete("/{log_id}")
def delete_log(log_id: int, session: Session=Depends(get_session)) -> None:
    cctv_log_crud.delete_log(session, log_id)

@router.get("/at/{cctv_id}", response_model=List[cctv_log_schema.CCTVLog])
def read_cctv_logs(cctv_id: int, session: Session=Depends(get_session)) -> List[cctv_log_schema.CCTVLog]:
    return cctv_log_crud.read_cctv_logs(session, cctv_id)