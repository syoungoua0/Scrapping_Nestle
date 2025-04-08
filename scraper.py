import requests
from bs4 import BeautifulSoup
import urllib.parse

def bing_search(query, max_results=5):
    base_url = "https://www.bing.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Encode la query
    params = {"q": query}
    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Erreur {response.status_code} lors de la requête.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for a in soup.select("li.b_algo h2 a"):
        href = a.get("href")
        if href and ("pdf" in href.lower() or "annual-report" in href.lower()):
            links.append(href)
        if len(links) >= max_results:
            break

    return links

