from invite_me.repositories.interfaces.users import IUsersRepository


class IUserUnitOfWork:
    users_repository = IUsersRepository

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass
