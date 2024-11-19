from abc import abstractmethod, ABC
from typing import List
from uuid import UUID

from invite_me.model import User


class IUsersRepository(ABC):
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
