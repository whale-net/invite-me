from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from invite_me.db import Base
from invite_me.model._shared import id_col


class RequestUsers(Base):
    __tablename__ = "request_users"
    id = id_col()
    request: Mapped["Request"] = relationship()


class Request(Base):
    __tablename__ = "requests"
    id = id_col()
    from_user = mapped_column(ForeignKey("users.id"))
