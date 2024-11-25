from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.station import station_router
from domain.user import user_router
from domain.cctv import cctv_router
from domain.cctv.log import cctv_log_router
from domain.robot import robot_router
from domain.robot.log import robot_log_router
from domain.robot.log.chat import chat_router


app = FastAPI()

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