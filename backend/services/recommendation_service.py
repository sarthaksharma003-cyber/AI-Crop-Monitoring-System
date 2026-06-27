class RecommendationService:

    def recommend(
        self,
        ndvi,
        temperature,
        humidity,
        rain
    ):

        # Healthy crop

        if ndvi > 0.7:

            if rain > 0:

                return {
                    "health": "Healthy",
                    "recommendation": "Do not irrigate today.",
                    "reason": "Rain is expected and vegetation is healthy."
                }

            return {
                "health": "Healthy",
                "recommendation": "Light irrigation if soil is dry.",
                "reason": "Healthy vegetation with no rainfall."
            }

        # Moderate crop

        if ndvi > 0.4:

            return {
                "health": "Moderate",
                "recommendation": "Monitor crop and irrigate if needed.",
                "reason": "Moderate vegetation health."
            }

        # Poor crop

        return {
            "health": "Poor",
            "recommendation": "Immediate irrigation recommended.",
            "reason": "Vegetation is stressed."
        }