from fastapi import APIRouter

from backend.services.moisture_service import MoistureService

router = APIRouter(
    prefix="/moisture",
    tags=["Moisture Stress"]
)

service = MoistureService()


@router.get("/")
def moisture(
    ndvi: float,
    ndmi: float
):
    return service.calculate_stress(
        ndvi,
        ndmi
    )