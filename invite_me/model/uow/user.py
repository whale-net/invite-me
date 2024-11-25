from invite_me.db import engine
from invite_me.model.repositories.users import UsersRepository, SqlAlchemyUsersRepository, MockUsersRepository


class UserUnitOfWork:
    users_repository = UsersRepository

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass


class SqlAlchemyUserUnitOfWork(UserUnitOfWork):
    def __enter__(self):
        self._session = engine.get_session()
        self.users_repository = SqlAlchemyUsersRepository(session=self._session)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()


class MockUserUnitOfWork(UserUnitOfWork):
    users_repo: MockUsersRepository

    def __init__(self, users_repo: MockUsersRepository):
        self.user_repo = users_repo
