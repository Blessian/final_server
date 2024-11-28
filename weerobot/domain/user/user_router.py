from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Sequence, Optional, Union, cast

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session
from domain.user import user_schema, user_crud


router: APIRouter = APIRouter(prefix="/weerobot/api/user")

@router.post("/")
def create_user(user: user_schema.UserCreate, session: Session=Depends(get_session)) -> None:
    user_crud.create_user(session, user)

@router.get("/", response_model=List[user_schema.User])
def read_all_users(session: Session=Depends(get_session)) -> List[user_schema.User]:
    return user_crud.read_all_users(session)

@router.get("/{user_id}", response_model=user_schema.User)
def read_one_user(user_id: int, session: Session=Depends(get_session)) -> user_schema.User:
    return user_crud.read_one_user(session, user_id)

@router.put("/", response_model=user_schema.User)
def update_user(user: user_schema.UserUpdate, session: Session=Depends(get_session)) -> user_schema.User:
    return user_crud.update_user(session, user)

@router.delete("/{user_id}")
def delete_user(user_id: int, session: Session=Depends(get_session)) -> None:
    user_crud.delete_user(session, user_id)