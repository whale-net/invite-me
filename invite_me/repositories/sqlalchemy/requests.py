from sqlalchemy.orm import Session

from invite_me.model import Request
from invite_me.repositories.interfaces.requests import IRequestsRepository


class SqlAlchemyRequestsRepository(IRequestsRepository):
    def __init__(self, session: Session):
        self._session = session

    def create_request(self, request: Request):
        self._session.add(request)
