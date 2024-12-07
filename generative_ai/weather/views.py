from typing import Any, Type

from fastapi import APIRouter  # type: ignore

from weather.operations import weather_api

router = APIRouter(prefix="/articles")


@router.post("/api/weather/get-current-forecast")
def get_current_forecast(location: str) -> dict[str, Any]:
    """
    This route returns current weather forecast.

    :param location:
    :type location: str
    :return:
    :rtype: dict
    """
    return weather_api.get_current(location)


@router.post("/api/weather/get-history-forecast")
def get_history_forecast(location: str) -> Type[NotImplementedError]:
    """
    This route returns history weather forecast.

    :param location:
    :type location: str
    :return:
    :rtype: dict
    """
    return NotImplementedError
