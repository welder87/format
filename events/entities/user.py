from pydantic import BaseModel
from pydantic import EmailStr

from events.types import UserId


class UserBase(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    class Config(UserBase.Config):
        pass


class User(UserBase):
    id: UserId

    class Config(UserBase.Config):
        pass
