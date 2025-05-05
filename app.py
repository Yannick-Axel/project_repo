import streamlit as st
import openrouteservice
import warnings

warnings.filterwarnings("ignore")

# Streamlit config
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

# Emission factors (kg CO2 per km)
emission_factor = {
    "Switzerland": {
        "voiture essence": 0.22,
        "voiture diesel": 0.20,
        "voiture hybride": 0.14,
        "voiture électrique": 0.10
    }
}

# Init ORS client
ORS_API_KEY = st.secrets["api_keys"]["5b3ce3597851110001cf62486a23cf7eabd24469afeccff7a53a5b18"]
client = openrouteservice.Client(key=ORS_API_KEY)

# Form
with st.form("carbon_form"):
    origin = st.text_input("Adresse de départ", placeholder="Ex: Paris, France")
    destination = st.text_input("Adresse d'arrivée", placeholder="Ex: Lyon, France")

    vehicle_type = st.selectbox("Type de véhicule", [
        "voiture essence",
        "voiture diesel",
        "voiture hybride",
        "voiture électrique"
    ])

    submit = st.form_submit_button("Calculer l'empreinte carbone")

# On submit
if submit:
    if origin and destination:
        try:
            # Géocodage
            geo_origin = client.pelias_search(text=origin)
            geo_dest = client.pelias_search(text=destination)

            coords = [
                geo_origin['features'][0]['geometry']['coordinates'],
                geo_dest['features'][0]['geometry']['coordinates']
            ]

            # Récupération de la distance
            route = client.directions(coords, profile='driving-car', format='geojson')
            distance_km = route['features'][0]['properties']['summary']['distance'] / 1000

            factor = emission_factor["Switzerland"].get(vehicle_type, 0)
            co2 = distance_km * factor

            st.success(f"Trajet de **{origin}** à **{destination}** avec un véhicule **{vehicle_type}**")
            st.write(f"- 🚗 Distance réelle : **{distance_km:.2f} km**")
            st.write(f"- ♻️ Émissions estimées : **{co2:.2f} kg CO₂**")
        except Exception as e:
            st.error(f"Erreur OpenRouteService : {e}")
    else:
        st.error("Veuillez remplir les deux adresses.")

# Estimations journalières
st.subheader("🧮 Estimation journalière des émissions en fonction du type de véhicule")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**Essence**")
    distance_essence = st.slider("Distance journalière (km)", 0.0, 100.0, key="distance_essence")
    if distance_essence > 0:
        annual = distance_essence * 365
        co2 = annual * emission_factor["Switzerland"]["voiture essence"]
        st.write(f"Émission annuelle : **{co2:.2f} kg CO₂**")

with col2:
    st.markdown("**Diesel**")
    distance_diesel = st.slider("Distance journalière (km)", 0.0, 100.0, key="distance_diesel")
    if distance_diesel > 0:
        annual = distance_diesel * 365
        co2 = annual * emission_factor["Switzerland"]["voiture diesel"]
        st.write(f"Émission annuelle : **{co2:.2f} kg CO₂**")

with col3:
    st.markdown("**Hybride**")
    distance_hybrid = st.slider("Distance journalière (km)", 0.0, 100.0, key="distance_hybrid")
    if distance_hybrid > 0:
        annual = distance_hybrid * 365
        co2 = annual * emission_factor["Switzerland"]["voiture hybride"]
        st.write(f"Émission annuelle : **{co2:.2f} kg CO₂**")

with col4:
    st.markdown("**Électrique**")
    distance_electric = st.slider("Distance journalière (km)", 0.0, 100.0, key="distance_electric")
    if distance_electric > 0:
        annual = distance_electric * 365
        co2 = annual * emission_factor["Switzerland"]["voiture électrique"]
        st.write(f"Émission annuelle : **{co2:.2f} kg CO₂**")

