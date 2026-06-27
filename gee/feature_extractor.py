import ee


class FeatureExtractor:

    def __init__(self, project_id):
        ee.Initialize(project=project_id)

    def load_image(self, latitude, longitude, start_date, end_date):
        """
        Load the least cloudy Sentinel-2 image for a location and date range.
        """

        point = ee.Geometry.Point([longitude, latitude])

        image = (
            ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
            .filterBounds(point)
            .filterDate(start_date, end_date)
            .sort("CLOUDY_PIXEL_PERCENTAGE")
            .first()
        )

        return image

    def calculate_indices(self, image):
        """
        Calculate vegetation indices.
        """

        ndvi = image.normalizedDifference(["B8", "B4"]).rename("NDVI")

        ndmi = image.normalizedDifference(["B8", "B11"]).rename("NDMI")

        evi = image.expression(
            "2.5*((NIR-RED)/(NIR+6*RED-7.5*BLUE+1))",
            {
                "NIR": image.select("B8"),
                "RED": image.select("B4"),
                "BLUE": image.select("B2")
            }
        ).rename("EVI")

        savi = image.expression(
            "1.5*((NIR-RED)/(NIR+RED+0.5))",
            {
                "NIR": image.select("B8"),
                "RED": image.select("B4")
            }
        ).rename("SAVI")

        return (
            image
            .addBands(ndvi)
            .addBands(ndmi)
            .addBands(evi)
            .addBands(savi)
        )

    def get_multitemporal_collection(
        self,
        latitude,
        longitude,
        start_date,
        end_date
    ):
        """
        Get all Sentinel-2 images for a location and date range.
        """

        point = ee.Geometry.Point([longitude, latitude])

        collection = (
            ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
            .filterBounds(point)
            .filterDate(start_date, end_date)
            .sort("system:time_start")
        )

        return collection

    def image_count(self, collection):
        """
        Return the number of images in the collection.
        """

        return collection.size().getInfo()
    

    def extract_single_image_features(self, image, point):

        image = self.calculate_indices(image)

        values = image.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=point,
            scale=10,
            maxPixels=1e9
        )

        return values.getInfo()