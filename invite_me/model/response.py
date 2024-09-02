from uuid import UUID

from sqlmodel import SQLModel, Field

from invite_me.model._shared import id_col


class Response(SQLModel, table=True):
    __tablename__ = "responses"
    id: UUID = id_col()
    request_id: UUID = Field(default=None)
