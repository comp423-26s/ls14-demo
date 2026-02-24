from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from models import User
from routes.authentication import get_current_user
from services.user_service import UserService


def test_get_current_user_unit_success():
    # Arrange
    authorization = "password"
    user = User(id=1, name="Sally")
    user_svc_mock = MagicMock(spec=UserService)
    user_svc_mock.get.return_value = user

    # Act
    result = get_current_user(authorization, user_svc_mock)

    # Assert
    user_svc_mock.get.assert_called_once()
    assert result == user


def test_get_current_user_unit_failure():
    # Arrange
    authorization = "secret"
    user_svc_mock = MagicMock(spec=UserService)

    # Act & "Assert" Raised Error
    with pytest.raises(HTTPException):
        get_current_user(authorization, user_svc_mock)

    # Assert
    user_svc_mock.get.assert_not_called()
