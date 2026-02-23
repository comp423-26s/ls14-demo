from typing import Literal

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class Message(BaseModel):
    role: Literal["user"] | Literal["assistant"]
    content: str


class Chat(BaseModel):
    id: str
    messages: list[Message]
