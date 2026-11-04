import psycopg
import logging
from dotenv import load_dotenv
import os

logger = logging.getLogger(__name__)

def conectar():
    load_dotenv()
    conn = psycopg.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
    )
    return conn

def carregar_dados(dados):
    inseridas = 0
    with conectar() as conn:
        with conn.cursor() as cur:
            for itens in dados:
                cur.execute(
                    """
                    INSERT INTO games (appid,name)
                    VALUES (%s,%s)
                    ON CONFLICT (appid) DO UPDATE SET name = EXCLUDED.name
                    """,
                    (itens["appid"], itens["name"]),
                )
                cur.execute(
                    """INSERT INTO promotions (appid, collection_date, original_price, final_price, discount_percent, expiration)
                    VALUES (%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (appid, collection_date) DO NOTHING
                    """,
                    (itens["appid"], itens["collection_date"], itens["original_price"], itens["final_price"], itens["discount_percent"], itens["expiration"]) 
                )
                inseridas += cur.rowcount
        logger.info("Insereidas %s linhas, ignoradas %s (ja existem)", inseridas, len(dados)-inseridas)
        return inseridas

