from typing import Annotated, TypeAlias

from fastapi import Depends

from models import User


class UserService:
    def get(self, id: int) -> User:
        raise NotImplementedError()


UserServiceDI: TypeAlias = Annotated[UserService, Depends()]
