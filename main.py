from scraper import bing_search
from downloader import download_pdf
from extractor import extract_financial_data

entreprise = "Nestlé"
année = "2022"
site = "nestle.com"

query = f"{entreprise} annual report {année} site:{site} filetype:pdf"
resultats = bing_search(query)

if resultats:
    pdf_url = resultats[0]
    fichier_pdf = download_pdf(pdf_url)
    
    if fichier_pdf:
        donnees = extract_financial_data(fichier_pdf)
        print("\n📊 Données extraites :")
        for k, v in donnees.items():
            print(f"{k} : {v}")
else:
    print("Aucun lien PDF trouvé.")
