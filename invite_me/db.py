import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine(os.getenv("DB_CONN_STRING"), echo=True, echo_pool="debug")
sm = sessionmaker(bind=engine)
