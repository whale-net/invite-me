from typing import Dict, Optional
from uuid import UUID

from invite_me.model import Request
from invite_me.repositories.interfaces.requests import IRequestsRepository


class TestingRequestsRepository(IRequestsRepository):
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
