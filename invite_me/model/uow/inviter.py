from abc import ABC, abstractmethod

from invite_me.db import EngineWrapper
from invite_me.model.repositories.inviters import (
    InvitersRepository,
    SqlAlchemyInvitersRepository,
    MockInvitersRepository,
)


class InviterResponseUnitOfWork(ABC):
    inviters_repo: InvitersRepository

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


class SqlAlchemyInviterResponseUnitOfWork(InviterResponseUnitOfWork):
    inviters_repo: SqlAlchemyInvitersRepository

    def __init__(self, engine: EngineWrapper):
        self._engine = engine

    def __enter__(self):
        self._session = self._engine.get_session()
        self.inviters_repo = SqlAlchemyInvitersRepository(session=self._session)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()


class MockInviterResponseUnitOfWork(InviterResponseUnitOfWork):
    inviters_repo: MockInvitersRepository

    def __init__(
        self,
        inviters_repo: MockInvitersRepository,
    ):
        self.inviters_repo = inviters_repo

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass
