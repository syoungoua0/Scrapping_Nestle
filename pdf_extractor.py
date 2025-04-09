# pdf_extractor.py
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extrait le texte d'un fichier PDF.
    :param pdf_path: Le chemin du fichier PDF
    :return: Le texte extrait du PDF
    """
    try:
        # Ouvrir le fichier PDF
        document = fitz.open(pdf_path)
        text = ""
        
        # Parcourir chaque page du PDF et extraire le texte
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text += page.get_text()
        
        return text
    
    except Exception as e:
        return f"Erreur lors de l'extraction du texte : {e}"
