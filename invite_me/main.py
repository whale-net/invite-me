import os
from time import sleep

from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import select

from invite_me.db import engine
from invite_me.inviters import SlackExternalInviter
from invite_me.model import Request, Inviter
from invite_me.model.uow.request_response import SqlAlchemyRequestResponseUnitOfWork
from invite_me.model.uow.user import SqlAlchemyUserUnitOfWork
from invite_me.service import InvitationService

load_dotenv()

app = FastAPI()
slack_token = os.getenv("AppToken")

# todo: this is here to wait for the postgres container to spin up. should use a sqlalchemy event to retry
sleep(1)

session = engine.get_session()

#
stmt = select(Inviter).where(Inviter.inviter_class == SlackExternalInviter.__name__)
inviter = session.execute(stmt).first()[0]
session.close()

invitation_service = InvitationService(
    inviter=SlackExternalInviter(slack_token=slack_token, inviter_id=inviter.id),
    request_response_uow=SqlAlchemyRequestResponseUnitOfWork(),
    user_uow=SqlAlchemyUserUnitOfWork(),
)


# Function to get all members of the Slack workspace

# call this with the user_id set to the channel id field, ez
# client.chat_postMessage()


@app.get("/")
def hello():
    """
    send task to worker
    """

    # inviter = SlackInviter(slack_token=slack_token)
    # users = inviter.get_users()
    #
    # invitation_service.create_users(users)

    # inviter.send_message(user=users[0], message='test')
    return None


@app.post("/invite/request")
def create_request(request: Request):
    invitation_service.create_request(request=request)

# @capp.task
# def hello():
#     return 'hello world'
