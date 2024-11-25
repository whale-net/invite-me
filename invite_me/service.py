from typing import List

from invite_me.inviters import ExternalInviter
from invite_me.model import Request, User
from invite_me.model.uow.request_response import RequestResponseUnitOfWork
from invite_me.model.uow.user import UserUnitOfWork


class InvitationService:
    _request_response_uow: RequestResponseUnitOfWork
    _user_uow: UserUnitOfWork

    def __init__(
            self,
            inviter: ExternalInviter,
            request_response_uow: RequestResponseUnitOfWork,
            user_uow: UserUnitOfWork,
    ):
        # todo: this should be a list of inviters
        self._inviter = inviter

        # todo: we should also pull in an inviter user repo
        # answer the question how do we determine which inviter to use? necessary for multi-inviter

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
                print("BEFORESAVE")
                print(request.id)
                uow.requests_repo.create_request(request=request)
                uow.commit()
                print("AFTERSAVE")
                print(request.id)
        except Exception:
            # todo: service should define its own errors (at some point)
            raise
