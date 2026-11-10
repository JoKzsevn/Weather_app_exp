import json
from pathlib import Path


# Project root
BASE_DIR = Path(__file__).resolve().parents[3]

# JSON file path
DATA_FILE = BASE_DIR / "data" / "Rotterdam_weather_data.json"


def get_weather_data():
    """
    Load weather data from JSON and return
    the selected fields.
    """

    # Read JSON
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Extract response
    response = data["response"][0]

    # Extract first weather observation
    period = response["periods"][0]

    # Select fields
    weather_data = {
        "date_time": period["dateTimeISO"],
        "temperature": period["tempC"],
        "feels_like": period["feelslikeC"],
        "humidity": period["humidity"],
        "wind_direction": period["windDir"],
        "visibility": period["visibilityKM"],
        "weather": period["weather"],
        "weather_primary": period["weatherPrimary"],
        "timezone": response.get("profile", {}).get(
            "tz", "Europe/Amsterdam"
        ),
    }

    return weather_data