import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_connection_string():
    return os.getenv("DB_CONN_STRING")


engine = create_engine(
    get_connection_string(), echo=True, echo_pool="debug", pool_pre_ping=True
)
sm = sessionmaker(bind=engine)
