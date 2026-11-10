from fastapi import FastAPI, HTTPException

from weather_project.services.weather_service import get_weather_data


# Initialize FastAPI
app = FastAPI(
    title="Weather Project API",
    description="Backend API for the Weather Dashboard Sandbox",
    version="1.0.0"
)


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Weather API is running"
    }


# Weather endpoint
@app.get("/api/weather")
def get_weather():
    try:
        return get_weather_data()

    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Weather data file not found"
        )

    except (KeyError, IndexError, TypeError, ValueError):
        raise HTTPException(
            status_code=500,
            detail="Invalid weather data format"
        )