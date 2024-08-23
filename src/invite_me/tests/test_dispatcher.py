import uuid

import pytest

from invite_me import InviteService
from invite_me.dispatch.domain.message import Message, MessageType_
from invite_me.dispatch.domain.user import User
from invite_me.tests.impl.dispatch.dispatcher import TestingDispatcher

def test_dispatcher():
    messages = []
    test_dispatcher = TestingDispatcher(testing_message_bank=messages)
    service = InviteService(dispatchers=[test_dispatcher])

    user = User(id=uuid.uuid4(), name="Test user")
    message = Message(contents="Colony has invited you to play overwatch!", message_type=MessageType_.Y_N_INVITE)
    service.dispatch_message([user], message)

    assert message in messages
