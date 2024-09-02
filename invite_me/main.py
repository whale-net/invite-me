from fastapi import FastAPI

from invite_me import seed_db
from invite_me.model import Request
from invite_me.service import InvitationService
from invite_me.uow.sqlalchemy.request_response import SqlAlchemyRequestResponseUnitOfWork

app = FastAPI()

seed_db()

invitation_service = InvitationService(request_response_uow=SqlAlchemyRequestResponseUnitOfWork())


@app.post("/invite/request")
def create_request(request: Request):
    invitation_service.create_request(request=request)
