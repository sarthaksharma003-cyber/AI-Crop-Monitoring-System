class MoistureService:

    def calculate_stress(self, ndvi, ndmi):

        # Healthy vegetation with good moisture
        if ndvi >= 0.70 and ndmi >= 0.35:
            return {
                "stress": "Low",
                "score": 0.1,
                "recommendation": "No immediate irrigation required."
            }

        # Moderate vegetation or moderate moisture
        elif ndvi >= 0.45 and ndmi >= 0.20:
            return {
                "stress": "Moderate",
                "score": 0.5,
                "recommendation": "Monitor field closely."
            }

        # Poor vegetation or low moisture
        else:
            return {
                "stress": "High",
                "score": 0.9,
                "recommendation": "Immediate irrigation recommended."
            }