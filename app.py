import streamlit as st
import warnings

warnings.filterwarnings("ignore")

# Set up Streamlit page
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

# Form for user input
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
        st.success(f"Calcul en cours pour un trajet de **{origin}** à **{destination}** avec un véhicule **{vehicle_type}**...")
        factor = emission_factor["Switzerland"].get(vehicle_type, 0)
        st.write(f"Facteur d'émission utilisé : **{factor} kg CO₂/km**")
    else:
        st.error("Veuillez remplir les deux adresses.")

st.subheader("🧮 Estimation journalière des émissions en fonction du type de véhicule")

# Create columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**Essence**")
    distance_essence = st.slider("Distance journalière (km)", 0.0, 100.0, key="distance_essence")
    if distance_essence > 0:
        annual_essence = distance_essence * 365
        emission_essence = annual_essence * emission_factor["Switzerland"]["voiture essence"]
        st.write(f"Émission annuelle : **{emission_essence:.2f} kg CO₂**")

with col2:
    st.markdown("**Diesel**")
    distance_diesel = st.slider("Distance journalière (km)", 0.0, 100.0, key="distance_diesel")
    if distance_diesel > 0:
        annual_diesel = distance_diesel * 365
        emission_diesel = annual_diesel * emission_factor["Switzerland"]["voiture diesel"]
        st.write(f"Émission annuelle : **{emission_diesel:.2f} kg CO₂**")

with col3:
    st.markdown("**Hybride**")
    distance_hybrid = st.slider("Distance journalière (km)", 0.0, 100.0, key="distance_hybrid")
    if distance_hybrid > 0:
        annual_hybrid = distance_hybrid * 365
        emission_hybrid = annual_hybrid * emission_factor["Switzerland"]["voiture hybride"]
        st.write(f"Émission annuelle : **{emission_hybrid:.2f} kg CO₂**")

with col4:
    st.markdown("**Électrique**")
    distance_electric = st.slider("Distance journalière (km)", 0.0, 100.0, key="distance_electric")
    if distance_electric > 0:
        annual_electric = distance_electric * 365
        emission_electric = annual_electric * emission_factor["Switzerland"]["voiture électrique"]
        st.write(f"Émission annuelle : **{emission_electric:.2f} kg CO₂**")
