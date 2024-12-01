from typing import Any

from fastapi import APIRouter  # type: ignore
from pydantic import ValidationError

from articles.exceptions import InvalidArticleRequestException
from articles.models import ArticleRequest, ArticleResponse
from articles import operations

router = APIRouter(prefix="/articles")


@router.get("/hello")
def hello_world() -> dict[str, str]:
    return {"message": "Hello, World!"}


@router.post("/api/articles/get-article")
def get_article(payload: dict[str, Any]) -> dict[str, Any]:
    """
    This route returns generated weather-related articles.

    :param payload:
    :type payload: dict
    :return:
    :rtype: dict
    """
    try:
        request = ArticleRequest(**payload)
        response: ArticleResponse = operations.generate_article(request)

    except (TypeError, ValidationError) as e:
        raise InvalidArticleRequestException(f"Message: {e}")

    return response.dict()
