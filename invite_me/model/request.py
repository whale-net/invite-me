from enum import Enum, auto
from uuid import UUID

from sqlmodel import SQLModel, Field

from invite_me.model._shared import id_col, created_updated_col
import datetime as dt

class RequestRecipient(SQLModel, table=True):
    __tablename__ = "request_recipients"
    id: UUID = id_col()
    request_id: UUID = Field(default=None, foreign_key="requests.id")
    to_user_id: UUID = Field(default=None, foreign_key="users.id")

    created_at: dt.datetime = created_updated_col()
    updated_at: dt.datetime = created_updated_col()

class RequestState_(Enum):
    INITIALIZED = auto()


class RequestState(SQLModel, table=True):
    __tablename__ = "request_states"
    id: UUID = id_col()
    name: str = Field(default=None)

class Request(SQLModel, table=True):
    __tablename__ = "requests"
    id: UUID = id_col()
    from_user: UUID = Field(default=None, foreign_key="users.id")
    request_body: str = Field(default=None)
    request_state_id: UUID = Field(default=None, foreign_key="request_states.id")
    created_at: dt.datetime = created_updated_col()
    updated_at: dt.datetime = created_updated_col()
