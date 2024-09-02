from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from invite_me.db import Base
from invite_me.model import Request
from invite_me.model._shared import id_col


class Response(Base):
    __tablename__ = "responses"
    id = id_col()
    request_id: Mapped[Request] = mapped_column(ForeignKey("requests.id"))
