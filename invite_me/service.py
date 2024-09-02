from invite_me.model import Request
from invite_me.uow.interfaces.request_response import IRequestResponseUnitOfWork


class InvitationService:
    _request_response_uow: IRequestResponseUnitOfWork

    def __init__(self, request_response_uow: IRequestResponseUnitOfWork):
        self._request_response_uow = request_response_uow

    def create_request(self, request: Request):
        try:

            with self._request_response_uow as uow:
                uow.requests_repo.create_request(request=request)
                uow.commit()
        except Exception as e:
            # todo: service should define its own errors
            raise
