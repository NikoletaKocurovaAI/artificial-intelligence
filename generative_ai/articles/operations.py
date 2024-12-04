from typing import Any

import articles.constants as cons
from articles.models import ArticleRequest, ArticleResponse
from content_gen.views import get_completion
from weather.views import get_current_forecast


def generate_article(data: ArticleRequest) -> ArticleResponse:
    weather_forecast: dict[str, Any] = get_current_forecast(data.location)

    if not weather_forecast:
        return _get_fallback(data.location, data.language)

    generated_article: dict[str, Any] = get_completion({
        "system_prompt": _prepare_system_prompt(data.content_style, data.language),
        "user_prompt": _prepare_user_prompt(weather_forecast)
    })

    if not generated_article:
        return _get_fallback(data.location, data.language)

    return ArticleResponse(**generated_article)


def _get_fallback(location: str, language: str) -> ArticleResponse:
    if language == cons.Language.ENGLISH.value:
        return ArticleResponse(
            title=cons.FALLBACK_TITLE_EN.format(location=location),
            intro=cons.FALLBACK_INTRO_EN,
            body=cons.FALLBACK_BODY_EN,
            content_type=cons.FALLBACK_CONTENT_TYPE,
        )
    else:
        return ArticleResponse(
            title=cons.FALLBACK_TITLE_SK.format(location=location),
            intro=cons.FALLBACK_INTRO_SK,
            body=cons.FALLBACK_BODY_SK,
            content_type=cons.FALLBACK_CONTENT_TYPE,
        )


def _prepare_system_prompt(content_style: str, language: str) -> dict[str, Any]:
    return {
        "role": "system",
        "content": f"You are a writer creating {content_style} article in {language} language about the weather.",
    }


def _prepare_user_prompt(weather_forecast: dict[str, Any]) -> dict[str, Any]:
    return {
        "role": "user",
        "content": f"Write an article and send result in the json format with attributes title, intro and body. Use "
        f"this weather data: {weather_forecast}",
    }
