from typing import Dict, Optional
from uuid import UUID

from invite_me.model import Response
from invite_me.repositories.interfaces.responses import IResponsesRepository


class TestingResponsesRepository(IResponsesRepository):
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
