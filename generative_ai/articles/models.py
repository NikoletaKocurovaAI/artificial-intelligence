from pydantic import BaseModel, Field
from typing import Literal


class ArticleRequest(BaseModel):
    language: Literal["english", "slovak"] = Field(..., description="Allowed languages are english and slovak.")
    content_style: Literal["factual", "tabloid"] = Field(..., description="Allowed styles are factual and tabloid.")
    location: str = Field(..., description="Country for which the weather forecast is requested.")

class ArticleResponse(BaseModel):
    title: str = Field(..., description="Article title")
    intro: str = Field(..., description="Article intro content")
    body: str = Field(..., description="Article body content")
    content_type: str = Field(..., description="Type of content: personalized or fallback")