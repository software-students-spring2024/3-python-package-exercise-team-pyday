![Python build & test](https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday/actions/workflows/build.yaml/badge.svg)



# Pyweath

Pyweath is a Python package designed for developers looking to integrate weather forecasting features into their applications. Using the OpenWeatherMap API, Pyweath provides access to current weather conditions, air quality data, and a five day weather forecast for any location specified by city name or latitude/longitude position.

### PyPi Link: https://pypi.org/project/pyweath

## Documentation

### get_todays_forecast_ll(lat, lon)

Example:
```py
print(get_todays_forecast_ll(40.7128, -74.0060))
```
For more: [example python program](https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday/blob/main/example.py)

### get_todays_forecast_city(city)
*Retrieves today's weather forecast based on city, returns a string.*

Example:
```py
print(get_todays_forecast_ctiy("Tokyo"))
```
For more: [example python program](https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday/blob/main/example.py)

### fiveday_forecast_city(city)
*Retrieves five day weather forecast graph or list of temperatures for a specificied city, based off user input, outputs graph or list of strings.*

Example:
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


## Installation & Use

If using the package in your own python program:


1. Make a pipenv (managed virtual environment) and install latest version of pyweath via: ```pipenv install pyweath``` **Note:** If you've previously created a pipenv virtual environment in the same directory, you may have to delete the old one first. Find out where it is located with the pipenv --venv command. For more information see: https://pipenv.pypa.io/en/latest/.
2. Enter the virtual environment: ```pipenv shell```
3. Create a Python file (ex: ```my_program.py```). In the file, import pyweath to utilize its features (ex: ```from pyweath import *```). For more: [example python program](https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday/blob/main/example.py).
4. Run the program in terminal: ```python3 my_program.py.```
5. Close virtual environment when done: ```exit```



If using the package directly in terminal:

1. Create and enter a pipenv virtual environment as seen above in steps 1 & 2.
2. Run our package directly from the command line: ```python3 -m pyweath```. This should run the code located inside ```__main__.py```, in the src folder.
3. Close virtual environment when done: ```exit```


## Contributing

1. Clone this repo ```git clone https://github.com/software-students-spring2024/3-python-package-exercise-team-pyday```
2. Create and enter virtual environment as seen above. 
3. Install package: ```pipenv install pyweath```
5. Install the necessary dependencies: ```pipenv install pytest build twine requests matplotlib numpy```
6. If you wish to run the unit tests provided: ```pytest```
## Contributors
- [Sang In (Harry) Kang](https://github.com/sik247)
- [Jean Luis Adrover](https://github.com/jladrover)

