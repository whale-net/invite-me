from abc import abstractmethod
from typing import Dict, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from invite_me.model import Inviter


class InvitersRepository:
    @abstractmethod
    def create_inviter(self, inviter: Inviter):
        """
        Creates an inviter

        :param inviter:
        :return:
        """
        raise NotImplementedError


class SqlAlchemyInvitersRepository(InvitersRepository):
    def __init__(self, session: Session):
        self._session = session

    def create_inviter(self, inviter: Inviter):
        self._session.add(inviter)


class MockInvitersRepository(InvitersRepository):
    _store: Dict[UUID, Inviter]

    def __init__(self, store: Optional[Dict[UUID, Inviter]] = None):
        if store is not None:
            self._store = store
        else:
            self._store = {}

    def create_inviter(self, inviter: Inviter):
        if self._store.get(inviter.id) is not None:
            raise ValueError("Some sort of implementation specific error")
        self._store[inviter.id] = inviter
