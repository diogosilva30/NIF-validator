import requests
from bs4 import BeautifulSoup


def validate(NIF: str) -> bool:
    response = requests.get(f"https://www.nif.pt/?q={NIF}")
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    # Search for entity NIF
    entity = soup.find("span", class_="search-title")

    if entity is not None:
        return True
    message = soup.select('div[class*="alert-message"]')[0].text

    return True if "O NIF indicado é válido" in message else False
