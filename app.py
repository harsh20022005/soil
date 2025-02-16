import streamlit as st
from soil1 import CropRecommendationSystem
import streamlit.components.v1 as components

# Basic page config
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add this at the top of app.py
translations = {
    'hi': {
        'crops': {
            'rice': 'चावल',
            'wheat': 'गेहूं',
            'sugarcane': 'गन्ना',
            'jute': 'जूट',
            'oilseeds': 'तिलहन',
            'pulses': 'दालें',
            'cotton': 'कपास',
            'millets': 'बाजरा',
            'gram': 'चना',
            'groundnut': 'मूंगफली',
            'maize': 'मक्का',
            'barley': 'जौ',
            'tea': 'चाय',
            'coffee': 'कॉफी',
            'spices': 'मसाले',
            'tropical fruits': 'उष्णकटिबंधीय फल',
            'coconut': 'नारियल',
            'areca nut': 'सुपारी',
            'banana': 'केला',
            'vegetables': 'सब्जियां',
            'tapioca': 'कसावा',
            'pineapple': 'अनानास',
            'pepper': 'काली मिर्च',
            'rape': 'सरसों'
        },
        'soils': {
            'Alluvial Soil': 'जलोढ़ मिट्टी',
            'Red Soil': 'लाल मिट्टी',
            'Black Soil': 'काली मिट्टी',
            'Mountain Soil': 'पर्वतीय मिट्टी',
            'Laterite Soil': 'लैटेराइट मिट्टी',
            'Desert Soil': 'रेगिस्तानी मिट्टी'
        }
    },
    'mr': {
        'crops': {
            'rice': 'तांदूळ',
            'wheat': 'गहू',
            'sugarcane': 'ऊस',
            'jute': 'ताग',
            'oilseeds': 'तेलबिया',
            'pulses': 'डाळी',
            'cotton': 'कापूस',
            'millets': 'ज्वारी',
            'gram': 'हरभरा',
            'groundnut': 'भुईमूग',
            'maize': 'मका',
            'barley': 'जव',
            'tea': 'चहा',
            'coffee': 'कॉफी',
            'spices': 'मसाले',
            'tropical fruits': 'उष्णकटिबंधीय फळे',
            'coconut': 'नारळ',
            'areca nut': 'सुपारी',
            'banana': 'केळी',
            'vegetables': 'भाज्या',
            'tapioca': 'कसावा',
            'pineapple': 'अननस',
            'pepper': 'मिरी',
            'rape': 'मोहरी'
        },
        'soils': {
            'Alluvial Soil': 'गाळाची माती',
            'Red Soil': 'तांबडी माती',
            'Black Soil': 'काळी माती',
            'Mountain Soil': 'डोंगराळ माती',
            'Laterite Soil': 'लॅटेराईट माती',
            'Desert Soil': 'वाळवंटी माती'
        }
    }
}

def main():
    # Updated CSS with specific h1 color
    st.markdown("""
        <style>
        .stApp {
            background-color: white;
        }
        
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        
        h1 {
            color: #4CAF50 !important;
            font-weight: bold;
        }
        
        h2, h3 {
            color: #2E7D32;
            font-weight: bold;
        }
        
        .stSelectbox label, .stSlider label {
            color: #2E7D32;
            font-weight: 600;
        }

        p {
            color: #1B5E20;
            font-weight: 500;
        }

        .stSuccess {
            color: #1B5E20;
            font-weight: bold;
        }

        .stSelectbox div[role="listbox"] div {
            color: #1B5E20;
        }
        </style>
    """, unsafe_allow_html=True)

    # Language selector in top right corner
    selected_language = st.selectbox(
        "",
        options=[
            "English",
            "मराठी (Marathi)",
            "हिंदी (Hindi)"
        ],
        index=0,
        key="language_selector"
    )

    # Convert display language to language code
    lang_code = {
        "English": "en",
        "मराठी (Marathi)": "mr",
        "हिंदी (Hindi)": "hi"
    }[selected_language]

    # Title and description based on selected language
    titles = {
        "en": "Crop Recommendation System",
        "mr": "पीक शिफारस प्रणाली",
        "hi": "फसल अनुशंसा प्रणाली"
    }
    
    descriptions = {
        "en": "Enter soil and environmental parameters to get crop recommendations",
        "mr": "पीक शिफारसी मिळवण्यासाठी मृदा आणि पर्यावरणीय मापदंड प्रविष्ट करा",
        "hi": "फसल की सिफारिशें प्राप्त करने के लिए मिट्टी और पर्यावरण मापदंड दर्ज करें"
    }

    st.title(titles[lang_code])
    st.write(descriptions[lang_code])

    # Input labels in different languages
    labels = {
        "en": {
            "soil_type": "Soil Type",
            "temperature": "Temperature (°C)",
            "humidity": "Humidity (%)",
            "rainfall": "Rainfall (mm)",
            "ph": "pH Level",
            "submit": "Get Recommendations",
            "soil_types": ["Alluvial Soil", "Red Soil", "Black Soil", "Mountain Soil", "Laterite Soil", "Desert Soil"]
        },
        "mr": {
            "soil_type": "मृदा प्रकार",
            "temperature": "तापमान (°C)",
            "humidity": "आर्द्रता (%)",
            "rainfall": "पर्जन्यमान (मिमी)",
            "ph": "सामू पातळी",
            "submit": "शिफारसी मिळवा",
            "soil_types": ["गाळाची मृदा", "तांबडी मृदा", "काळी मृदा", "डोंगराळ मृदा", "लॅटेराइट मृदा", "वाळवंटी मृदा"]
        },
        "hi": {
            "soil_type": "मिट्टी का प्रकार",
            "temperature": "तापमान (°C)",
            "humidity": "आर्द्रता (%)",
            "rainfall": "वर्षा (मिमी)",
            "ph": "पीएच स्तर",
            "submit": "सिफारिशें प्राप्त करें",
            "soil_types": ["जलोढ मिट्टी", "लाल मिट्टी", "काली मिट्टी", "पर्वतीय मिट्टी", "लैटेराइट मिट्टी", "मरुस्थलीय मिट्टी"]
        }
    }

    # Create form
    soil_type = st.selectbox(
        labels[lang_code]["soil_type"],
        options=range(1, 7),
        format_func=lambda x: labels[lang_code]["soil_types"][x-1]
    )
    
    temperature = st.slider(
        labels[lang_code]["temperature"],
        min_value=0,
        max_value=50,
        value=25
    )
    
    humidity = st.slider(
        labels[lang_code]["humidity"],
        min_value=0,
        max_value=100,
        value=70
    )
    
    rainfall = st.slider(
        labels[lang_code]["rainfall"],
        min_value=0,
        max_value=500,
        value=200
    )
    
    ph = st.slider(
        labels[lang_code]["ph"],
        min_value=0.0,
        max_value=14.0,
        value=7.0,
        step=0.1
    )

    if st.button(labels[lang_code]["submit"]):
        recommender = CropRecommendationSystem()
        prediction = recommender.predict_from_parameters(
            soil_type=soil_type,
            temperature=temperature,
            humidity=humidity,
            rainfall=rainfall,
            ph=ph
        )

        # Display results
        result_labels = {
            "en": {
                "soil_type": "Soil Type",
                "recommended": "Recommended Crop",
                "suitable": "Suitable Crops"
            },
            "mr": {
                "soil_type": "मृदा प्रकार",
                "recommended": "शिफारस केलेले पीक",
                "suitable": "योग्य पिके"
            },
            "hi": {
                "soil_type": "मिट्टी का प्रकार",
                "recommended": "अनुशंसित फसल",
                "suitable": "उपयुक्त फसलें"
            }
        }

        st.success(f"{result_labels[lang_code]['soil_type']}: {labels[lang_code]['soil_types'][soil_type-1]}")
        
        # Fix for recommended crop translation
        if lang_code == "en":
            st.success(f"{result_labels[lang_code]['recommended']}: {prediction['recommended_crop']}")
        else:
            # Translate the recommended crop
            translated_recommended = translations[lang_code]['crops'].get(prediction['recommended_crop'], prediction['recommended_crop'])
            st.success(f"{result_labels[lang_code]['recommended']}: {translated_recommended}")
        
        # Display suitable crops
        suitable_crops = prediction['suitable_crops']
        if lang_code == "en":
            st.success(f"{result_labels[lang_code]['suitable']}: {', '.join(suitable_crops)}")
        else:
            translated_crops = [translations[lang_code]['crops'].get(crop, crop) for crop in suitable_crops]
            st.success(f"{result_labels[lang_code]['suitable']}: {', '.join(translated_crops)}")

if __name__ == "__main__":
    main()