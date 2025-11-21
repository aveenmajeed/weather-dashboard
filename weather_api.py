# weather_api.py
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/"

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    
    def get_local_city(self):
        try:
            r = requests.get("http://ip-api.com/json/")
            data = r.json()
            if data["status"] == "success":
                return data["city"]
            else:
                return None
        except:
            return None


    def get_current_weather(self, city):
        url = f"{BASE_URL}weather?q={city}&appid={self.api_key}&units=metric"
        r = requests.get(url)

        if r.status_code != 200:
            print("ERROR:", r.status_code, r.text)
            return None
        
        data = r.json()
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"]
        }

    def get_forecast(self, city):
        url = f"{BASE_URL}forecast?q={city}&appid={self.api_key}&units=metric"
        r = requests.get(url)

        if r.status_code != 200:
            return None
        
        data = r.json()
        
        forecast_list = []
        for entry in data["list"]:
            forecast_list.append({
                "time": entry["dt_txt"],
                "temp": entry["main"]["temp"],
                "description": entry["weather"][0]["description"]
            })
        return forecast_list
