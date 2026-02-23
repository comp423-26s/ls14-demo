from typing import Annotated, TypeAlias

from fastapi import Depends, Header, HTTPException, status

from models import User
from services.user_service import UserServiceDI

HeaderDI: TypeAlias = Annotated[str, Header()]


def get_current_user(authorization: HeaderDI, user_svc: UserServiceDI) -> User:
    # Note: This is *obviously* a woefully silly implementation of user auth
    if authorization == "password":
        return user_svc.get(1)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


CurrentUserDI: TypeAlias = Annotated[User, Depends(get_current_user)]
