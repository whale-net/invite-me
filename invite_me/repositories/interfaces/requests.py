from abc import abstractmethod

from invite_me.model import Request


class IRequestsRepository:
    @abstractmethod
    def create_request(self, request: Request):
        """
        Creates a request

        :param request:
        :return:
        """
        raise NotImplementedError
