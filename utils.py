# utils.py

def print_current_weather(w):
    print("\n=== Current Weather ===")
    print(f"City: {w['city']}")
    print(f"Temperature: {w['temp']}°C")
    print(f"Feels Like: {w['feels_like']}°C")
    print(f"Humidity: {w['humidity']}%")
    print(f"Condition: {w['description'].title()}")
    print("=======================\n")


def print_forecast(forecast):
    print("\n=== 5-Day Forecast (Every 3 Hours) ===")
    for entry in forecast[:10]:   # show only first ~1.5 days to keep it short
        print(f"{entry['time']}: {entry['temp']}°C | {entry['description']}")
    print("======================================\n")

def print_ascii_chart(forecast):
    print("\n=== Temperature Chart (Next 10 Entries) ===")

    # Only display first 10 entries
    data = forecast[:10]

    for entry in data:
        temp = entry['temp']
        bar_length = int(temp) if temp > 0 else int(abs(temp)/2)  # smaller bars for negative temps
        bar = "#" * bar_length

        print(f"{entry['time'][:16]} | {temp:>5}°C | {bar}")

    print("==========================================\n")
