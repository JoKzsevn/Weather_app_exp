import json
from pathlib import Path
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Rotterdam Weather Dashboard",
    page_icon="🌤️",
    layout="wide"
)

# Load JSON
file_path = Path("../data/Rotterdam_weather_data.json")

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract weather data
weather_data = data["response"][0]
period = weather_data["periods"][0]

# Extract values
date_time = period["dateTimeISO"]
temperature = period["tempC"]
feels_like = period["feelslikeC"]
humidity = period["humidity"]
wind_direction = period["windDir"]
visibility = period["visibilityKM"]
weather = period["weather"]
weather_primary = period["weatherPrimary"]
timezone = weather_data.get("profile", {}).get("tz", "Europe/Amsterdam")

# Dashboard
st.title("🌤️ Rotterdam Weather Dashboard")

st.write(f"📅 **Date and Time:** {date_time}")
st.write(f"🌍 **Timezone:** {timezone}")

st.divider()

# First row
col1, col2, col3 = st.columns(3)

col1.metric("🌡️ Temperature", f"{temperature} °C")
col2.metric("🌡️ Feels Like", f"{feels_like} °C")
col3.metric("💧 Humidity", f"{humidity}%")

# Second row
col4, col5 = st.columns(2)

col4.metric("🧭 Wind Direction", wind_direction)
col5.metric("👁️ Visibility", f"{visibility} km")

st.divider()

# Weather conditions
st.subheader("☁️ Weather Conditions")

st.write(f"**Weather:** {weather}")
st.write(f"**Weather Primary:** {weather_primary}")