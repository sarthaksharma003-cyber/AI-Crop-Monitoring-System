from gee.feature_extractor import FeatureExtractor

PROJECT_ID = "crop-monitoring-ai"

extractor = FeatureExtractor(PROJECT_ID)

collection = extractor.get_multitemporal_collection(
    28.6139,
    77.2090,
    "2025-06-01",
    "2025-09-30"
)

print("Images Found :", extractor.image_count(collection))