# __all__ = ["InviteService"]
#
# from invite_me.service import InviteService
import uuid_extensions
from sqlmodel import SQLModel

from alembic.config import Config
from alembic import command


def run_migrations():
    # Load Alembic configuration
    alembic_cfg = Config("/app/alembic.ini")  # Path to your alembic.ini file

    # Run upgrade to head
    command.upgrade(alembic_cfg, "head")

def hello() -> str:
    return uuid_extensions.uuid7()
