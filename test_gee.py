import ee
from gee.fetch_satellite import fetch_satellite_image

# Initialize Earth Engine
ee.Initialize(project="crop-monitoring-ai")

# Delhi coordinates (example)
latitude = 28.6139
longitude = 77.2090

image = fetch_satellite_image(latitude, longitude)

print("Satellite image fetched successfully!")
print(image.getInfo())