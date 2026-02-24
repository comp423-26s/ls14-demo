from unittest.mock import MagicMock

from models import Chat, Message, User
from routes.chat_api import start_chat
from services.chat_service import ChatService


def test_start_chat_delegates_to_chat_svc_unit():
    # Arrange
    chat_svc_mock = MagicMock(spec=ChatService)
    user = User(id=1, name="Sally")
    message = Message(role="user", content="Hello, world")
    chat_svc_mock.new.return_value = Chat(id="abc", messages=[message])

    # Act
    result = start_chat(chat_svc_mock, user, message)

    # Assert
    chat_svc_mock.new.assert_called_once_with(user, message)
    assert message in result.messages
