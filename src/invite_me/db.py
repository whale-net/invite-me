import os

import sqlalchemy.orm
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine(os.getenv("DB_CONN_STRING"), echo=True, echo_pool="debug")
sm = sessionmaker(bind=engine)


class Session:
    _session: sqlalchemy.orm.Session
    _autocommit: bool

    def __init__(self, autocommit=False):
        self._autocommit = autocommit

    def __enter__(self):
        self._session = sm()
        return self._session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._session.commit()
