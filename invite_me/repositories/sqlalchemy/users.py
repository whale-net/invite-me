from typing import List
from uuid import UUID

from invite_me.model import User
from sqlalchemy.orm import Session, load_only
from sqlalchemy import select
from invite_me.repositories.interfaces.users import IUsersRepository


class SqlAlchemyUsersRepository(IUsersRepository):
    def __init__(self, session: Session):
        self._session = session

    def create_user(self, user: User):
        self._session.add(user)

    def get_user(self, id: UUID):
        pass

    def get_users(self) -> List[User]:
        return self._session.query(User).all()

    def get_user_names(self) -> List[str]:
        stmt = select(User).options(load_only(User.name))
        users = self._session.scalars(stmt).all()

        return [u.name for u in users]
