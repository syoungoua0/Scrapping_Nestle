import os
import requests

def download_pdf(url, output_folder="data"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    local_filename = os.path.join(output_folder, url.split("/")[-1].split("?")[0])

    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"✅ Téléchargé : {local_filename}")
        return local_filename
    except Exception as e:
        print(f"❌ Erreur lors du téléchargement : {e}")
        return None
