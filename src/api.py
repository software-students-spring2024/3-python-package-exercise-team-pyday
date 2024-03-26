import requests, os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

class WeatherAPI:
    def __init__(self):
        """
        Initialize the WeatherAPI with a given API key.
        """
        self.api_key = os.getenv('API_KEY')
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def get_weather_data(self, lat, lon):
        """
        Fetch weather data for a specific latitude and longitude.
        """
        url = f"{self.base_url}lat={lat}&lon={lon}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        return response.json()
    
    def get_current_weather(self, lat, lon):
        """Retrieve current weather information for a specific location."""
        weather_data = self.get_weather_data(lat, lon)
        return weather_data['main']['temp']  # 'main' contains the current weather information

    def get_hourly_forecast(self, lat, lon):
        """
        Retrieve the hourly weather forecast for a specific location.
        """
        weather_data = self.get_weather_data(lat, lon)
        return weather_data['hourly']

    def get_daily_forecast(self, lat, lon):
        """
        Retrieve the daily weather forecast for a specific location.
        """
        weather_data = self.get_weather_data(lat, lon)
        return weather_data['daily']

    def plot_temperature(self, lat, lon):
        """
        Plot the hourly temperature forecast for a specific location.
        """
        weather_data = self.get_weather_data(lat, lon)
        temperatures = [hour['temp'] for hour in weather_data['hourly']]
        plt.plot(temperatures)
        plt.xlabel('Hour')
        plt.ylabel('Temperature (°C)')
        plt.title('Hourly Temperature Forecast')
        plt.show()

x = WeatherAPI()
print(x.get_current_weather(37.7749, -122.4194))