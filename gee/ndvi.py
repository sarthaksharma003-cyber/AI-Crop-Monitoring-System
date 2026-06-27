import ee


class NDVIService:

    def __init__(self, project_id: str):
        self.project_id = project_id
        ee.Initialize(project=self.project_id)

    def get_ndvi(self, latitude: float, longitude: float):

        point = ee.Geometry.Point([longitude, latitude])

        image = (
            ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
            .filterBounds(point)
            .filterDate("2025-01-01", "2025-12-31")
            .sort("CLOUDY_PIXEL_PERCENTAGE")
            .first()
        )

        ndvi = image.normalizedDifference(["B8", "B4"]).rename("NDVI")

        return ndvi

    def get_ndvi_map(self, latitude: float, longitude: float):

        ndvi = self.get_ndvi(latitude, longitude)

        vis = {
            "min": 0,
            "max": 1,
            "palette": [
                "red",
                "yellow",
                "green"
            ]
        }

        map_id = ndvi.getMapId(vis)

        return map_id