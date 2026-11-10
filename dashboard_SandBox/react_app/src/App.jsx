import { useEffect, useState } from "react";
import "./App.css";


function App() {

  // React states
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);


  // Fetch data from FastAPI
  useEffect(() => {

    const fetchWeather = async () => {

      try {

        const response = await fetch("/api/weather");

        if (!response.ok) {
          throw new Error("Failed to fetch weather data");
        }

        const data = await response.json();

        setWeather(data);

      } catch (err) {

        setError(err.message);

      } finally {

        setLoading(false);

      }
    };

    fetchWeather();

  }, []);


  // Loading screen
  if (loading) {
    return <h2>Loading weather data...</h2>;
  }


  // Error screen
  if (error) {
    return <h2>Error: {error}</h2>;
  }


  if (!weather) {
    return <h2>No weather data available</h2>;
  }


  // Weather dashboard
  return (

    <div className="dashboard">

      <header className="dashboard-header">

        <h1>🌤️ Rotterdam Weather Dashboard</h1>

        <p>Date and Time: {weather.date_time}</p>

        <p>Timezone: {weather.timezone}</p>

      </header>


      <div className="weather-grid">

        <WeatherCard
          title="Temperature"
          value={`${weather.temperature} °C`}
          icon="🌡️"
        />

        <WeatherCard
          title="Feels Like"
          value={`${weather.feels_like} °C`}
          icon="🌡️"
        />

        <WeatherCard
          title="Humidity"
          value={`${weather.humidity}%`}
          icon="💧"
        />

        <WeatherCard
          title="Wind Direction"
          value={weather.wind_direction}
          icon="🧭"
        />

        <WeatherCard
          title="Visibility"
          value={`${weather.visibility} km`}
          icon="👁️"
        />

        <WeatherCard
          title="Weather"
          value={weather.weather}
          icon="☁️"
        />

      </div>


      {/* <section className="weather-details">

        <h2>Weather Details</h2>

        <p>
          <strong>Weather Primary:</strong>{" "}
          {weather.weather_primary}
        </p>

      </section> */}

    </div>
  );
}


// Reusable React component
function WeatherCard({ title, value, icon }) {

  return (

    <div className="weather-card">

      <h3>{icon} {title}</h3>

      <p>{value}</p>

    </div>

  );
}


export default App;