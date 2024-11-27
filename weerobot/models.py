from datetime import datetime, timezone

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Station(Base):
    __tablename__: str = "station"

    station_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    latitude: Mapped[float] = mapped_column(nullable=False)
    longitude: Mapped[float] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"Station(station_id={self.station_id!r}, \
            name={self.name!r}, \
            latitude={self.latitude!r}, \
            longitude={self.longitude!r})"


class User(Base):
    __tablename__: str = "user"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    station_id: Mapped[int] = mapped_column(ForeignKey("station.station_id"), nullable=False)
    passoword: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False, default="common")
    station: Mapped[Station] = relationship(backref="station")

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, \
            station_id={self.cctv_id!r}, \
            passoword={self.passoword!r}, \
            name={self.name!r}, \
            role={self.role!r})"


class Robot(Base):
    __tablename__: str = "robot"

    robot_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    station_id: Mapped[int] = mapped_column(ForeignKey("station.station_id"), nullable=False)
    hostname: Mapped[str] = mapped_column(String(50), nullable=False)
    station: Mapped[Station] = relationship(backref="robot")

    def __repr__(self) -> str:
        return f"Robot(robot_id={self.robot_id!r}, \
            station_id={self.station_id!r}, \
            hostname={self.hostname!r}"


class RobotLog(Base):
    __tablename__: str = "robot_log"
    
    log_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    robot_id: Mapped[int] = mapped_column(ForeignKey("robot.robot_id"), nullable=False)
    video_address: Mapped[str] = mapped_column(String(500), nullable=True)
    status: Mapped[int] = mapped_column(nullable=False, default=0)
    registerd: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(tz=timezone.utc), nullable=False)
    robot: Mapped[Robot] = relationship(backref="robot_log")

    def __repr__(self) -> str:
        return f"RobotLog(log_id={self.log_id!r}, \
            robot_id={self.robot_id!r}, \
            video_address={self.video_address!r}, \
            status={self.status!r}, \
            registerd={self.registerd!r})"


class ChatLog(Base):
    __tablename__: str = "chat_log"

    log_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    robot_log_id: Mapped[int] = mapped_column(ForeignKey("robot_log.log_id"), nullable=False)
    content: Mapped[str] = mapped_column(String(1000), nullable=True)
    robot_log: Mapped[RobotLog] = relationship(backref="chat_log")

    def __repr__(self) -> str:
        return f"ChatLog(log_id={self.call_log_id!r}, \
            log_id={self.log_id!r}, \
            robot_id={self.robot_id!r}, \
            content={self.content!r})"


class CCTV(Base):
    __tablename__: str = "cctv"

    cctv_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    station_id: Mapped[int] = mapped_column(ForeignKey("station.station_id"), nullable=False)
    cctv_idx: Mapped[int] = mapped_column(nullable=False)
    station: Mapped[Station] = relationship(backref="cctv")

    def __repr__(self) -> str:
        return f"CCTV(cctv_id={self.cctv_id!r}, \
            station_id={self.station_id!r}, \
            cctv_idx={self.cctv_idx!r}"


class CCTVLog(Base):
    __tablename__: str = "cctv_log"

    log_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cctv_id: Mapped[int] = mapped_column(ForeignKey("cctv.cctv_id"), nullable=False)
    video_address: Mapped[str] = mapped_column(String(500), nullable=True)
    registerd: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(tz=timezone.utc), nullable=False)
    x: Mapped[float] = mapped_column(nullable=False)
    y: Mapped[float] = mapped_column(nullable=False)
    cctv: Mapped[CCTV] = relationship(backref="cctv_log")
    
    def __repr__(self) -> str:
        return f"CCTVLog(log_id={self.log_id!r}, \
            cctv_id={self.cctv_id!r}, \
            video_address={self.video_address!r}, \
            registerd={self.registerd!r}), \
            x={self.x!r}, \
            y={self.y!r}"