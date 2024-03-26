import requests, os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather_data(lat, lon):
    """
    Fetch weather data for a specific latitude and longitude.
    """
    url = f"{base_url}lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()


def get_temp_ll(self, lat, lon):
    """
    Retrieve current weather information for a specific longitude/latitude position.
    """
    try:
        weather_data = get_weather_data(lat, lon)
        return weather_data['main']['temp']  # 'main' contains the current weather information
    except:
        return "Invalid latitude/longitude, please try again."


def get_temp_city(city):
    """
    Retrieve current weather information for a specific city.
    """
    url = f"{base_url}q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        return response['main']['temp']  # 'main' contains the current weather information
    except:
        return "City not found, please try again."

#todo
def get_hourly_forecast(lat, lon):
    """
    Retrieve the hourly weather forecast for a specific location.
    """
    weather_data = get_weather_data(lat, lon)
    return weather_data


def get_daily_forecast(lat, lon):
    """
    Retrieve the daily weather forecast for a specific location.
    """
    weather_data = get_weather_data(lat, lon)
    return weather_data['daily']

# def plot_temperature(lat, lon):
#     """
#     Plot the hourly temperature forecast for a specific location.
#     """
#     weather_data = self.get_weather_data(lat, lon)
#     temperatures = [hour['temp'] for hour in weather_data['hourly']]
#     plt.plot(temperatures)
#     plt.xlabel('Hour')
#     plt.ylabel('Temperature (°C)')
#     plt.title('Hourly Temperature Forecast')
#     plt.show()


print(get_hourly_forecast(40.7128, -74.0060))