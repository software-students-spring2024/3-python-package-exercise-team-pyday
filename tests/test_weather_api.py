import os
from src.pyweath import WeatherAPI

def test_get_current_weather():
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    assert api_key is not None, "API key must be set as environment variable"
    weather_api = WeatherAPI(api_key)
    lat, lon = 40.7128, -74.0060
    current_weather = weather_api.get_current_weather(lat, lon)
    assert 'temp' in current_weather
