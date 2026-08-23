"""
Script de diagnóstico: roda cada etapa do pipeline isoladamente
e imprime o que está a acontecer, para descobrir onde a busca
de vagas está a falhar.
"""
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}


def debug_fetch(keywords=os.getenv("KEYWORDS"), location="Portugal", start=0):
    session = requests.Session()
    session.headers.update(HEADERS)

    params = {"keywords": keywords, "location": location, "start": start}

    print(f"→ GET {BASE_URL}")
    print(f"  params: {params}")

    res = session.get(BASE_URL, params=params, timeout=10)

    print(f"← status: {res.status_code}")
    print(f"← tamanho da resposta: {len(res.text)} caracteres")
    print(f"← primeiros 500 chars:\n{res.text[:500]}\n")

    if res.status_code != 200:
        print("!!! Status não é 200  provavelmente bloqueado ou parâmetros errados.")
        return

    if len(res.text.strip()) == 0:
        print("!!! Resposta vazia  LinkedIn provavelmente bloqueou (sem User-Agent válido, rate limit, ou geoId errado).")
        return

    soup = BeautifulSoup(res.text, "html.parser")
    cards = soup.select(".base-card")
    print(f"← número de '.base-card' encontrados: {len(cards)}")

    if len(cards) == 0:
        print("!!! HTML retornado, mas nenhum '.base-card' os selectors do LinkedIn provavelmente mudaram.")
        print("    Tenta abrir a URL manualmente num browser (com esses params) e inspecionar o HTML atual.")
        return

    # mostra o primeiro card em detalhe
    card = cards[0]
    print("\n--- Primeiro card encontrado ---")
    print(f"title selector (.base-search-card__title): {card.select_one('.base-search-card__title')}")
    print(f"company selector (.base-search-card__subtitle): {card.select_one('.base-search-card__subtitle')}")
    print(f"location selector (.job-search-card__location): {card.select_one('.job-search-card__location')}")
    print(f"link selector (a): {card.select_one('a')}")


if __name__ == "__main__":
    debug_fetch()