from fastapi import APIRouter
from backend.services.recommendation_service import RecommendationService
from backend.schemas.recommendation_schema import RecommendationResponse

router = APIRouter(
    prefix="/recommendation",
    tags=["Recommendation"]
)

service = RecommendationService()


@router.get("/", response_model=RecommendationResponse)
def recommendation(
    ndvi: float,
    temperature: float,
    humidity: float,
    rain: float
):

    return service.recommend(
        ndvi,
        temperature,
        humidity,
        rain
    )