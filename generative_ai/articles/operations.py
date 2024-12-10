import logging

from typing import Any

import articles.constants as cons
from articles.models import ArticleRequest, ArticleResponse
from content_gen.exceptions import ContentGenApiError
from content_gen.views import get_completion
from weather.views import get_current_forecast


def generate_article(data: ArticleRequest) -> ArticleResponse:
    weather_forecast: dict[str, Any] = get_current_forecast(data.location)

    if not weather_forecast:
        logging.info(f"Weather data unavailable for location {data.location}. Using fallback.")
        return _get_fallback(data.location, data.language)

    try:
        generated_article: dict[str, Any] = get_completion({
            "system_prompt": _prepare_system_prompt(data.content_style, data.language),
            "user_prompt": _prepare_user_prompt(weather_forecast)
        })

    except ContentGenApiError:
        logging.info(f"Content generation unavailable. Using fallback.")
        return _get_fallback(data.location, data.language)

    return ArticleResponse(**generated_article)


def _get_fallback(location: str, language: str) -> ArticleResponse:
    content: dict[str, Any] = cons.FALLBACK_CONTENT.get(language)

    if not content:
        logging.warning(f"Unsupported language {language}, article fallback defaulting to English")
        content: dict[str, Any] = cons.FALLBACK_CONTENT.get(cons.Language.ENGLISH.value)

    return ArticleResponse(
        title=content["title"].format(location=location),
        intro=content["intro"],
        body=content["body"],
        content_type=cons.ContentType.FALLBACK,
    )


def _prepare_system_prompt(content_style: str, language: str) -> dict[str, Any]:
    return {
        "role": cons.PromptRoles.SYSTEM.value,
        "content": cons.SYSTEM_PROMPT_CONTENT.format(content_style, language)
    }


def _prepare_user_prompt(weather_forecast: dict[str, Any]) -> dict[str, Any]:
    return {
        "role": cons.PromptRoles.USER.value,
        "content": cons.USER_PROMPT_CONTENT.format(weather_forecast)
    }
