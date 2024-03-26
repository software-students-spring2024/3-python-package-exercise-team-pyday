from src.pyweath import *

example_lat, example_lon = 40.7128, -74.0060
print(get_todays_forecast_ll(example_lat, example_lon))

example_city = "Dubai"
print(get_todays_forecast_city(example_city))

fiveday_forecast_city(example_city)

print(get_today_airqual_city(example_city))