from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
print(f"Key -> {API_KEY} ")

app = FastAPI()

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def _handle_root():
    return {"message": "Welcome to Cropboard weather server. Navigate to /any-city-name to get weather data for that city"}


@app.get("/{city}")
def _server_weather_data(request: Request, city: str):
    weather_response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").json()

    pprint(weather_response)
    weather_data = {
        "lat": weather_response['coord']['lat'],
        "lon": weather_response['coord']['lon'],
        "temp": f"{weather_response['main']['temp']} F",
        "pressure": f"{weather_response['main']['pressure']}hPa",
        "humidity": f"{weather_response['main']['humidity']}%",
        "visibility": f"{weather_response['visibility']/1000}km",
        "windSpeed": f"{weather_response['wind']['speed']}m/s",
        "windDeg": weather_response['wind']['deg'],
        "timezone": weather_response['timezone'],
        "location": weather_response['name'],
        "country": weather_response['sys']['country'],
        "weather": weather_response['weather'][0]['description']
    }

    print(weather_data)
    return weather_data
