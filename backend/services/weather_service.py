import requests


class WeatherService:

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, latitude, longitude):

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "rain",
                "cloud_cover",
                "wind_speed_10m"
            ]
        }

        response = requests.get(self.BASE_URL, params=params)

        return response.json()