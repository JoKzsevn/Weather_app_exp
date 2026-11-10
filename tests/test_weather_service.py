import json

from weather_project.services import weather_service


def test_get_weather_data(tmp_path, monkeypatch):

    # Example weather data
    mock_data = {
        "response": [
            {
                "profile": {
                    "tz": "Europe/Amsterdam"
                },
                "periods": [
                    {
                        "dateTimeISO": "2026-11-08T17:04:00+01:00",
                        "tempC": 8.9,
                        "feelslikeC": 8.9,
                        "humidity": 82,
                        "windDir": "S",
                        "visibilityKM": 8,
                        "weather": "Cloudy",
                        "weatherPrimary": "Cloudy"
                    }
                ]
            }
        ]
    }

    # Create temporary JSON file
    test_file = tmp_path / "test_weather.json"

    test_file.write_text(
        json.dumps(mock_data),
        encoding="utf-8"
    )

    # Replace actual data file with temporary test file
    monkeypatch.setattr(
        weather_service,
        "DATA_FILE",
        test_file
    )

    # Run service
    result = weather_service.get_weather_data()

    # Assertions
    assert result["temperature"] == 8.9
    assert result["feels_like"] == 8.9
    assert result["humidity"] == 82
    assert result["wind_direction"] == "S"
    assert result["visibility"] == 8
    assert result["weather"] == "Cloudy"
    assert result["timezone"] == "Europe/Amsterdam"