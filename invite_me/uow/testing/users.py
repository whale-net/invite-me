from invite_me.repositories.testing.users import MockUsersRepository
from invite_me.uow.interfaces.users import IUserUnitOfWork


class MockUserUnitOfWork(IUserUnitOfWork):
    users_repo: MockUsersRepository

    def __init__(self, users_repo: MockUsersRepository):
        self.user_repo = users_repo
