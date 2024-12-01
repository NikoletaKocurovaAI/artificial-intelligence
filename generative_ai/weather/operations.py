import logging
import os
import requests

from requests import Response
from typing import Any

import weather.constants as cons


class WeatherApi:
    """
    Facade class responsible for the generation of text articles that interpret weather forecasts into a readable format.
    """
    def __init__(self, location: str) -> None:
        self.location: str = location
        self.weather_api_key = os.getenv("OPENAI_API_KEY", None)

    def get_current(self) -> dict[str, Any]:
        url: str = f"{cons.BASE_URL}/current.json?key={self.weather_api_key}&q={self.location}&aqi=no"
        response: Response = requests.post(url, params={"location": self.location}, timeout=cons.REQUEST_TIMEOUT_SEC)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 400:
            logging.warning(f"Invalid input error. Message: {response.json()}")

        if response.status_code == 403:
            logging.error(f"API key error. Message: {response.json()}")

        return {}

    @staticmethod
    def get_history() -> dict[str, Any]:
        return {}