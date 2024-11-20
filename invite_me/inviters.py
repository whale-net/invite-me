from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from invite_me.model import InviterUser


class ExternalInviter(ABC):
    """
    This is the class that will be inherited for api integrations.
    """

    @abstractmethod
    def get_users(self) -> List[InviterUser]:
        """
        Returns all users formatted appropriately as invite_me.model.user.User.

        :return: List of users
        """

    @abstractmethod
    def send_message(self, user: InviterUser, message: str) -> None:
        """
        Sends a text message to the listed user.

        :param user: user to send to.
        :param message: string text to send.
        :return: None
        """


class SlackExternalInviter(ExternalInviter):
    def __init__(self, slack_token, inviter_id: UUID):
        self._client = WebClient(token=slack_token)
        self._inviter_id = inviter_id

    def _get_slack_members(self):
        try:
            # Get the list of users in the workspace
            response = self._client.users_list()
            if response["ok"]:
                return response["members"]
            else:
                print("Error fetching users:", response["error"])
                return []
        except SlackApiError as e:
            print(f"Error fetching users: {e.response['error']}")
            return []

    def get_users(self) -> List[InviterUser]:
        return [
            InviterUser(
                inviter_id=self._inviter_id,
                user_id_from_inviter=sm["id"],
                user_object_from_inviter=sm,
                full_user_info=sm,
            )
            for sm in self._get_slack_members()
            if (not sm["deleted"])
            and sm.get("profile")
            and sm["profile"]["display_name"] == "koni"
        ]

    def send_message(self, user: InviterUser, message: str) -> None:
        self._client.chat_postMessage(channel=user.user_id_from_inviter, text=message)
