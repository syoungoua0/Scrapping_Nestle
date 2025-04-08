from scraper import bing_search

entreprise = "Nestlé"
année = "2022"
site = "nestle.com"

query = f"{entreprise} annual report {année} site:{site} filetype:pdf"
resultats = bing_search(query)

print("Résultats trouvés :")
for url in resultats:
    print(url)

