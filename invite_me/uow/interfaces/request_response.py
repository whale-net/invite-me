from abc import ABC, abstractmethod

from invite_me.repositories.interfaces.requests import IRequestsRepository
from invite_me.repositories.interfaces.responses import IResponsesRepository


class IRequestResponseUnitOfWork(ABC):
    requests_repo: IRequestsRepository
    responses_repo: IResponsesRepository

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
