from fastapi import FastAPI

from backend.routes.ndvi import router as ndvi_router
from backend.routes.weather import router as weather_router
from backend.routes.recommendation import router as recommendation_router


app = FastAPI(
    title="AI Crop Monitoring",
    version="1.0"
)

app.include_router(ndvi_router)
app.include_router(weather_router)
app.include_router(recommendation_router)



@app.get("/")
def home():

    return {
        "status": "Backend Running"
    }