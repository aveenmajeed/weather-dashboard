# Weather Dashboard

A Python command-line weather dashboard that retrieves real-time weather data using the OpenWeatherMap API. The project includes automatic location detection, a five-day forecast, and an ASCII-based temperature visualization system.

---

## Features

### Real-Time Weather
Users can enter any city and view:
- Current temperature
- Feels-like temperature
- Humidity
- General weather conditions

### Auto-Detect Location
Users can type "local" to automatically:
- Detect their current city via IP geolocation
- Retrieve weather data without manual entry

### Five-Day Forecast
Displays future weather conditions in three-hour intervals.

### ASCII Temperature Chart
Provides a simple terminal-based graph of upcoming temperatures.

### Modular Code Structure
The project is organized into multiple Python modules:
- `main.py` — application logic and CLI interaction
- `weather_api.py` — handles API requests and data retrieval
- `utils.py` — formatting, output utilities, and ASCII chart drawing

---

## Example Output

==== Weather Dashboard ====
Enter a city name, 'local' to auto-detect, or 'q' to quit: local
Detecting your location...
Detected city: Kanata
=== Current Weather ===
City: Kanata
Temperature: -4.59°C
Feels Like: -8.54°C
Humidity: 89%
Condition: Few Clouds
See 5-day forecast? (y/n): y
=== 5-Day Forecast (Every 3 Hours) ===
2025-11-19 12:00:00 | -4.53°C | clear sky
2025-11-19 15:00:00 | -5.85°C | clear sky
...
Show ASCII temperature chart? (y/n): y
=== Temperature Chart (Next 10 Entries) ===
2025-11-19 12:00 | -6.69°C | ###
2025-11-19 15:00 | -2.45°C | ##
2025-11-19 18:00 | -0.26°C | #
...

---

## Installation

### 1. Clone the repository

git clone https://github.com/aveenmajeed/weather-dashboard.git
cd weather-dashboard

### 2. Install required libraries

pip install requests

### 3. API Key Setup
Obtain a free API key from OpenWeatherMap and insert it into the project inside `weather_api.py`.

### 4. Run the Application

python main.py

---

## Requirements
- Python 3.10 or newer  
- `requests` library  
- OpenWeatherMap API key  

---

## Author
Aveen Majeed  
GitHub: https://github.com/aveenmajeed






Just tell me what style you want.
