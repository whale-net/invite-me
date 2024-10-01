from time import sleep

from fastapi import FastAPI

from invite_me import seed_db
from invite_me.model import Request
from invite_me.service import InvitationService
from invite_me.tasks import add
from invite_me.uow.sqlalchemy.request_response import SqlAlchemyRequestResponseUnitOfWork
from celery import Celery
# broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'
# capp = Celery("hello", broker="amqp://guest@localhost:5672")
app = FastAPI()

celery_app = Celery('tasks', broker='pyamqp://guest@rabbit//', backend='rpc://guest@rabbitmq',)


# todo: this is here to wait for the postgres container to spin up. should use a sqlalchemy event to retry
sleep(1)
seed_db()
invitation_service = InvitationService(request_response_uow=SqlAlchemyRequestResponseUnitOfWork())


@app.get("/")
def hello():
    """
    send task to worker
    """
    task = celery_app.send_task('add', (4, 3))  # Send task by name
    return task.get(timeout=1)


@app.post("/invite/request")
def create_request(request: Request):
    invitation_service.create_request(request=request)

# @capp.task
# def hello():
#     return 'hello world'
