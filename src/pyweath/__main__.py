from src.pyweath.pyweath import *

def main():
    try:
        example_lat, example_lon = input("Enter latitude and longitude separated by a comma: ").split(",")
        print(get_todays_forecast_ll(float(example_lat), float(example_lon)))
    except:
        print("Invalid input.")

    try:
        example_city = input("Enter city: ")
        print(get_todays_forecast_city(example_city))
        fiveday_forecast_city(example_city)
        print(get_today_airqual_city(example_city))
    except:
        print("Invalid input.")    

if __name__ == "__main__":
    main()
