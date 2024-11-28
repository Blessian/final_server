from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Sequence, Optional, Union, cast

from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from domain.user import user_schema


def create_user(session: Session, user: user_schema.UserCreate) -> None:
    session.add(models.User(
        station_id=user.station_id,
        password=user.password,
        name=user.name,
        role=user.role
    ))
    session.commit()

def read_all_users(session: Session) -> List[models.User]:
    return session.query(models.User).all()

def read_one_user(session: Session, user_id: int) -> models.User:
    user_obj: models.User = session.get_one(models.User, user_id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return user_obj

def update_user(session: Session, user: user_schema.UserUpdate) -> models.User:
    user_obj: models.User = read_one_user(session, user.user_id)
    for field, value in user.model_dump(exclude_unset=True).items():
        setattr(user_obj, field, value)
    session.add(user_obj)
    session.commit()
    session.refresh(user_obj)
    return user_obj

def delete_user(session: Session, user_id: int) -> None:
    user_obj: models.User = read_one_user(session, user_id)
    session.delete(user_obj)
    session.commit()