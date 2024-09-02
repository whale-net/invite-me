from sqlalchemy import Column, String

from invite_me import Base
from invite_me.model._shared import id_col


class User(Base):
    __tablename__ = "users"
    id = id_col()
    name = Column(String, nullable=False)
