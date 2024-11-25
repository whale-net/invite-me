import pytest
import uuid_extensions

from invite_me.inviters import MockInviter
from invite_me.model import Request
from invite_me.model.repositories.requests import MockRequestsRepository
from invite_me.model.repositories.responses import MockResponsesRepository
from invite_me.model.repositories.users import MockUsersRepository
from invite_me.model.uow.request_response import MockRequestResponseUnitOfWork
from invite_me.model.uow.user import MockUserUnitOfWork
from invite_me.service import InvitationService


@pytest.fixture(scope="function")
def requests_repo():
    yield MockRequestsRepository()


@pytest.fixture(scope="function")
def responses_repo():
    yield MockResponsesRepository()


@pytest.fixture(scope="function")
def service(requests_repo, responses_repo):
    yield InvitationService(
        request_response_uow=MockRequestResponseUnitOfWork(
            requests_repo=requests_repo, responses_repo=responses_repo
        ),
        user_uow=MockUserUnitOfWork(users_repo=MockUsersRepository()),
        inviter=MockInviter()
    )


class TestInvitationService:
    def test_create_response(self, service, requests_repo):
        service.create_request(Request(from_user=uuid_extensions.uuid7()))
        # todo more meaningful tests, this is just a starting point
        assert len(requests_repo._store) == 1
