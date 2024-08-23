"""
Testing implementation of the dispatch classes to provide to tests for the dispatch service
"""
from typing import List
from uuid import UUID

from invite_me.dispatch.dispatcher import IDispatcher
from invite_me.dispatch.domain.message import Message


class TestingDispatcher(IDispatcher):
    def __init__(self, testing_message_bank: List[Message]):
        self._bank = testing_message_bank

    def send_message(self, user_ids: List[UUID], message: Message):
        self._bank.append(message)
