from ai.crop_classification.dataset import DatasetGenerator

PROJECT_ID = "crop-monitoring-ai"   


generator = DatasetGenerator(PROJECT_ID)

sample = generator.generate_single_sample(
    latitude=28.6139,
    longitude=77.2090,
    crop="Wheat",
    start_date="2025-06-01",
    end_date="2025-06-30"
)

print(sample)