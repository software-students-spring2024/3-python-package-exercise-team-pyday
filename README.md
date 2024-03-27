![Python build & test](https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday/actions/workflows/build.yaml/badge.svg)



# PyWeath

PyWeath is a Python package designed for developers looking to integrate weather forecasting features into their applications. Using the OpenWeatherMap API, PyWeath provides access to current weather conditions, air quality data, and a five day weather forecast for any location specified by city name or latitude/longitude position.

## Docs

### get_todays_forecast_ll(lat, lon)
*Retrieves today's weather forecast based on latitude and longitude.*

<!-- 
Simulate flipping one or more coins. 
* num_coins: The number of coins to flip (default is 1).

Example:


Parameters:

- lat (float): Latitude of the location.
- lon (float): Longitude of the location.

Returns:

- string: A string containing weather conditions and details such as temperature, humidity, visibility, wind speed, sunrise, and sunset times.

Example:
```py
print(get_todays_forecast_ll(40.7128, -74.0060))

```
Copy code   

get_todays_forecast_city(city)
Retrieves today's weather forecast for a specified city.

Parameters:
city (str): Name of the city.
Returns:
string: A string containing weather conditions and details such as temperature, humidity, visibility, wind speed, sunrise, and sunset times.
Example:
python
Copy code
print(get_todays_forecast_city("New York"))

### fiveday_forecast_city( int:city)
Retrieves a five-day weather forecast for a specified city.

Parameters:
city (str): Name of the city.
Returns:
Depending on user input, either displays a graph of temperature changes over the next five days or prints a list of temperatures every three hours.
Example:
python
Copy code
fiveday_forecast_city("London")
get_today_airqual_city(city)
Retrieves today's air quality index and detailed pollutant data for a specified city.

Parameters:
city (str): Name of the city.
Returns:
string: A string containing the air quality index and, optionally, detailed pollutant concentrations such as CO, NO, NO2, O3, SO2, PM2.5, PM10, and NH3 levels.
Example:
python
Copy code
print(get_today_airqual_city("Beijing")) -->
<!-- ### Getting an API Key

1. Sign up for the free version of an OpenWeatherMap account and obtain an API key.
2. Set an environment variable on your system to store this key:

   - On Linux/macOS: `export OPENWEATHERMAP_API_KEY='your_api_key_here'`
   - On Windows: Set `OPENWEATHERMAP_API_KEY` as a system environment variable through the System Properties.

### Configuring the Project

1. Clone the repository and navigate to the project directory.
2. (If using a `.env` file for local development) Create a `.env` file in the root directory and add `OPENWEATHERMAP_API_KEY=your_api_key_here`. Make sure `.env` is listed in your `.gitignore` file to prevent it from being committed. -->

## Contributors
- [Sang In (Harry) Kang](https://github.com/sik247)
- [Jean Luis Adrover](https://github.com/jladrover)