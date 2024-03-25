import requests
import matplotlib.pyplot as plt

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/onecall?"

    def get_weather_data(self, lat, lon):
        url = f"{self.base_url}lat={lat}&lon={lon}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        return response.json()

    def get_current_weather(self, lat, lon):
        weather_data = self.get_weather_data(lat, lon)
        return weather_data['current']

    def get_hourly_forecast(self, lat, lon):
        weather_data = self.get_weather_data(lat, lon)
        return weather_data['hourly']

    def get_daily_forecast(self, lat, lon):
        weather_data = self.get_weather_data(lat, lon)
        return weather_data['daily']

    def plot_temperature(self, lat, lon):
        weather_data = self.get_weather_data(lat, lon)
        temperatures = [hour['temp'] for hour in weather_data['hourly']]
        plt.plot(temperatures)
        plt.xlabel('Hour')
        plt.ylabel('Temperature (°C)')
        plt.title('Hourly Temperature Forecast')
        plt.show()
