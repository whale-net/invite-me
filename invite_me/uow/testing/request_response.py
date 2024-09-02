from invite_me.repositories.testing.requests import TestingRequestsRepository
from invite_me.repositories.testing.responses import TestingResponsesRepository
from invite_me.uow.interfaces.request_response import IRequestResponseUnitOfWork


class TestingRequestResponseUnitOfWork(IRequestResponseUnitOfWork):
    requests_repo: TestingRequestsRepository
    responses_repo: TestingResponsesRepository

    def __init__(self, requests_repo: TestingRequestsRepository, responses_repo: TestingResponsesRepository):
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
