# __all__ = ["InviteService"]
#
# from invite_me.service import InviteService
from dotenv import load_dotenv
from sqlmodel import SQLModel

load_dotenv()

from invite_me.db import Base, engine


def seed_db():
    # import all table clases
    from .model import Request, Response, User  # noqa

    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


def hello() -> str:
    return "Hello from invite-me!"
