import pytest
from src.pyweath.pyweath import *
from unittest.mock import patch


# Test get_todays_forecast_ll
def test_get_todays_forecast_ll_invalid_latlong():
    actual = "Invalid latitude/longitude, please try again."
    
    expected = get_todays_forecast_ll(-1000,-1000)
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_ll(1000,1000)
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_ll(100,100)
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_ll(-100,-100)
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_ll("4000", "1700")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_ll("abc", "def")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"
    
    expected = get_todays_forecast_ll("abc", 100.89)
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_ll("40.71", "abc")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

def test_get_todays_forecast_ll_success(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {
                "weather": [{"main": "Sunny", "description": "clear sky"}],
                "main": {"temp": 25, "feels_like": 24, "humidity": 50},
                "wind": {"speed": 3},
                "visibility": 10000,
                "sys": {"sunrise": 1589644322, "sunset": 1589695322},
            }

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    expected_response = (
        "Position: 50, 30 \n"
        "Weather: Sunny\n"
        "Details: clear sky\n"
        "Temperature: 25°C\n"
        "Feels like: 24°C\n"
        "Humidity: 50%\n"
        "Wind speed: 3m/s\n"
        "Visibility: 10000m\n"
        "Sunrise: 1589644322\n"
        "Sunset: 1589695322\n"
    )
    assert get_todays_forecast_ll(50, 30) == expected_response

def test_get_todays_forecast_ll_invalid_json(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {"weather": "Sunny", }

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    expected = "Invalid latitude/longitude, please try again."
    actual = get_todays_forecast_ll(50, 30)
    assert actual == expected



# Test get_todays_forecast_city
def test_get_todays_forecast_city_invalid_city():
    actual = "City not found, please try again."
    
    expected = get_todays_forecast_city("abc")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_city("def")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_city("Nw York City")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_city("Nebrska")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_city("Prais")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_city("Londn")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_city("Ls Angeles")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_city("Xi'an famous foods")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = get_todays_forecast_city("yz")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

def test_get_todays_forecast_city_success(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {
                "weather": [{"main": "Partly Cloudy", "description": "some clouds"}],
                "main": {"temp": 15, "feels_like": 14, "humidity": 50},
                "wind": {"speed": 3},
                "visibility": 10000,
                "sys": {"sunrise": 1589644322, "sunset": 1589695322},
            }

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    expected = (
        "City: Miami \n"
        "Weather: Partly Cloudy\n"
        "Details: some clouds\n"
        "Temperature: 15°C\n"
        "Feels like: 14°C\n"
        "Humidity: 50%\n"
        "Wind speed: 3m/s\n"
        "Visibility: 10000m\n"
        "Sunrise: 1589644322\n"
        "Sunset: 1589695322\n"
    )

    actual = get_todays_forecast_city("Miami")

    assert actual == expected

def test_get_todays_forecast_city_invalid_json(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {"weather": "Partly Cloudy", }

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    expected_response = "City not found, please try again."
    assert get_todays_forecast_city("New York") == expected_response



# Test fiveday_forecast_city
def test_fiveday_forecast_city_invalid_city():
    actual = "City not found, please try again."
    
    expected = fiveday_forecast_city("abc")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = fiveday_forecast_city("def")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = fiveday_forecast_city("Nw York City")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = fiveday_forecast_city("Nebrska")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = fiveday_forecast_city("Prais")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = fiveday_forecast_city("Londn")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = fiveday_forecast_city("Ls Angeles")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = fiveday_forecast_city("Xi'an famous foods")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

    expected = fiveday_forecast_city("McDonalds")
    assert actual == expected, f"Expected: {actual}, Got: {expected}"

def test_fiveday_forecast_city_nograph_success(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {
                "list": [
                    {"main": {"temp": 15}}, {"main": {"temp": 16}}, {"main": {"temp": 17}},
                    {"main": {"temp": 18}}, {"main": {"temp": 19}}, {"main": {"temp": 20}},
                    {"main": {"temp": 21}}, {"main": {"temp": 22}}, {"main": {"temp": 23}},
                    {"main": {"temp": 24}}, {"main": {"temp": 25}}, {"main": {"temp": 26}},
                    {"main": {"temp": 27}}, {"main": {"temp": 28}}, {"main": {"temp": 29}},
                    {"main": {"temp": 30}}, {"main": {"temp": 31}}, {"main": {"temp": 32}},
                    {"main": {"temp": 33}}, {"main": {"temp": 34}}, {"main": {"temp": 35}},
                    {"main": {"temp": 36}}, {"main": {"temp": 37}}, {"main": {"temp": 38}},
                    {"main": {"temp": 39}}, {"main": {"temp": 40}}, {"main": {"temp": 41}},
                    {"main": {"temp": 42}}, {"main": {"temp": 43}}, {"main": {"temp": 44}},
                    {"main": {"temp": 45}}, {"main": {"temp": 46}}, {"main": {"temp": 47}},
                    {"main": {"temp": 48}}, {"main": {"temp": 49}}, {"main": {"temp": 50}},
                    {"main": {"temp": 51}}, {"main": {"temp": 52}}, {"main": {"temp": 53}},
                    {"main": {"temp": 54}}, {"main": {"temp": 55}}, {"main": {"temp": 56}},
                    {"main": {"temp": 57}}, {"main": {"temp": 58}}, {"main": {"temp": 59}},
                    {"main": {"temp": 60}}, {"main": {"temp": 61}}, {"main": {"temp": 62}},
                    {"main": {"temp": 63}}, {"main": {"temp": 64}}, {"main": {"temp": 65}},
                    {"main": {"temp": 66}}, {"main": {"temp": 67}}, {"main": {"temp": 68}},
                    {"main": {"temp": 69}}, {"main": {"temp": 70}}, {"main": {"temp": 71}},
                    {"main": {"temp": 72}}, {"main": {"temp": 73}}, {"main": {"temp": 74}},
                    {"main": {"temp": 75}}, {"main": {"temp": 76}}, {"main": {"temp": 77}},
                    {"main": {"temp": 78}}, {"main": {"temp": 79}}, {"main": {"temp": 80}},
                    {"main": {"temp": 81}}, {"main": {"temp": 82}}, {"main": {"temp": 83}},
                    {"main": {"temp": 84}}, {"main": {"temp": 85}}, {"main": {"temp": 86}},
                    {"main": {"temp": 87}}, {"main": {"temp": 88}}, {"main": {"temp": 89}},
                    {"main": {"temp": 90}}, {"main": {"temp": 91}}, {"main": {"temp": 92}},
                    {"main": {"temp": 93}}, {"main": {"temp": 94}}, {"main": {"temp": 95}},
                    {"main": {"temp": 96}}, {"main": {"temp": 97}}, {"main": {"temp": 98}},
                    {"main": {"temp": 99}}, {"main": {"temp": 100}},
                ]
            }

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    expected_response = [
        15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
        25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
        35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
        45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
        55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
        65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
        75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
        85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
        95, 96, 97, 98, 99, 100
    ]
    
    with patch("builtins.input", return_value="n"):
        actual = fiveday_forecast_city("New York")
        assert actual == expected_response

def test_fiveday_forecast_graph_success(): 
    with patch("builtins.input", return_value="y"):
        expected = "Graph displayed. \n"
        #print("CLOSE GRAPH TO SEE TEST RESULTS")
        actual = fiveday_forecast_city("London")
        assert actual == expected

def test_fiveday_forecast_graph_failures():
    with patch("builtins.input", return_value="y"):
        expected = "City not found, please try again."
        actual = fiveday_forecast_city("Lesster")
        assert actual == expected



# Test get_todays_airqual_city
def test_get_today_airqual_city_success(monkeypatch):
    class MockGeoResponse:
        @staticmethod
        def json():
            return [{'lat': 51.5073, 'lon': -0.1276, 'name': 'New York'}]

    class MockAirQualityResponse:
        @staticmethod
        def json():
            return {
                'list': [{'main': {'aqi': 2}, 'components': {'co': 240.33, 'no': 0.78, 'no2': 12.51, 'o3': 90.84, 'so2': 5.72, 'pm2_5': 0.78, 'pm10': 1.02, 'nh3': 0.68}}]
            }

    monkeypatch.setattr("requests.get", lambda url, params=None: MockGeoResponse() if "geo" in url else MockAirQualityResponse())
    monkeypatch.setattr("builtins.input", lambda prompt: "n")

    expected = "City: New York \nAir Quality: Fair (2)\n"
    actual = get_today_airqual_city("New York")
    assert actual == expected, f"Expected: {expected}, Got: {actual}"

def test_get_today_airqual_city_failures():
    expected = "City not found, please try again."
    actual = get_today_airqual_city("Nouvelle York")
    assert actual == expected, f"Expected: {expected}, Got: {actual}"

    actual = get_today_airqual_city("UNKNOWN")
    assert actual == expected, f"Expected: {expected}, Got: {actual}"

    actual = get_today_airqual_city(10003)
    assert actual == expected, f"Expected: {expected}, Got: {actual}"

def test_get_today_airqual_city_invalid_json(monkeypatch):
    expected = "City not found, please try again."
    class MockResponse:
        @staticmethod
        def json():
            return {"list": "Fair"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    assert get_today_airqual_city("New York") == expected

    monkeypatch.setattr("requests.get", lambda url, params=None: MockResponse())
    assert get_today_airqual_city("New York") == expected
