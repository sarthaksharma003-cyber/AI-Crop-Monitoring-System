from fastapi import APIRouter
from backend.services.weather_service import WeatherService

router = APIRouter(prefix="/weather", tags=["Weather"])

weather_service = WeatherService()


@router.get("/")
def weather(latitude: float, longitude: float):

    return weather_service.get_weather(latitude, longitude)