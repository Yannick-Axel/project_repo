import streamlit as st 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

import warnings 
warnings.filterwarnings("ignore")

st.set_page_config(page_title='Titanic !!!' , page_icon="bar_chart:", layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title ("Car Carbon Emission Calculator")
st.markdown("""
    <style>
    div.block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)
# Formulaire utilisateur
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
        # Ici tu ajouteras l'appel à Google Maps API pour la distance
        # Puis l'appel à Carbon Interface API pour les émissions CO₂
    else:
        st.error("Veuillez remplir les deux adresses.")import streamlit as st 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

import warnings 
warnings.filterwarnings("ignore")

st.set_page_config(page_title='Titanic !!!' , page_icon="bar_chart:", layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title ("Car Carbon Emission Calculator")
st.markdown("""
    <style>
    div.block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)
# Formulaire utilisateur
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
        # Ici tu ajouteras l'appel à Google Maps API pour la distance
        # Puis l'appel à Carbon Interface API pour les émissions CO₂
    else:
        st.error("Veuillez remplir les deux adresses.") 