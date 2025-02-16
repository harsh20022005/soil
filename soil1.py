import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class CropRecommendationSystem:
    def __init__(self):
        # Create balanced training data with more varied conditions
        soil_types = []
        temperatures = []
        humidities = []
        rainfalls = []
        phs = []
        crops = []

        # Alluvial soil data - varies with conditions
        for _ in range(10):
            soil_types.extend([1] * 6)
            temperatures.extend([25, 28, 24, 26, 27, 23])  # Different temperatures
            humidities.extend([70, 75, 72, 68, 73, 71])   # Different humidity levels
            rainfalls.extend([200, 180, 190, 185, 195, 188])  # Different rainfall
            phs.extend([6.5, 6.8, 6.7, 6.6, 6.9, 6.7])    # Different pH
            # Crops vary based on conditions
            crops.extend(['rice', 'wheat', 'sugarcane', 'jute', 'oilseeds', 'pulses'])

        # Red soil data
        for _ in range(10):
            soil_types.extend([2] * 6)
            temperatures.extend([26, 24, 27, 25, 28, 23])
            humidities.extend([65, 70, 68, 72, 67, 69])
            rainfalls.extend([150, 160, 155, 165, 158, 162])
            phs.extend([6.0, 6.2, 6.1, 6.3, 6.2, 6.1])
            crops.extend(['wheat', 'rice', 'millets', 'gram', 'pulses', 'cotton'])

        # Black soil data
        for _ in range(10):
            soil_types.extend([3] * 3)
            temperatures.extend([27, 26, 28])
            humidities.extend([75, 73, 74])
            rainfalls.extend([170, 175, 172])
            phs.extend([7.2, 7.0, 7.1])
            crops.extend(['sugarcane', 'wheat', 'groundnut'])

        # Mountain soil data
        for _ in range(10):
            soil_types.extend([4] * 7)
            temperatures.extend([20, 22, 21, 19, 23, 18, 20])
            humidities.extend([80, 82, 81, 83, 79, 81, 80])
            rainfalls.extend([250, 245, 255, 248, 252, 247, 251])
            phs.extend([5.8, 6.0, 5.9, 5.7, 6.1, 5.8, 5.9])
            crops.extend(['wheat', 'maize', 'barley', 'tea', 'coffee', 'spices', 'tropical fruits'])

        # Laterite soil data
        for _ in range(10):
            soil_types.extend([5] * 9)
            temperatures.extend([28, 27, 29, 26, 28, 27, 29, 26, 28])
            humidities.extend([85, 83, 84, 82, 85, 83, 84, 82, 85])
            rainfalls.extend([300, 295, 305, 298, 302, 297, 303, 296, 301])
            phs.extend([5.5, 5.6, 5.4, 5.7, 5.5, 5.6, 5.4, 5.7, 5.5])
            crops.extend(['tea', 'coffee', 'coconut', 'areca nut', 'banana', 'vegetables', 'tapioca', 'pineapple', 'pepper'])

        # Desert soil data
        for _ in range(10):
            soil_types.extend([6] * 6)
            temperatures.extend([35, 34, 36, 33, 35, 34])
            humidities.extend([30, 32, 31, 33, 30, 32])
            rainfalls.extend([50, 55, 48, 52, 51, 53])
            phs.extend([8.0, 7.8, 8.1, 7.9, 8.0, 7.8])
            crops.extend(['barley', 'rape', 'cotton', 'millets', 'maize', 'pulses'])

        self.training_data = {
            'soil_type': soil_types,
            'temperature': temperatures,
            'humidity': humidities,
            'rainfall': rainfalls,
            'ph': phs,
            'crop': crops
        }
        
        self.soil_crop_mapping = {
            1: {  # Alluvial Soil
                'name': "Alluvial Soil",
                'crops': ["rice", "wheat", "sugarcane", "jute", "oilseeds", "pulses"]
            },
            2: {  # Red Soil
                'name': "Red Soil",
                'crops': ["wheat", "rice", "millets", "gram", "pulses", "cotton"]
            },
            3: {  # Black Soil
                'name': "Black Soil",
                'crops': ["sugarcane", "wheat", "groundnut"]
            },
            4: {  # Mountain Soil
                'name': "Mountain Soil",
                'crops': ["wheat", "maize", "barley", "tea", "coffee", "spices", "tropical fruits"]
            },
            5: {  # Laterite Soil
                'name': "Laterite Soil",
                'crops': ["tea", "coffee", "coconut", "areca nut", "banana", "vegetables", "tapioca", "pineapple", "pepper"]
            },
            6: {  # Desert Soil
                'name': "Desert Soil",
                'crops': ["barley", "rape", "cotton", "millets", "maize", "pulses"]
            }
        }
        
        self.rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        self._train_model()
    
    def _train_model(self):
        df = pd.DataFrame(self.training_data)
        X = df[['soil_type', 'temperature', 'humidity', 'rainfall', 'ph']]
        y = df['crop']
        self.rf_model.fit(X, y)

    def predict_from_parameters(self, soil_type, temperature, humidity, rainfall, ph):
        # Get the soil-specific crops
        soil_info = self.soil_crop_mapping.get(soil_type, {
            'name': "Unknown Soil Type",
            'crops': []
        })
        
        # Create feature array for prediction
        features = np.array([[soil_type, temperature, humidity, rainfall, ph]])
        
        # Get model prediction
        model_prediction = self.rf_model.predict(features)[0]
        
        # Get suitable crops for this soil type
        suitable_crops = soil_info['crops']
        
        return {
            'recommended_crop': model_prediction,
            'suitable_crops': suitable_crops,
            'soil_name': soil_info['name']
        }

    def get_soil_type_description(self, soil_type):
        return self.soil_crop_mapping.get(soil_type, {
            'name': "Unknown Soil Type",
            'crops': []
        })

# Example usage:
def main():
    recommender = CropRecommendationSystem()
    
    # Make predictions
    prediction = recommender.predict_from_parameters(
        soil_type=1,
        temperature=26,
        humidity=75,
        rainfall=180,
        ph=6.7
    )
    print(f"Recommended crop: {prediction['recommended_crop']}")
    print(f"Suitable crops: {', '.join(prediction['suitable_crops'])}")
    print(f"Soil type: {prediction['soil_name']}")

if __name__ == "__main__":
    main()
