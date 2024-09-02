import pytest
import uuid_extensions

from invite_me.model import Request
from invite_me.repositories.testing.requests import TestingRequestsRepository
from invite_me.repositories.testing.responses import TestingResponsesRepository
from invite_me.service import InvitationService
from invite_me.uow.testing.request_response import TestingRequestResponseUnitOfWork


@pytest.fixture(scope="function")
def requests_repo():
    yield TestingRequestsRepository()


@pytest.fixture(scope="function")
def responses_repo():
    yield TestingResponsesRepository()


@pytest.fixture(scope="function")
def service(requests_repo, responses_repo):
    yield InvitationService(request_response_uow=TestingRequestResponseUnitOfWork(requests_repo=requests_repo,
                                                                                  responses_repo=responses_repo))


class TestInvitationService:
    def test_create_response(self, service, requests_repo):
        service.create_request(Request(from_user=uuid_extensions.uuid7()))

        # todo more meaningful tests, this is just a starting point
        assert len(requests_repo._store) == 1
