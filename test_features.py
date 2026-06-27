from gee.feature_extractor import FeatureExtractor
import ee

PROJECT_ID = "crop-monitoring-ai"   # <-- Replace if different

extractor = FeatureExtractor(PROJECT_ID)

latitude = 28.6139
longitude = 77.2090

point = ee.Geometry.Point([longitude, latitude])

image = extractor.load_image(
    latitude,
    longitude,
    "2025-06-01",
    "2025-09-30"
)

features = extractor.extract_single_image_features(
    image,
    point
)

print(features)