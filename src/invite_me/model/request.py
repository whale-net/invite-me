from sqlalchemy import UUID, Column

from invite_me.db import Base
from invite_me.model._shared import id_col


class Request(Base):
    __tablename__ = "requests"
    id = id_col()
    from_user = Column(UUID, index=True, nullable=False)
