from typing import Any


RESPONSE_SUCCESS: dict[str, Any] = {
    "location": {
        "name": "New York",
        "region": "New York",
        "country": "United States of America",
        "lat": 40.7142,
        "lon": -74.0064,
        "tz_id": "America/New_York",
        "localtime_epoch": 1733072650,
        "localtime": "2024-12-01 12:04",
    },
    "current": {
        "last_updated_epoch": 1733072400,
        "last_updated": "2024-12-01 12:00",
        "temp_c": 0.2,
        "temp_f": 32.4,
        "is_day": 1,
        "condition": {
            "text": "Sunny",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
            "code": 1000,
        },
        "wind_mph": 15.0,
        "wind_kph": 24.1,
        "wind_degree": 259,
        "wind_dir": "W",
        "pressure_mb": 1019.0,
        "pressure_in": 30.1,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 43,
        "cloud": 0,
        "feelslike_c": -5.5,
        "feelslike_f": 22.0,
        "windchill_c": -4.0,
        "windchill_f": 24.9,
        "heatindex_c": 0.7,
        "heatindex_f": 33.3,
        "dewpoint_c": -6.3,
        "dewpoint_f": 20.8,
        "vis_km": 16.0,
        "vis_miles": 9.0,
        "uv": 1.2,
        "gust_mph": 17.9,
        "gust_kph": 28.8,
    },
}

RESPONSE_NO_MATCHING_LOCATION: dict[str, Any] = {'error': {'code': 1006, 'message': 'No matching location found.'}}

RESPONSE_API_KEY_DISABLED: dict[str, Any] = {
    "error": {
        "code": 2008,
        "message": "API key has been disabled."
    }
}