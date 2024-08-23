from typing import List

from invite_me.dispatch.dispatcher import IDispatcher
from invite_me.dispatch.domain.message import Message
from invite_me.dispatch.domain.user import User


class InviteService:
    def __init__(self, dispatchers: List[IDispatcher]):
        self._dispatchers = dispatchers

    def dispatch_message(self, users: List[User], message: Message):
        for dispatcher in self._dispatchers:
            dispatcher.send_message(user_ids=[u.id for u in users], message=message)
