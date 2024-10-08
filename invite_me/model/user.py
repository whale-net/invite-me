from uuid import UUID

from sqlmodel import SQLModel, Field

from invite_me.model._shared import id_col


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: UUID = id_col()
    name: str = Field(nullable=False)
