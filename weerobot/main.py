from functools import partial

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from gmqtt import Client as MQTTClient
from fastapi_mqtt import FastMQTT, MQTTConfig

from domain.station import station_router
from domain.user import user_router
from domain.cctv import cctv_router
from domain.cctv.log import cctv_log_router
from domain.robot import robot_router
from domain.robot.log import robot_log_router
from domain.robot.log.chat import chat_router
from utilities.mqtt_connection import _lifespan, get_fast_mqtt


fast_mqtt: FastMQTT = get_fast_mqtt()
app = FastAPI(lifespan=partial(_lifespan, fast_mqtt=fast_mqtt))

origins = [
    "http://localhost:94",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(station_router.router)
app.include_router(robot_router.router)
app.include_router(user_router.router)
app.include_router(cctv_router.router)
app.include_router(cctv_log_router.router)
app.include_router(robot_log_router.router)
app.include_router(chat_router.router)


# TEST SETUP
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session
from domain.station import station_schema, station_crud
from domain.robot import robot_schema, robot_crud
from domain.cctv import cctv_schema, cctv_crud

router: APIRouter = APIRouter(prefix="/weerobot/api")

@router.post("/setup")
def setup(session: Session=Depends(get_session)) -> None:
    station_obj: station_schema.StationCreate = station_schema.StationCreate(name="커넥트벨류_센터", latitude=37.5074279, longitude=127.0540188)
    cctv_obj: cctv_schema.CCTVCreate = cctv_schema.CCTVCreate(station_id=1, cctv_idx=0)
    robot_obj: robot_schema.RobotCreate = robot_schema.RobotCreate(station_id=1, hostname="127.0.0.1")

    station_crud.create_station(session, station_obj)
    robot_crud.create_robot(session, robot_obj)
    cctv_crud.create_cctv(session, cctv_obj)

@app.get("/test")
async def func():
    fast_mqtt.publish("/mqtt_blessian", "Hello from Fastapi", 2)  # publishing mqtt topic
    return {"result": True, "message": "Published"}

app.include_router(router)