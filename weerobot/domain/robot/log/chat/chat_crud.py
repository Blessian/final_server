from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Sequence, Optional, Union, cast

from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from domain.robot.log.chat import chat_schema


def create_log(session: Session, chat_log: chat_schema.ChatLogCreate) -> None:
    session.add(models.ChatLog(
        robot_id=chat_log.robot_id,
        content=chat_log.content
    ))
    session.commit()

def read_chats(session: Session) -> List[chat_schema.ChatLog]:
    return session.query(models.ChatLog).all()

def read_log_chats(session: Session, robot_id: int) -> List[chat_schema.ChatLog]:
    return session.query(models.ChatLog).filter(models.ChatLog.robot_id==robot_id).all()