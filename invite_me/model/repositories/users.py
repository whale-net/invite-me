from abc import abstractmethod, ABC
from typing import List, Dict, Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session, load_only

from invite_me.model import User


class UsersRepository(ABC):
    @abstractmethod
    def create_user(self, user: User):
        """
        Creates a user

        :param user:
        :return:
        """
        raise NotImplementedError

    def create_users(self, users: List[User]):
        """
        Creates multiple users

        :param users:
        :return:
        """
        for user in users:
            self.create_user(user)

    @abstractmethod
    def get_user(self, id: UUID) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_users(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def get_user_names(self) -> List[str]:
        raise NotImplementedError


class SqlAlchemyUsersRepository(UsersRepository):
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


class MockUsersRepository(UsersRepository):
    _store: Dict[UUID, User]

    def __init__(self, store: Optional[Dict[UUID, User]] = None):
        if store is not None:
            self._store = store
        else:
            self._store = {}

    def create_user(self, user: User):
        if user.id not in self._store:
            self._store[user.id] = user

    def get_user(self, id: UUID) -> User:
        return self._store[id]

    def get_users(self) -> List[User]:
        return list(self._store.values())

    def get_user_names(self) -> List[str]:
        return [user.name for user in self._store.values()]
