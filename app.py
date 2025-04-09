# app.py
import streamlit as st
from scraper.bing_scraper import bing_search

st.set_page_config(page_title="Scraper Bing PDF", page_icon="🔍")
st.title("🔍 Scraper Bing PDF & rapports annuels")

# Initialiser la session pour stocker les résultats
if "liens_scrapes" not in st.session_state:
    st.session_state.liens_scrapes = []

# Saisie de la requête
query = st.text_input("Entrez une requête de recherche", value="Nike annual report 2023")

# Bouton de lancement de recherche
if st.button("🔎 Lancer la recherche"):
    with st.spinner("Recherche en cours..."):
        resultats = bing_search(query)
        st.session_state.liens_scrapes = resultats
        st.success(f"{len(resultats)} lien(s) trouvé(s).")

# Bouton pour afficher les résultats précédents
if st.button("📄 Voir les résultats enregistrés"):
    st.subheader("🔗 Liens enregistrés")
    if st.session_state.liens_scrapes:
        for lien in st.session_state.liens_scrapes:
            st.write("🔗", lien)
    else:
        st.info("Aucun lien n'a encore été trouvé.")

# import streamlit as st
#from bing_scraper import bing_search

#st.title("🔍 Scraper Bing PDF & rapports annuels")

#query = st.text_input("Entrez une requête de recherche", value="Nike annual report 2023")

#if st.button("Lancer la recherche"):
#    with st.spinner("Recherche en cours..."):
#        resultats = bing_search(query)
#        for lien in resultats:
#            st.write("🔗", lien)
