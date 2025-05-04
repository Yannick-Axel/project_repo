import streamlit as st
import pandas as pd
import warnings 

warnings.filterwarnings("ignore")

st.set_page_config(page_title='Titanic !!!', page_icon="📊", layout="wide")

st.title("Car Carbon Emission Calculator")
st.markdown("""
    <style>
    div.block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.subheader("Entrez les informations de votre trajet")

with st.form("carbon_form"):
    origin = st.text_input("Adresse de départ", placeholder="Ex: Paris, France")
    destination = st.text_input("Adresse d'arrivée", placeholder="Ex: Lyon, France")

    vehicle_type = st.selectbox("Type de véhicule", [
        "Voiture essence",
        "Voiture diesel",
        "Voiture hybride",
        "Voiture électrique"
    ])

    submit = st.form_submit_button("Calculer l'empreinte carbone")

if submit:
    if origin and destination:
        st.success(f"Calcul en cours pour un trajet de **{origin}** à **{destination}** avec un véhicule **{vehicle_type}**...")
    else:
        st.error("Veuillez remplir les deux adresses.")

emission_factor = {
    "Switzerland": {
        "voiture essence": 0.22,
        "voiture diesel": 0.20,
        "voiture hybride": 0.14,
        "voiture électrique": 0.10
    }
}

col1, col2, col3, col4 = st.columns(4)


with col1:
    distance_essence = st.slider("Distance (Essence)", 0.0, 100.0, key="distance_essence")
with col2:
    distance_diesel = st.slider("Distance (Diesel)", 0.0, 100.0, key="distance_diesel")
with col3:
    distance_hybrid = st.slider("Distance (Hybride)", 0.0, 100.0, key="distance_hybrid")
with col4:
    distance_electric = st.slider("Distance (Électrique)", 0.0, 100.0, key="distance_electric")

if distance_essence > 0:
    annual_essence = distance_essence * 365
