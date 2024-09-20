from invite_me.model import Request
from invite_me.uow.interfaces.request_response import IRequestResponseUnitOfWork


class InvitationService:
    _request_response_uow: IRequestResponseUnitOfWork

    def __init__(self, request_response_uow: IRequestResponseUnitOfWork):
        # todo: i want to be provided a dictionary of dispatchers
        # a user could have a preferred dispatcher, so we will need some user data in the database
        # could it be a user_dispatchers table with a priority rank assigned?
        self._request_response_uow = request_response_uow

    def create_request(self, request: Request):
        try:
            with self._request_response_uow as uow:
                uow.requests_repo.create_request(request=request)
                uow.commit()
        except Exception as e:
            # todo: service should define its own errors
            raise
