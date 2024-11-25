from abc import ABC, abstractmethod

from invite_me.db import EngineWrapper
from invite_me.model.repositories.requests import (
    RequestsRepository,
    SqlAlchemyRequestsRepository,
    MockRequestsRepository,
)
from invite_me.model.repositories.responses import (
    ResponsesRepository,
    SqlAlchemyResponsesRepository,
    MockResponsesRepository,
)


class RequestResponseUnitOfWork(ABC):
    requests_repo: RequestsRepository
    responses_repo: ResponsesRepository

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass


class SqlAlchemyRequestResponseUnitOfWork(RequestResponseUnitOfWork):
    requests_repo: SqlAlchemyRequestsRepository
    responses_repo: SqlAlchemyResponsesRepository

    def __init__(self, engine: EngineWrapper):
        self._engine = engine

    def __enter__(self):
        self._session = self._engine.get_session()
        self.requests_repo = SqlAlchemyRequestsRepository(session=self._session)
        self.responses_repo = SqlAlchemyResponsesRepository(session=self._session)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()


class MockRequestResponseUnitOfWork(RequestResponseUnitOfWork):
    requests_repo: MockRequestsRepository
    responses_repo: MockResponsesRepository

    def __init__(
        self,
        requests_repo: MockRequestsRepository,
        responses_repo: MockResponsesRepository,
    ):
        self.requests_repo = requests_repo
        self.responses_repo = responses_repo

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass
