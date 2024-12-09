from enum import Enum
from typing import Any


class Language(str, Enum):
    SLOVAK = "slovak"
    ENGLISH = "english"


class PromptRoles(Enum):
    SYSTEM = "system"
    USER = "user"


class ContentStyle(str, Enum):
    TABLOID = "tabloid"
    FACTUAL = "factual"


class ContentType:
    FALLBACK: str = "model_fallback"
    AI_MODEL: str = "model_personalized"


MAX_USER_PROMPT_LENGTH: int = 50

FALLBACK_TITLE_EN: str = "Weather Update for {location}"
FALLBACK_INTRO_EN: str = "Weather can be unpredictable, so stay prepared and keep an eye on the skies."
FALLBACK_BODY_EN: str = "Long before weather forecasts became a regular part of our lives, people relied on a variety " \
                        "of methods to predict the weather. Ancient civilizations looked to the skies, observing the " \
                        "movements of clouds and the behavior of animals to get a glimpse of what the day might bring."

FALLBACK_TITLE_SK: str = "Aktualizácia počasia pre {location}"
FALLBACK_INTRO_SK: str = "Počasie môže byť nepredvídateľné, preto buďte pripravení a sledujte oblohu."
FALLBACK_BODY_SK: str = "Dlho predtým, ako sa predpovede počasia stali bežnou súčasťou našich životov, ľudia sa " \
                        "spoliehali na rôzne metódy na predpovedanie počasia. Staroveké civilizácie sa pozerali na " \
                        "oblohu, sledovali pohyby oblakov a správanie zvierat, aby získali náhľad na to, čo deň " \
                        "prinesie."

FALLBACK_CONTENT: dict[str, Any] = {
    Language.ENGLISH.value: {
        "title": FALLBACK_TITLE_EN,
        "intro": FALLBACK_INTRO_EN,
        "body": FALLBACK_BODY_EN
    },
    Language.SLOVAK.value: {
        "title": FALLBACK_TITLE_SK,
        "intro": FALLBACK_INTRO_SK,
        "body": FALLBACK_BODY_SK
    }
}

SYSTEM_PROMPT_CONTENT: str = "You are a writer creating {content_style} article in {language} language about the " \
                             "weather."
USER_PROMPT_CONTENT: str = "Write an article and send result in the json format with attributes title, intro and " \
                             "body. Use this weather data: {weather_forecast}"
