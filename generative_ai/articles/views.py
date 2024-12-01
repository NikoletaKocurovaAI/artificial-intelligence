from typing import Any

from fastapi import APIRouter  # type: ignore
from pydantic import ValidationError

from articles.exceptions import InvalidArticleRequestException
from articles.models import ArticleRequest

router = APIRouter(prefix="/articles")


@router.get("/hello")
def hello_world() -> dict[str, str]:
    return {"message": "Hello, World!"}

@router.post("/api/articles/get-article")
def get_article(payload: dict[str, Any]) -> dict[str, Any]:
    print(f"received payload: {payload}")
    try:
        request = ArticleRequest(**payload)
    except (TypeError, ValidationError) as e:
        raise InvalidArticleRequestException(f"Message: {e}")

    return {"article": "Some article", "type": "fallback"}