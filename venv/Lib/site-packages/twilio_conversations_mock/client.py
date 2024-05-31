from conversations.conversations import ConversationList
from conversations.users import UserList


class ConversationsClientV1Mock:
    @property
    def conversations(self):
        return ConversationList()

    @property
    def users(self):
        return UserList()


class ConversationsClientMock:
    @property
    def v1(self):
        return ConversationsClientV1Mock()


class ClientMock:
    def __init__(self, *args, **kwargs):
        pass

    @property
    def conversations(self):
        return ConversationsClientMock()
