from typing import List

from invite_me.model import Request, User
from invite_me.uow.interfaces.request_response import IRequestResponseUnitOfWork
from invite_me.uow.interfaces.users import IUserUnitOfWork


class InvitationService:
    _request_response_uow: IRequestResponseUnitOfWork
    _user_uow: IUserUnitOfWork

    def __init__(
        self,
        request_response_uow: IRequestResponseUnitOfWork,
        user_uow: IUserUnitOfWork,
    ):
        self._request_response_uow = request_response_uow
        self._user_uow = user_uow

    def create_users(self, users: List[User], check_if_exists: bool = False):
        if check_if_exists:
            with self._user_uow as uow:
                user_names = set(uow.users_repository.get_user_names())
            users = [u for u in users if u.name not in user_names]

        with self._user_uow as uow:
            uow.users_repository.create_users(users)
            uow.commit()

    def create_request(self, request: Request):
        """
        Dispatches a new request
        :param request:
        :return:
        """
        try:
            with self._request_response_uow as uow:
                uow.requests_repo.create_request(request=request)
                uow.commit()
        except Exception:
            # todo: service should define its own errors (at some point)
            raise
