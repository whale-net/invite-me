from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from invite_me.dispatch.domain.message import Message


class IDispatcher(ABC):
    @abstractmethod
    def send_message(self, user_ids: List[UUID], message: Message):
        pass

