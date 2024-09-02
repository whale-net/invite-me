# from typing import List, Dict
# from uuid import UUID
#
# from invite_me.dispatch.dispatcher import IDispatcher
# from invite_me.dispatch.domain.request import Request
# from invite_me.dispatch.domain.response import Response
#
#
# class InviteService:
#     _dispatchers: Dict[UUID, IDispatcher]
#     _request_repository: IRequestRepository
#
#     def __init__(self, dispatchers: List[IDispatcher]):
#         self._dispatchers = {
#             dispatcher.dispatcher_id: dispatcher for dispatcher in dispatchers
#         }
#
#     def make_request(self, request: Request):
#         """
#         Makes a request, for each user the request to going to, send using their preferred dispatcher
#         """
#         for user in request.to_users:
#             # todo: async dispatch with thread pool
#             self._dispatchers[user.preferred_dispatcher].make_request(request, user)
#
#     def handle_response(self, response: Response):
#         self._dispatchers[response.from_user.preferred_dispatcher].handle_response(
#             response
#         )
