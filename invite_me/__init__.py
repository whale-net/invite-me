# __all__ = ["InviteService"]
#
# from invite_me.service import InviteService
from dotenv import load_dotenv

load_dotenv()

from invite_me.db import Base, engine


def seed_db():
    # import all table clases
    from .model import Request, Response, User  # noqa

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def hello() -> str:
    return "Hello from invite-me!"
