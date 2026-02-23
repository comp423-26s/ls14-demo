from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from models import User
from routes.authentication import get_current_user
from services.user_service import UserService


def test_get_current_user_unit_success():
    # Arrange
    authorization = ...  # TODO
    user = User(id=1, name="Sally")
    user_svc_mock = MagicMock(spec=UserService)
    user_svc_mock.get.return_value = user

    # Act
    result = get_current_user(...)

    # Assert
    ...  # TODO


def test_get_current_user_unit_failure():
    # Arrange
    ...

    # Act & "Assert" Raised Error
    with pytest.raises(HTTPException):
        ...  # TODO
