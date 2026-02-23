from typing import Annotated, TypeAlias

from fastapi import APIRouter, Body

from models import Chat, Message
from services.chat_service import ChatServiceDI

from .authentication import CurrentUserDI

router = APIRouter()

MessageDI: TypeAlias = Annotated[Message, Body]


@router.post("/chat")
def start_chat(
    chat_svc: ChatServiceDI, user: CurrentUserDI, message: MessageDI
) -> Chat:
    return chat_svc.new(user, message)
