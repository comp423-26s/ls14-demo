from typing import Iterator
from unittest.mock import MagicMock

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from main import app
from models import Chat, Message, User
from services.chat_service import ChatService
from services.user_service import UserService


@pytest.fixture
def integrate_auth_helper() -> Iterator[tuple[TestClient, MagicMock]]:
    # This fixture sets up mock services for testing authenticated API routes.
    # It creates a mock UserService that returns a test user, and a mock ChatService
    # that returns a test chat. These mocks are injected into FastAPI's dependency
    # system so that when route handlers request UserService or ChatService,
    # they get our mock versions instead of the real ones. This allows us to test
    # the route logic without testing real implementations of the services.
    mock_user_svc = MagicMock(spec=UserService)
    mock_user_svc.get.return_value = User(id=1, name="Sally")
    app.dependency_overrides[UserService] = lambda: mock_user_svc

    mock_chat_svc = MagicMock(spec=ChatService)
    mock_chat_svc.new.return_value = Chat(
        id="123", messages=[Message(role="user", content="Hello, world")]
    )
    app.dependency_overrides[ChatService] = lambda: mock_chat_svc
    # Override FastAPI's Dependency Injection for ChatService

    with TestClient(app) as client:
        yield (client, mock_user_svc)
    app.dependency_overrides.clear()


def test_start_chat_current_user_integration(
    integrate_auth_helper: tuple[TestClient, MagicMock],
):
    # Arrange
    client, mock_user_svc = integrate_auth_helper

    # Act
    response = client.post(
        "/chat",
        headers={"Authorization": "password"},
        json=Message(role="user", content="Hello, world").model_dump(),
    )

    # Assert
    assert response.status_code == status.HTTP_200_OK
    mock_user_svc.get.assert_called_once_with(1)


def test_start_chat_bad_auth(integrate_auth_helper: tuple[TestClient, MagicMock]):
    # Arrange
    client, mock_user_svc = integrate_auth_helper

    # Act - TODO
    response = client.post(
        "/chat",
        headers={"Authorization": "bad-password"},
        json=Message(role="user", content="Hello, world").model_dump(),
    )

    # Assert
    assert response.status_code == status.HTTP_403_FORBIDDEN
    mock_user_svc.get.assert_not_called()
