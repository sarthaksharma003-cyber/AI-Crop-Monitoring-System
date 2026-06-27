import streamlit as st
from streamlit_folium import st_folium

from utils.map_utils import create_base_map
from utils.api import get_ndvi
from utils.weather_api import get_weather

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Crop Monitoring System",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 AI Crop Monitoring Dashboard")

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "tile_url" not in st.session_state:
    st.session_state.tile_url = None

if "weather" not in st.session_state:
    st.session_state.weather = None

# --------------------------------------------------
# Coordinate Inputs
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    latitude = st.number_input(
        "📍 Latitude",
        value=28.6139,
        format="%.6f"
    )

with col2:
    longitude = st.number_input(
        "📍 Longitude",
        value=77.2090,
        format="%.6f"
    )

# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button("🌱 Analyze Field", use_container_width=True):

    with st.spinner("Analyzing field..."):

        try:
            ndvi_result = get_ndvi(latitude, longitude)

            st.session_state.tile_url = ndvi_result["tile_fetcher"]

            weather_result = get_weather(latitude, longitude)

            st.session_state.weather = weather_result

            st.success("Analysis Completed Successfully!")

        except Exception as e:
            st.error(f"Error: {e}")

# --------------------------------------------------
# Weather Section
# --------------------------------------------------

st.divider()

st.subheader("🌦 Current Weather")

if st.session_state.weather:

    current = st.session_state.weather["current"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🌡 Temperature",
            f'{current["temperature_2m"]} °C'
        )

    with c2:
        st.metric(
            "💧 Humidity",
            f'{current["relative_humidity_2m"]}%'
        )

    with c3:
        st.metric(
            "🌧 Rain",
            f'{current["rain"]} mm'
        )

    with c4:
        st.metric(
            "💨 Wind",
            f'{current["wind_speed_10m"]} km/h'
        )

else:

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🌡 Temperature", "--")

    with c2:
        st.metric("💧 Humidity", "--")

    with c3:
        st.metric("🌧 Rain", "--")

    with c4:
        st.metric("💨 Wind", "--")

# --------------------------------------------------
# Map Section
# --------------------------------------------------

st.divider()

st.subheader("🛰 NDVI Map")

farm_map = create_base_map(
    latitude,
    longitude,
    st.session_state.tile_url
)

st_folium(
    farm_map,
    width=1200,
    height=650
)