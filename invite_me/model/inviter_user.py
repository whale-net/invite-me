from uuid import UUID

import datetime as dt
from sqlmodel import SQLModel, Field

from invite_me.model._shared import id_col, created_updated_col


class InviterUser(SQLModel, table=True):
    __tablename__ = "inviter_user"
    id: UUID = id_col()
    inviter_id: UUID = Field(nullable=False, index=True)
    user_id: UUID = Field(foreign_key="users.id", index=True, nullable=True)
    user_id_from_inviter: str = Field(nullable=True)
    user_object_from_inviter: str = Field(nullable=True)
    created_at: dt.datetime = created_updated_col()
    updated_at: dt.datetime = created_updated_col()
