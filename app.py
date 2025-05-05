import streamlit as st
import openrouteservice
import warnings

warnings.filterwarnings("ignore")

# --- Streamlit page config ---
st.set_page_config(page_title='Car Carbon Emission Calculator 🚗', page_icon="📊", layout="wide")

st.title("Car Carbon Emission Calculator")
st.markdown("""
    <style>
    div.block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.subheader("Entrez les informations de votre trajet")

# --- Emission factors (kg CO2 per km) ---
emission_factor = {
    "voiture essence": 0.22,
    "voiture diesel": 0.20,
    "voiture hybride": 0.14,
    "voiture électrique": 0.10
}

# --- ORS Client ---
ORS_API_KEY = "YOUR_ORS_API_KEY_HERE"  # Replace with your ORS API Key
client = openrouteservice.Client(key=ORS_API_KEY)

# --- User Form ---
with st.form("carbon_form"):
    origin = st.text_input("Adresse de départ", placeholder="Ex: Paris, France")
    destination = st.text_input("Adresse d'arrivée", placeholder="Ex: Lyon, France")

    vehicle_type = st.selectbox("Type de véhicule", list(emission_factor.keys()))
    fallback_distance = st.slider("Distance journalière estimée (km, si aucun itinéraire)", 0.0, 100.0, 10.0)

    submit = st.form_submit_button("Calculer l'empreinte carbone")

# --- Distance and CO2 Calculation ---
if submit:
    if origin and destination:
        try:
            # Geocode the addresses
            geocode_origin = client.pelias_search(text=origin)
            geocode_destination = client.pelias_search(text=destination)

            coords = [
                [geocode_origin['features'][0]['geometry']['coordinates'][0],
                 geocode_origin['features'][0]['geometry']['coordinates'][1]],
                [geocode_destination['features'][0]['geometry']['coordinates'][0],
                 geocode_destination['features'][0]['geometry']['coordinates'][1]]
            ]

            # Get route
            route = client.directions(coords, profile='driving-car', format='geojson')
            distance_meters = route['features'][0]['properties']['summary']['distance']
            distance_km = distance_meters / 1000

            st.success(f"Distance réelle entre **{origin}** et **{destination}** : **{distance_km:.2f} km**")

        except Exception as e:
            st.error(f"Erreur lors de la récupération de la distance : {e}")
            distance_km = fallback_distance
            st.info(f"Utilisation de la distance estimée : **{distance_km:.2f} km**")

    else:
        st.warning("Adresses manquantes. Utilisation de la distance journalière estimée.")
        distance_km = fallback_distance

    # Calculate annual distance & emissions
    annual_distance = distance_km * 365
    factor = emission_factor[vehicle_type]
    annual_emissions = annual_distance * factor

    st.write(f"- 🚘 Type de véhicule : **{vehicle_type}**")
    st.write(f"- 📅 Distance annuelle : **{annual_distance:.2f} km**")
    st.write(f"- ♻️ Émissions CO₂ estimées : **{annual_emissions:.2f} kg/an**")
    

