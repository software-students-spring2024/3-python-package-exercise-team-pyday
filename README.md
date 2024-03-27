![Python build & test](https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday/actions/workflows/build.yaml/badge.svg)



# PyWeath

PyWeath is a Python package designed for developers looking to integrate weather forecasting features into their applications. Using the OpenWeatherMap API, PyWeath provides access to current weather conditions, air quality data, and a five day weather forecast for any location specified by city name or latitude/longitude position.

### PyPi Link: 

## Docs

### get_todays_forecast_ll(lat, lon)

Example:
```py
print(get_todays_forecast_ll(40.7128, -74.0060))
```
For more: [example python program](https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday/blob/main/example.py)

### get_todays_forecast_city(lat, lon)
*Retrieves today's weather forecast based on city, returns a string.*

Example:
```py
print(get_todays_forecast_ctiy("Tokyo"))
```
For more: [example python program](https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday/blob/main/example.py)

### fiveday_forecast_city(city)
*Retrieves five day weather forecast graph or list of temperatures for a specificied city, based off user input, outputs graph or list of strings.*

Example_
```py
fiveday_forecast_city("Dubai")
Would you like to see the graph? (y/n): n
```
For more: [example python program](https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday/blob/main/example.py)

### get_today_airqual_city(city):
*Retrieve today's air quality for a specificied city using Geocoder API to locate coordinates, returns a string. Extra details about componenets in air are available upon user input.*

Example:

```py
print(get_todays_airqual_city("New York"))
Would you like to see extra air quality details? (y/n): y
```
For more: [example python program](https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday/blob/main/example.py)


## Installing

## Contributing



## Contributors
- [Sang In (Harry) Kang](https://github.com/sik247)
- [Jean Luis Adrover](https://github.com/jladrover)

