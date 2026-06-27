import pandas as pd
import ee

from gee.feature_extractor import FeatureExtractor


class DatasetGenerator:

    def __init__(self, project_id):

        self.extractor = FeatureExtractor(project_id)

    def generate_single_sample(
        self,
        latitude,
        longitude,
        crop,
        start_date,
        end_date
    ):

        point = ee.Geometry.Point(
            [longitude, latitude]
        )

        image = self.extractor.load_image(
            latitude,
            longitude,
            start_date,
            end_date
        )

        features = self.extractor.extract_single_image_features(
            image,
            point
        )

        features["Latitude"] = latitude
        features["Longitude"] = longitude
        features["Crop"] = crop

        return features