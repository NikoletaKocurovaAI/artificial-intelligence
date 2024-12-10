import logging
import os
import requests

from requests import Response
from typing import Any

import weather.constants as cons
from weather.exceptions import MissingApiKeyException


class WeatherApi:
    """
    Class responsible for fetching the weather forecast.
    """
    def __init__(self) -> None:
        self._weather_api_key = os.getenv("WEATHER_API_KEY", None)

        if not self._weather_api_key:
            raise MissingApiKeyException("WeatherAPI key env variable not set")

    def get_current(self, location: str) -> dict[str, Any]:
        response: Response = requests.get(
            url=f"{cons.BASE_URL}/current.json",
            params={
                "key": self._weather_api_key,
                "q": location,
                "aqi": "no"
            },
            timeout=cons.REQUEST_TIMEOUT_SEC
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 400:
            logging.warning(f"Invalid input error. Message: {response.json()}")

        if response.status_code == 403:
            logging.error(f"API key error. Message: {response.json()}")

        return {}


weather_api = WeatherApi()