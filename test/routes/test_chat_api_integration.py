from unittest.mock import MagicMock

from models import Chat, Message, User
from routes.authentication import get_current_user
from routes.chat_api import start_chat
from services.chat_service import ChatService
from services.user_service import UserService


def test_chat_api_integrates_auth():
    # Arrange
    user_svc_mock = MagicMock(spec=UserService)
    user_svc_mock.get.return_value = User(id=1, name="Sally")

    message = Message(role="user", content="Hello, world")

    chat_svc_mock = MagicMock(spec=ChatService)
    chat_svc_mock.new.return_value = Chat(id="123", messages=[message])

    # Act - TODO: Complete these steps
    user = get_current_user(...)
    result = start_chat(...)

    # Assert
    # TODO: Prove the integration succeeds by testing delegated call to UserService
    ...
