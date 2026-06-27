from fastapi import APIRouter
from gee.ndvi import NDVIService

router = APIRouter(prefix="/ndvi", tags=["NDVI"])

PROJECT_ID = "crop-monitoring-ai"

service = NDVIService(PROJECT_ID)


@router.get("/")
def get_ndvi(latitude: float, longitude: float):

    result = service.get_ndvi_map(latitude, longitude)

    return {
        "status": "success",
        "tile_fetcher": result["tile_fetcher"].url_format
    }