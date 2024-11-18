import os
from dotenv import load_dotenv
from time import sleep

from fastapi import FastAPI

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from invite_me import seed_db, _celery
from invite_me.executors import CeleryExecutor
from invite_me.model import Request
from invite_me.service import InvitationService
from invite_me.uow.sqlalchemy.request_response import SqlAlchemyRequestResponseUnitOfWork

app = FastAPI()

# todo: this is here to wait for the postgres container to spin up. should use a sqlalchemy event to retry
sleep(1)
seed_db()
invitation_service = InvitationService(request_response_uow=SqlAlchemyRequestResponseUnitOfWork())


def add(x, y):
    return x - y

load_dotenv()
slack_token = os.getenv("AppToken")

client = WebClient(token=slack_token)

# Function to get all members of the Slack workspace
def get_slack_members():
    # todo: we should get users and insert into a database table. can validate existing on startup? we never add or remove anyone
    try:
        # Get the list of users in the workspace
        response = client.users_list()
        if response['ok']:
            return response['members']
        else:
            print("Error fetching users:", response['error'])
            return []
    except SlackApiError as e:
        print(f"Error fetching users: {e.response['error']}")
        return []

    # call this with the user_id set to the channel id field, ez
    # client.chat_postMessage()


@app.get("/")
def hello():
    """
    send task to worker
    """
    res = CeleryExecutor().execute_static('invite_me.tmp', func='hello_world')
    print(slack_token)

    return get_slack_members()
    # return res


@app.post("/invite/request")
def create_request(request: Request):
    invitation_service.create_request(request=request)

# @capp.task
# def hello():
#     return 'hello world'