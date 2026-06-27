import requests

BASE_URL = "http://127.0.0.1:8000"


def get_ndvi(latitude, longitude):

    response = requests.get(
        f"{BASE_URL}/ndvi",
        params={
            "latitude": latitude,
            "longitude": longitude
        }
    )

    return response.json()