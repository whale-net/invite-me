from sqlalchemy.orm import Session

from invite_me.model import Response
from invite_me.repositories.interfaces.responses import IResponsesRepository


class SqlAlchemyResponsesRepository(IResponsesRepository):
    def __init__(self, session: Session):
        self._session = session

    def create_response(self, response: Response):
        self._session.add(response)
