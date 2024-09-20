# __all__ = ["InviteService"]
#
# from invite_me.service import InviteService
from sqlmodel import SQLModel


def seed_db():
    """
    Right now this runs on every restart of the application, which is frequent when we use hot reloading
    todo: move to alembic for db migrations
    """
    from invite_me.db import engine
    # import all table clases
    from .model import Request, Response, User  # noqa

    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


def hello() -> str:
    return "Hello from invite-me!"
