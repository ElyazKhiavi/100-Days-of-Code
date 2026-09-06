import requests
from dotenv import load_dotenv
import os

# https://openweathermap.org/api/geocoding-api
# Geocoding API
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
# http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API key}


API = "http://api.openweathermap.org/geo/1.0/direct"
load_dotenv()
API_KEY = os.getenv('API_KEY')

GEO_PARAMS = {"q": "Tabriz", "limit": 1, "appid": API_KEY, "lang": "en"}


connection = requests.get(url=API, params=GEO_PARAMS)
connection.raise_for_status()
print(connection)  # <Response [200]>


print(
    connection.json()
)  # [{'name': 'Tabriz', 'local_names': {'ku': 'Tewrêz', 'et': 'Tabrīz', 'lt': 'Tebrizas', 'he': 'תבריז', 'fa': 'تبریز', 'az': 'Təbriz', 'feature_name': 'Tabriz', 'fi': 'Tabriz', 'hi': 'तबरेज़', 'uk': 'Тебриз', 'ru': 'Тебриз', 'zh': '大不里士', 'cs': 'Tabríz', 'ascii': 'Tabriz', 'la': 'Tauris', 'de': 'Täbris', 'nl': 'Tabriz', 'pl': 'Tebriz', 'es': 'Tabriz', 'tr': 'Tebriz', 'ja': 'タブリーズ', 'fr': 'Tabriz', 'pt': 'Tabriz', 'en': 'Tabriz', 'ml': 'തബ്രീസ്'}, 'lat': 38.0739964, 'lon': 46.2961952, 'country': 'IR', 'state': 'East Azerbaijan Province'}]
