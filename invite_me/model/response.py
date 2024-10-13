from uuid import UUID
import datetime as dt

from sqlmodel import SQLModel, Field

from invite_me.model._shared import id_col, created_updated_col


class Response(SQLModel, table=True):
    __tablename__ = "responses"
    id: UUID = id_col()
    request_id: UUID = Field(default=None)
    created_at: dt.datetime = created_updated_col()
    updated_at: dt.datetime = created_updated_col()
