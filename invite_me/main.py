from time import sleep

from fastapi import FastAPI

from invite_me import seed_db, _celery
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


@app.get("/")
def hello():
    """
    send task to worker
    """
    task = _celery.app.send_task('execute_static', ['invite_me.tmp'])  # Send task by name
    return task.get(timeout=1)


@app.post("/invite/request")
def create_request(request: Request):
    invitation_service.create_request(request=request)

# @capp.task
# def hello():
#     return 'hello world'
