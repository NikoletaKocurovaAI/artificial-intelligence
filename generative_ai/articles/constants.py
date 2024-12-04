from enum import Enum


FALLBACK_CONTENT_TYPE: str = "model_fallback"
AI_MODEL_CONTENT_TYPE: str = "model_personalized"

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

MAX_USER_PROMPT_LENGTH: int = 50


class Language(Enum):
    SLOVAK = "slovak"
    ENGLISH = "english"
