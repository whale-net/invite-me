from typing import List, Dict, Optional
from uuid import UUID

from invite_me.model import User
from invite_me.repositories.interfaces.users import IUsersRepository


class MockUsersRepository(IUsersRepository):
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
