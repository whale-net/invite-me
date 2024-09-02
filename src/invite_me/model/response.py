from invite_me.db import Base
from invite_me.model._shared import id_col


class Response(Base):
    __tablename__ = "responses"
    id = id_col()
