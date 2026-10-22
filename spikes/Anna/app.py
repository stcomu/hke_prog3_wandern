import pandas as pd
import streamlit as st
from daten import Tourdaten
from funktionen import filter_schwierigkeit, filter_distanz, filter_hoehenmeter, filter_dauer

Passende_touren = []

st.title("Wandertouren Filter")

Schwirigkeit = st.selectbox("Schwierigkeit auswählen", ["leicht", "mittel", "schwer"])
min_distanz = st.number_input("Minimale Distanz (km)", min_value=0, step=1)
max_distanz = st.number_input("Maximale Distanz (km)", min_value=min_distanz, step=1)
min_hoehenmeter = st.number_input("Minimale Höhenmeter (m)", min_value=0, step=10)
max_hoehenmeter = st.number_input("Maximale Höhenmeter (m)", min_value=min_hoehenmeter, step=10)
min_dauer = st.number_input("Minimale Dauer (h)", min_value=0.0, step=0.5)
max_dauer = st.number_input("Maximale Dauer (h)", min_value=min_dauer, step=0.5)


if st.button("Touren filtern"):
    Passende_touren = filter_schwierigkeit(
        Tourdaten, Schwirigkeit
    )
    Passende_touren = filter_distanz(
        Passende_touren, min_distanz, max_distanz
    )
    Passende_touren = filter_hoehenmeter(
        Passende_touren, min_hoehenmeter, max_hoehenmeter
    )
    Passende_touren = filter_dauer(
        Passende_touren, min_dauer, max_dauer
    )

Tour = st.table (Passende_touren)

