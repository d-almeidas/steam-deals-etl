import os 
import requests
import psycopg
import logging
import time

logger = logging.getLogger(__name__)

url = "https://store.steampowered.com/api/featuredcategories/"

CATEGORIAS = {"specials", "top_sellers", "new_releases"}

def get_with_retry(url, tentativas = 3, espera = 2, **kwargs):
    for tentativa in range(1, tentativas + 1):
        try:
            req = requests.get(url, timeout=10, **kwargs)
            req.raise_for_status()
            return req

        except (requests.exceptions.Timeout,
                requests.exceptions.ConnectionError):
            logger.warning("Tentativa %s: falha de conexão.", tentativa)

        except requests.exceptions.HTTPError as e:
            if e.response.stuatus_code < 500:
                raise
            loger.waring("Tentativa %s: Error de servidor.", tentativa)

        if tentativa < tentativas:
            logger.info("Tentando de novo em %s segundos", espera)
            time.sleep(espera)

    Exception("A API nao respondeu depois de varais tentativas.")

def buscar_destaques():
    params = {"cc": "br", "l": "portuguese"}
    req = get_with_retry(url, params=params)
    return req.json()

def extrair_promocoes(dados):
    promocoes = {} 

    for categoria in CATEGORIAS:
        itens = dados.get(categoria, {}).get("items", [])

        for jogo in itens:
            if not jogo.get("discounted") or jogo.get("type") != 0:
                continue
            
            promocoes[jogo["id"]] = {
                "appid": jogo["id"],
                "name": jogo["name"],
                "original_price": jogo["original_price"],
                "final_price": jogo["final_price"],
                "discount_percent": jogo["discount_percent"],
                "expiration": jogo.get("discount_expiration")
            }      
            
    return list(promocoes.values())

def extrair_todas():
    destaques = buscar_destaques()
    promocoes = extrair_promocoes(destaques)
    logger.info("Extraida %s promocões", len(promocoes))
    return promocoes

