from pydantic import BaseModel

from .user import User
from .event import Event


class EventUserCreate(BaseModel):
    event: Event
    user: User

    class Config:
        orm_mode = True


class EventUser(BaseModel):
    event: Event
    user: User

    class Config:
        orm_mode = True
