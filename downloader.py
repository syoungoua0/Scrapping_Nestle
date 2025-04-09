import requests
import os

def download_pdfs(links, download_dir="downloads"):
    os.makedirs(download_dir, exist_ok=True)
    downloaded_files = []

    for i, url in enumerate(links):
        try:
            response = requests.get(url, timeout=15)
            if response.ok and 'application/pdf' in response.headers.get('Content-Type', ''):
                filename = os.path.join(download_dir, f"report_{i + 1}.pdf")
                with open(filename, "wb") as f:
                    f.write(response.content)
                downloaded_files.append(filename)
        except Exception as e:
            print(f"Erreur lors du téléchargement de {url} : {e}")

    return downloaded_files
