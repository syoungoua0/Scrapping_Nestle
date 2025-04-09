import requests
from bs4 import BeautifulSoup

def bing_search(query, max_results=5):
    base_url = "https://www.bing.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(base_url, headers=headers, params={"q": query}, timeout=10)

        if response.status_code != 200:
            return [f"Erreur HTTP {response.status_code}"]

        soup = BeautifulSoup(response.text, "html.parser")
        links = []

        for a in soup.select("li.b_algo h2 a"):
            href = a.get("href")
            if href and ("pdf" in href.lower() or "annual-report" in href.lower()):
                links.append(href)
            if len(links) >= max_results:
                break

        return links or ["Aucun lien trouvé"]
    
    except Exception as e:
        return [f"Erreur pendant la requête : {e}"]
