from typing import Any

from pydantic import BaseModel, Field


class ContentGenRequest(BaseModel):
    system_prompt: dict[str, Any] = Field(
        ...,
        description="The system prompt used to define the assistant's behavior."
    )
    user_prompt: dict[str, Any] = Field(
        ...,
        description="The user prompt for the content generation."
    )

class ContentGenResponse(BaseModel):
    intro: str
    title: str
    body: str
