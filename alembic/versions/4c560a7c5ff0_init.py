"""init

Revision ID: 4c560a7c5ff0
Revises:
Create Date: 2024-11-24 17:18:55.246390

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlmodel import SQLModel


from invite_me.inviters import SlackExternalInviter

# revision identifiers, used by Alembic.
revision: str = "4c560a7c5ff0"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    from invite_me.model import Request, Response, User, Inviter, InviterUser  # noqa

    connection = op.get_bind()
    SQLModel.metadata.create_all(connection)
    connection.commit()

    # ensure we have the base slack inviter
    inviter = Inviter(inviter_class=SlackExternalInviter.__name__)
    session = sa.orm.sessionmaker(bind=connection)()
    session.add(inviter)
    session.commit()


def downgrade() -> None:
    pass
