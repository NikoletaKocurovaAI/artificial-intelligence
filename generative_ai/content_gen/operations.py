import json
import os
import logging

from openai import OpenAI
from pydantic import ValidationError
from typing import Any

import content_gen.constants as cons
from content_gen.exceptions import InvalidContentGenResponseException, ContentGenApiError
from content_gen.models import ContentGenRequest, ContentGenResponse
from openai import RateLimitError, APIConnectionError


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))


class ContentGenApi:
    """
    Class responsible for retrieving the generated content from an external API.
    """

    def get_completion(self, data: ContentGenRequest) -> ContentGenResponse:
        try:
            response = self._request_completion(data)
            return self._validate_completion(response)

        except (RateLimitError, APIConnectionError) as e:
            logging.error(f"API key error. Message: {e}")
            raise ContentGenApiError(f"Message {e}")

        except InvalidContentGenResponseException as e:
            logging.error(f"Content gen returned invalid format. Message: {e}")
            raise ContentGenApiError(f"Message {e}")

    @staticmethod
    def _request_completion(data: ContentGenRequest) -> dict[str, Any]:
        completion = client.chat.completions.create(
            model=cons.MODEL,
            messages=[data.system_prompt, data.user_prompt],
            max_tokens=cons.MAX_RESPONSE_TOKENS,
            temperature=cons.TEMPERATURE
        )
        return completion.choices[0].message

    @staticmethod
    def _validate_completion(response) -> ContentGenResponse:
        try:
            if isinstance(response, str):
                response = json.loads(response)

            return ContentGenResponse(**response)

        except (json.JSONDecodeError, ValidationError) as e:
            raise InvalidContentGenResponseException(f"Message {e}")


content_gen_api = ContentGenApi()