from pydantic import BaseModel


class RecommendationResponse(BaseModel):
    health: str
    recommendation: str
    reason: str