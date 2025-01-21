import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



import subprocess


def get_alembic_revision(command):
    result = subprocess.run(["alembic", command], capture_output=True, text=True)
    return result.stdout.strip()


def run_migrations():
    current_revision = get_alembic_revision("current")
    latest_revision = get_alembic_revision("heads")

    if current_revision != latest_revision:
        print("New migration detected. Upgrading...")
        subprocess.run(["alembic", "upgrade", "head"])
    else:
        print("Database is already up-to-date.")


def get_connection_string():
    return os.getenv("DB_CONN_STRING")


class EngineWrapper:
    _engine = None
    _sessionmaker = None

    def __init__(self):
        pass

    def get_engine(self):
        if self._engine is not None:
            return self._engine
        else:
            self._engine = create_engine(
                get_connection_string(),
                echo=True,
                echo_pool="debug",
                pool_pre_ping=True,
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


engine = EngineWrapper()
