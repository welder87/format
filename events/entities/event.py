from datetime import date

from pydantic import BaseModel

from events.types import EventId
from .user import User


class EventBase(BaseModel):
    name: str
    start_date: date

    class Config:
        orm_mode = True


class EventCreate(EventBase):
    class Config(EventBase.Config):
        pass


class Event(EventBase):
    id: EventId
    users: list[User]

    class Config(EventBase.Config):
        pass
