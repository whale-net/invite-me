from abc import ABC, abstractmethod
from typing import Dict, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from invite_me.model import Response


class ResponsesRepository(ABC):
    @abstractmethod
    def create_response(self, response: Response):
        raise NotImplementedError


class SqlAlchemyResponsesRepository(ResponsesRepository):
    def __init__(self, session: Session):
        self._session = session

    def create_response(self, response: Response):
        self._session.add(response)


class MockResponsesRepository(ResponsesRepository):
    _store: Dict[UUID, Response]

    def __init__(self, store: Optional[Dict[UUID, Response]] = None):
        if store is not None:
            self._store = store
        else:
            self._store = {}

    def create_response(self, response: Response):
        if self._store.get(response.id) is not None:
            raise ValueError("Some sort of implementation specific error")
        self._store[response.id] = response
