import os
import logging

from openai import OpenAI
from typing import Any

import content_gen.constants as cons
from content_gen.models import ContentGenRequest
from openai import RateLimitError, APIConnectionError


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))


class ContentGenApi:
    """
    Facade class responsible for getting current weather forecasts and historical weather data.
    """

    def get_completion(self, data: ContentGenRequest) -> dict[str, Any]:
        try:
            return self._request_completion(data)
        except (RateLimitError, APIConnectionError) as e:
            logging.error(f"API key error. Message: {e}")
        return {}

    @staticmethod
    def _request_completion(data: ContentGenRequest) -> dict[str, Any]:
        completion = client.chat.completions.create(
            model=cons.MODEL,
            messages=[data.system_prompt, data.user_prompt],
            max_tokens=cons.MAX_RESPONSE_TOKENS,
            temperature=cons.TEMPERATURE
        )
        return completion.choices[0].message


content_gen_api = ContentGenApi()