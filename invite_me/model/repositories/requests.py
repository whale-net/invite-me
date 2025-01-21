from abc import abstractmethod
from typing import Dict, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from invite_me.model import Request


class RequestsRepository:
    @abstractmethod
    def create_request(self, request: Request):
        """
        Creates a request

        :param request:
        :return:
        """
        raise NotImplementedError


class SqlAlchemyRequestsRepository(RequestsRepository):
    def __init__(self, session: Session):
        self._session = session

    def create_request(self, request: Request):
        self._session.add(request)


class MockRequestsRepository(RequestsRepository):
    _store: Dict[UUID, Request]

    def __init__(self, store: Optional[Dict[UUID, Request]] = None):
        if store is not None:
            self._store = store
        else:
            self._store = {}

    def create_request(self, request: Request):
        if self._store.get(request.id) is not None:
            raise ValueError("Some sort of implementation specific error")
        self._store[request.id] = request
