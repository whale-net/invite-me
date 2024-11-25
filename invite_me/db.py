import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_connection_string():
    return os.getenv("DB_CONN_STRING")


class _EngineWrapper:
    _engine = None
    _sessionmaker = None

    def __init__(self):
        pass

    def get_engine(self):
        if self._engine is not None:
            return self._engine
        else:
            self._engine = create_engine(
                get_connection_string(), echo=True, echo_pool="debug", pool_pre_ping=True
            )
            return self._engine

    def get_sessionmaker(self):
        if self._sessionmaker is not None:
            return self._sessionmaker
        else:
            self._sessionmaker = sessionmaker(bind=self.get_engine())
            return self._sessionmaker

    def get_session(self):
        return self.get_sessionmaker()()


engine = _EngineWrapper()
