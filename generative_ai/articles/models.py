# from stereotype import Model, StrField
from pydantic import BaseModel, Field
from typing import Literal


class ArticleRequest(BaseModel):
    ALLOWED_LANGUAGES: list[str] = ["en", "sk"]

    language: Literal["en", "sk"] = Field(..., description="Allowed languages are en and sk.")
    # style: str = StrField()

# class ArticleResponse(Model):
#     body: str = StrField()