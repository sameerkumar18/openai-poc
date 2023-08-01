from enum import Enum
from typing import List, Literal

from pydantic import BaseModel, Field, ConfigDict


class ChatRole(Enum):
    system = "system"
    user = "user"
    assistant = "assistant"


class Message(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    role: str = Field(alias='from')  # Literal[ChatRole.system, ChatRole.user, ChatRole.assistant]
    content: str = Field(alias='value')


class Conversation(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    messages: List[Message] = Field(alias='conversations')
    llm_model: Literal['gpt-4', 'gpt-3.5-turbo']
