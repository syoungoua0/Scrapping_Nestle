import os
import requests
import streamlit as st
from bing_scraper import bing_search
from pathlib import Path

# Importer la fonction d'extraction de texte depuis le fichier pdf_extractor.py
from pdf_extractor import extract_text_from_pdf

# Créer un répertoire de téléchargement si nécessaire
download_dir = "downloads"
Path(download_dir).mkdir(parents=True, exist_ok=True)

st.title("🔍 Scraper Bing PDF & rapports annuels")

query = st.text_input("Entrez une requête de recherche", value="Nike annual report 2023")

if st.button("Lancer la recherche"):
    with st.spinner("Recherche en cours..."):
        # Lancer la recherche Bing pour récupérer les liens
        resultats = bing_search(query)
        
        # Afficher les liens trouvés
        for lien in resultats:
            st.write("🔗", lien)
        
        # Télécharger les fichiers PDF trouvés et extraire le texte
        for lien in resultats:
            if "pdf" in lien.lower():
                # Télécharger le fichier PDF
                pdf_path = os.path.join(download_dir, lien.split("/")[-1])
                response = requests.get(lien, stream=True)
                
                if response.status_code == 200:
                    with open(pdf_path, "wb") as f:
                        for chunk in response.iter_content(1024):
                            f.write(chunk)
                    
                    st.write(f"Fichier PDF téléchargé : {pdf_path}")
                    
                    # Extraire le texte du fichier PDF téléchargé
                    extracted_text = extract_text_from_pdf(pdf_path)
                    st.write("Texte extrait du PDF :")
                    st.text_area("Contenu du PDF", extracted_text, height=300)
                else:
                    st.write(f"Erreur lors du téléchargement du PDF à {lien}")
