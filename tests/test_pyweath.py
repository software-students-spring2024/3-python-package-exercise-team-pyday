import os, pytest
from src.pyweath.pyweath import *
def test_get_todays_forecast_ll():
    lat, lon = 40.7128, -74.0060
    forecast = get_todays_forecast_ll(lat, lon)
    
    assert forecast is not None
    #assert 'temperature' in forecast
    #assert 'humidity' in forecast

def test_get_todays_forecast_city():
    city = "New York"
    forecast = get_todays_forecast_city(city)
    #assert isinstance(forecast, dict)
    # assert 'temperature' in forecast
    #assert 'humidity' in forecast

def test_fiveday_forecast_city():
    city = "New York"
    forecast = fiveday_forecast_city(city)
    #assert isinstance(forecast, list)
    #assert len(forecast) == 5

def test_get_today_airqual_city():
    city = "New York"
    air_quality = get_today_airqual_city(city)
    #assert isinstance(air_quality, str)
    #assert air_quality in ['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous']

def test_get_today_airqual_city_invalid_city():
    city = "Invalid City"
    #with pytest.raises(Exception):
    #    get_today_airqual_city(city)
