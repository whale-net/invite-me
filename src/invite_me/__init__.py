# __all__ = ["InviteService"]
#
# from invite_me.service import InviteService
from dotenv import load_dotenv

load_dotenv()

from invite_me.db import Base, engine, Session


def seed_db():
    # import all table clases
    from .model import Request, Response, User

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        pass


def hello() -> str:
    return "Hello from invite-me!"
