from fastapi.testclient import TestClient

from weather_project.api.main import app
from weather_project.api import main


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Weather API is running"
    }


def test_weather_endpoint(monkeypatch):

    # Mock weather response
    mock_weather = {
        "date_time": "2026-11-08T17:04:00+01:00",
        "temperature": 8.9,
        "feels_like": 8.9,
        "humidity": 82,
        "wind_direction": "S",
        "visibility": 8,
        "weather": "Cloudy",
        "weather_primary": "Cloudy",
        "timezone": "Europe/Amsterdam"
    }

    # Replace service call
    monkeypatch.setattr(
        main,
        "get_weather_data",
        lambda: mock_weather
    )

    response = client.get("/api/weather")

    assert response.status_code == 200

    data = response.json()

    assert data["temperature"] == 8.9
    assert data["humidity"] == 82
    assert data["weather"] == "Cloudy"


def test_weather_file_not_found(monkeypatch):

    def mock_weather():
        raise FileNotFoundError("Weather file missing")

    monkeypatch.setattr(
        main,
        "get_weather_data",
        mock_weather
    )

    response = client.get("/api/weather")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Weather data file not found"
    }


def test_invalid_weather_data(monkeypatch):

    def mock_weather():
        raise KeyError("tempC")

    monkeypatch.setattr(
        main,
        "get_weather_data",
        mock_weather
    )

    response = client.get("/api/weather")

    assert response.status_code == 500

    assert response.json() == {
        "detail": "Invalid weather data format"
    }