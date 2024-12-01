from typing import Any

import articles.constants as cons
from articles.models import ArticleRequest, ArticleResponse
from weather.views import get_current_forecast


def generate_article(data: ArticleRequest) -> ArticleResponse:
    weather_forecast: dict[str, Any] = get_current_forecast(data.location)

    if not weather_forecast:
        return get_fallback(data.location, data.language)

    generated_article: dict[str, Any] = {}

    return {}


def get_fallback(location: str, language: str) -> ArticleResponse:
    if language == "en":
        return ArticleResponse(
            title=f"Weather Update for {location}",
            intro="Weather can be unpredictable, so stay prepared and keep an eye on the skies.",
            body="Long before weather forecasts became a regular part of our lives, people relied on a variety of "
                 "methods to predict the weather. Ancient civilizations looked to the skies, observing the movements "
                 "of clouds and the behavior of animals to get a glimpse of what the day might bring.",
            content_type=cons.FALLBACK_CONTENT_TYPE,
        )
    else:
        return ArticleResponse(
            title=f"Aktualizácia počasia pre {location}",
            intro="Počasie môže byť nepredvídateľné, preto buďte pripravení a sledujte oblohu.",
            body="Dlho predtým, ako sa predpovede počasia stali bežnou súčasťou našich životov, ľudia sa spoliehali "
                 "na rôzne metódy na predpovedanie počasia. Staroveké civilizácie sa pozerali na oblohu, sledovali "
                 "pohyby oblakov a správanie zvierat, aby získali náhľad na to, čo deň prinesie.",
            content_type=cons.FALLBACK_CONTENT_TYPE,
        )
