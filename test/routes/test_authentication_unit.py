import pytest
from fastapi import HTTPException

from routes.authentication import get_current_user


def test_get_current_user_unit_success():
    # Arrange
    ...

    # Act
    result = get_current_user(...)

    # Assert
    ...


def test_get_current_user_unit_failure():
    # Arrange
    ...

    # Act & "Assert" Raised Error
    with pytest.raises(HTTPException):
        ...  # TODO
