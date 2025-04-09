import streamlit as st
from bing_scraper import bing_search

st.title("🔍 Scraper Bing PDF & rapports annuels")

query = st.text_input("Entrez une requête de recherche", value="Nike annual report 2023")

if st.button("Lancer la recherche"):
    with st.spinner("Recherche en cours..."):
        resultats = bing_search(query)
        for lien in resultats:
            st.write("🔗", lien)
