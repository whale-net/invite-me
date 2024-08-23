from abc import ABC
from dataclasses import dataclass
from enum import Enum, auto


class MessageType_(Enum):
    Y_N_INVITE = auto()

@dataclass
class Message:
    contents: str
    message_type: MessageType_
