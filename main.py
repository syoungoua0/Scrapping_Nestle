from scraper import bing_search
from downloader import download_pdf

entreprise = "Nestlé"
année = "2022"
site = "nestle.com"

query = f"{entreprise} annual report {année} site:{site} filetype:pdf"
resultats = bing_search(query)

if resultats:
    pdf_url = resultats[0]  # On prend le premier résultat
    fichier_pdf = download_pdf(pdf_url)
else:
    print("Aucun lien PDF trouvé.")

