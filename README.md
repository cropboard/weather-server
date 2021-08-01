# Cropboard weather service

This is a minimal weather microservice for cropboard.
It serves little data like below

```json
{
  "lat": 3.8667,
  "lon": 11.5167,
  "temp": "298.96 F",
  "pressure": "1017hPa",
  "humidity": "67%",
  "visibility": "10.0km",
  "windSpeed": "1.88m/s",
  "windDeg": 271,
  "timezone": 3600,
  "location": "Yaoundé",
  "country": "CM",
  "weather": "overcast clouds"
}
```

This information is used as the `Weather` scalar for `cropData` object.

## Setting up

First clone this repository

```shell
git clone https://github.com/cropboard/weather-server
```

The change directory into it

```shell
cd weather-server
```

Go to [openweathermap](https://openweathermap.org) and create an account along with an API key.

Create a `.env` file and add the following inside

```env
OPENWEATHERMAP_API_KEY=<YOUR_API_KEY>
```

Install requirements by typing the following in your terminal

```shell
pip install -r requirements.txt
```

Now run with

```shell
uvicorn main:app --reload
```

Navigate to `/<CITY-NAME>` to view weather data for a city.
