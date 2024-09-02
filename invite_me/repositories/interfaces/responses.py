from abc import ABC, abstractmethod

from invite_me.model import Response


class IResponsesRepository(ABC):
    @abstractmethod
    def create_response(self, response: Response):
        raise NotImplementedError
