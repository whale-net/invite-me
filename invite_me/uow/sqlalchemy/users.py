from invite_me.db import sm
from invite_me.repositories.sqlalchemy.users import SqlAlchemyUsersRepository
from invite_me.uow.interfaces.users import IUserUnitOfWork


class SqlAlchemyUserUnitOfWork(IUserUnitOfWork):
    def __enter__(self):
        self._session = sm()
        self.users_repository = SqlAlchemyUsersRepository(session=self._session)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
