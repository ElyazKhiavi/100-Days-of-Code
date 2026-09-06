import requests
from dotenv import load_dotenv
import os

# https://openweathermap.org/api/current?collection=current_forecast
# Current weather data
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}


### Call 5 day / 3 hour forecast data
### api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

API = "http://api.openweathermap.org/data/2.5/forecast"
load_dotenv()
API_KEY = os.getenv("API_KEY")

WEATHER_PARAMS = {
    "lat": 38.0739964,
    "lon": 46.2961952,
    "appid": API_KEY,
    "units": "metric",
    "lang": "en",
    "cnt": 4,
}


response = requests.get(url=API, params=WEATHER_PARAMS)
response.raise_for_status()

print(response)  # <Response [200]>


print(response.json())  # the json response
