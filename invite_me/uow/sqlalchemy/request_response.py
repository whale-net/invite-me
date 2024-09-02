from invite_me.db import sm
from invite_me.repositories.sqlalchemy.requests import SqlAlchemyRequestsRepository
from invite_me.repositories.sqlalchemy.responses import SqlAlchemyResponsesRepository
from invite_me.uow.interfaces.request_response import IRequestResponseUnitOfWork


class SqlAlchemyRequestResponseUnitOfWork(IRequestResponseUnitOfWork):
    requests_repo: SqlAlchemyRequestsRepository
    responses_repo: SqlAlchemyResponsesRepository

    def __enter__(self):
        self._session = sm()
        self.requests_repo = SqlAlchemyRequestsRepository(session=self._session)
        self.responses_repo = SqlAlchemyResponsesRepository(session=self._session)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
