from invite_me.repositories.testing.requests import MockRequestsRepository
from invite_me.repositories.testing.responses import MockResponsesRepository
from invite_me.uow.interfaces.request_response import IRequestResponseUnitOfWork


class MockRequestResponseUnitOfWork(IRequestResponseUnitOfWork):
    requests_repo: MockRequestsRepository
    responses_repo: MockResponsesRepository

    def __init__(self, requests_repo: MockRequestsRepository, responses_repo: MockResponsesRepository):
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
