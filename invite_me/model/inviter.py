from uuid import UUID

import datetime as dt
from sqlmodel import SQLModel, Field

from invite_me.model._shared import id_col, created_updated_col


class Inviter(SQLModel, table=True):
    __tablename__ = "inviter"
    id: UUID = id_col()
    inviter_class: str = Field(nullable=False, unique=True, index=True)
    created_at: dt.datetime = created_updated_col()
    updated_at: dt.datetime = created_updated_col()
