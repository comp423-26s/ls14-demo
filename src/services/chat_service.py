from typing import Annotated, TypeAlias

from fastapi import Depends

from models import Chat, Message, User


class ChatService:
    def new(self, user: User, message: Message) -> Chat:
        raise NotImplementedError()


ChatServiceDI: TypeAlias = Annotated[ChatService, Depends()]
