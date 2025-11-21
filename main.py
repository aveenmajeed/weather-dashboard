# main.py
from weather_api import WeatherAPI
from utils import print_current_weather, print_forecast, print_ascii_chart

API_KEY = "bcaeb20389984c3a5875bbf82ea64260"   # ← replace this with your actual key

weather = WeatherAPI(API_KEY)

def main():
    print("==== Weather Dashboard ====")
    
    while True:
        city = input("\nEnter a city name, 'local' to auto-detect, or 'q' to quit: ").strip()
        if city.lower() == "q":
            print("Goodbye!")
            break

        if city.lower() == "local":
            print("Detecting your location...")
            detected_city = weather.get_local_city()
            if detected_city is None:
                print("Could not detect your location. Try entering a city manually.")
                continue

            print(f"Detected city: {detected_city}")
            city = detected_city


        current = weather.get_current_weather(city)
        if current is None:
            print("City not found or API error. Try again.")
            continue

        print_current_weather(current)

        see_forecast = input("See 5-day forecast? (y/n): ").strip().lower()
        if see_forecast == "y":
            forecast = weather.get_forecast(city)
            print_forecast(forecast)

            see_chart = input("Show ASCII temperature chart? (y/n): ").strip().lower()
            if see_chart == "y":
                print_ascii_chart(forecast)

if __name__ == "__main__":
    main()
