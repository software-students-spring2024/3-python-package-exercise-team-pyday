import requests, os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import numpy as np

load_dotenv()

api_key = os.getenv('API_KEY')
base_url = "http://api.openweathermap.org/data/2.5/"


def get_todays_forecast_ll(lat, lon):
    """
    Retrieve today's weather forecast for a specific longitude/latitude position.
    """
    try:
        url = f"{base_url}weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        weather_data = requests.get(url).json()
        return f'Position: {lat}, {lon} \nWeather: {weather_data["weather"][0]["main"]}\nDetails: {weather_data["weather"][0]["description"]}\nTemperature: {weather_data["main"]["temp"]}°C\nFeels like: {weather_data["main"]["feels_like"]}°C\nHumidity: {weather_data["main"]["humidity"]}%\nWind speed: {weather_data["wind"]["speed"]}m/s\nVisibility: {weather_data["visibility"]}m\nSunrise: {weather_data["sys"]["sunrise"]}\nSunset: {weather_data["sys"]["sunset"]}\n'
    except:
        return "Invalid latitude/longitude, please try again."
    

def get_todays_forecast_city(city):
    """
    Retrieve today's weather forecast for a specificied city.
    """
    try:
        url = f"{base_url}weather?q={city}&appid={api_key}&units=metric"
        weather_data = requests.get(url).json()
        return f'City: {city} \nWeather: {weather_data["weather"][0]["main"]}\nDetails: {weather_data["weather"][0]["description"]}\nTemperature: {weather_data["main"]["temp"]}°C\nFeels like: {weather_data["main"]["feels_like"]}°C\nHumidity: {weather_data["main"]["humidity"]}%\nWind speed: {weather_data["wind"]["speed"]}m/s\nVisibility: {weather_data["visibility"]}m\nSunrise: {weather_data["sys"]["sunrise"]}\nSunset: {weather_data["sys"]["sunset"]}\n'
    except:
        return "City not found, please try again."


def display_fiveday_temps_city(city):
    """
    Retrieve five day weather forecast for a specificied city.
    """
    try:
        url = f"{base_url}forecast?q={city}&appid={api_key}&units=metric"
        weather_data = requests.get(url).json()
        temps = [hour["main"]["temp"] for hour in weather_data["list"]]
        
        # Plotting temperature changes
        plt.figure(figsize=(10, 6))  # Adjust the figure size
        
        # Customize the line style and color
        plt.plot(temps, color='blue', linestyle='-', linewidth=2)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.xlabel('Hours from current time (5-days)', fontsize=12)  # Modify x-axis label
        plt.ylabel('Temperature (°C)', fontsize=12)
        plt.title('Temperature Changes Over Next 5 Day Forecast', fontsize=14)  # Modify title
        hours = np.arange(0, len(temps), 3)  # Show ticks every 3 hours
        plt.xticks(hours, [3 + i*3 for i in hours])  # Modify x-axis ticks
        
        plt.yticks(np.arange(min(temps), max(temps)+1, 5))
        plt.legend(['Temperature'], loc='upper right')
        
        plt.show()
        
    except:
        return "City not found, please try again."
    
# todo, ll version

# print(get_todays_forecast_ll(40.7128, -74.0060))
# print(get_todays_forecast_city("New York"))
#print(display_fiveday_temps_city("New York"))