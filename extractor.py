import pdfplumber
import re

def extract_financial_data(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages[:5]:  # On limite aux premières pages
            text += page.extract_text() + "\n"

    # Recherche de patterns financiers simples
    results = {}

    revenue_match = re.search(r"(Revenue|Total revenue|Chiffre d’affaires)[^\d]*(\d[\d\s,.]+)", text, re.IGNORECASE)
    income_match = re.search(r"(Net income|Profit|Résultat net)[^\d]*(\d[\d\s,.]+)", text, re.IGNORECASE)
    employee_match = re.search(r"(Employees|Effectif|Effectifs)[^\d]*(\d[\d\s,.]+)", text, re.IGNORECASE)

    if revenue_match:
        results["Revenue"] = revenue_match.group(2).strip()
    if income_match:
        results["Net Income"] = income_match.group(2).strip()
    if employee_match:
        results["Employees"] = employee_match.group(2).strip()

    return results

