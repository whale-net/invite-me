from uuid import UUID

from sqlmodel import SQLModel, Field

from invite_me.model._shared import id_col


class Request(SQLModel, table=True):
    __tablename__ = "requests"
    id: UUID = id_col()
    from_user: UUID = Field(default=None)
