import os
from abc import ABC, abstractmethod
from typing import List

from dotenv import load_dotenv
from time import sleep

from fastapi import FastAPI

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from invite_me import seed_db, _celery
from invite_me.executors import CeleryExecutor
from invite_me.model import Request, User
from invite_me.service import InvitationService
from invite_me.uow.sqlalchemy.request_response import SqlAlchemyRequestResponseUnitOfWork

class Inviter(ABC):
    """
    This is the class that will be inherited for api integrations.
    """
    @abstractmethod
    def get_users(self) -> List[User]:
        """
        Returns all users formatted appropriately as invite_me.model.user.User.

        :return: List of users
        """

    @abstractmethod
    def send_message(self, user: User, message: str) -> None:
        """
        Sends a text message to the listed user.

        :param user: user to send to.
        :param message: string text to send.
        :return: None
        """

class SlackInviter(Inviter):
    def __init__(self, slack_token):
        self._client = WebClient(token=slack_token)

    def _get_slack_members(self):
        try:
            # Get the list of users in the workspace
            response = self._client.users_list()
            if response['ok']:
                return response['members']
            else:
                print("Error fetching users:", response['error'])
                return []
        except SlackApiError as e:
            print(f"Error fetching users: {e.response['error']}")
            return []

    def get_users(self) -> List[User]:

        # how should this resolve? do we want to have a relationship between api users and users? just a quick lookup
        # by implementation mapping their api user id to our internal user id?

        return [User(id=sm['id'], name=sm['real_name']) for sm in self._get_slack_members() if not sm['deleted']]

    def send_message(self, user: User, message: str) -> None:
        self._client.chat_postMessage(channel=user.id)
        pass


app = FastAPI()

slack_token = os.getenv("AppToken")

# todo: this is here to wait for the postgres container to spin up. should use a sqlalchemy event to retry
sleep(1)
seed_db()
invitation_service = InvitationService(request_response_uow=SqlAlchemyRequestResponseUnitOfWork())


def add(x, y):
    return x - y

load_dotenv()

# Function to get all members of the Slack workspace

    # call this with the user_id set to the channel id field, ez
    # client.chat_postMessage()


@app.get("/")
def hello():
    """
    send task to worker
    """
    res = CeleryExecutor(_celery.app).execute_static('invite_me.tmp', func='hello_world')
    print(slack_token)

    return get_slack_members()
    # return res


@app.post("/invite/request")
def create_request(request: Request):
    invitation_service.create_request(request=request)

# @capp.task
# def hello():
#     return 'hello world'