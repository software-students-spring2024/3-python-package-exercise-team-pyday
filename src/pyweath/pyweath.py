import requests, os
import matplotlib.pyplot as plt
import numpy as np


api_key = os.getenv('API_KEY')
base_url = "http://api.openweathermap.org/data/2.5/"


def get_todays_forecast_ll(lat, lon):
    """
    Retrieve today's weather forecast for a specific longitude/latitude position, can accept str/float vals.
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


def fiveday_forecast_city(city):
    """
    Retrieve five day weather forecast for a specificied city.
    """
    try:
        url = f"{base_url}forecast?q={city}&appid={api_key}&units=metric"
        weather_data = requests.get(url).json()
        temps = [hour["main"]["temp"] for hour in weather_data["list"]]
        
        see_graph = input("Would you like to see the graph? (y/n): ")
        if see_graph.lower() == "y":
            fig = plt.figure(figsize=(10, 6))  
            
            plt.plot(temps, color='blue', linestyle='-', linewidth=2)
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.xlabel('Hours from current time (5-days)', fontsize=12)  
            plt.ylabel('Temperature (°C)', fontsize=12)
            plt.title(f'Temperature Changes Over Next 5 Days in {city}', fontsize=14) 
            hours = np.arange(0, len(temps), 3)  # show ticks every 3 hours
            plt.xticks(hours, [3 + i*3 for i in hours])  
            
            plt.yticks(np.arange(min(temps), max(temps)+1, 5))
            plt.legend(['Temperature'], loc='upper right')
            
            plt.show()
            plt.close(fig)
            return "Graph displayed. \n" 
        else:
            print("Temperatures for the next 5 days: ")
            return(temps)
        
    except:
        return "City not found, please try again."

def get_today_airqual_city(city):
    """
    Retrieve today's air quality for a specificied city, uses Geocoder API to locate coordinates.
    """
    try:
        geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"
        geo_data = requests.get(geo).json()
        lat, long = geo_data[0]["lat"], geo_data[0]["lon"]
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={long}&appid={api_key}"
        airquality_data = requests.get(url).json()
        air = airquality_data["list"][0]["main"]["aqi"]
        names = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}
        give_extra = input("Would you like to see extra air quality details? (y/n): ")
        if give_extra.lower() == "y":
            extra = f'\nCO: {airquality_data["list"][0]["components"]["co"]} µg/m³\nNO: {airquality_data["list"][0]["components"]["no"]} µg/m³\nNO2: {airquality_data["list"][0]["components"]["no2"]} µg/m³\nO3: {airquality_data["list"][0]["components"]["o3"]} µg/m³\nSO2: {airquality_data["list"][0]["components"]["so2"]} µg/m³\nPM2.5: {airquality_data["list"][0]["components"]["pm2_5"]} µg/m³\nPM10: {airquality_data["list"][0]["components"]["pm10"]} µg/m³\nNH3: {airquality_data["list"][0]["components"]["nh3"]} µg/m³\n'
        else:
            extra = ""
        return f'City: {geo_data[0]["name"]} \nAir Quality: {names[air]} ({air})\n{extra}'
    except:
        return "City not found, please try again."

