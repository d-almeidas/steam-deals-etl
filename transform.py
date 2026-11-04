import logging 
from datetime import date, datetime
from decimal import Decimal
from extract import extrair_todas

logger = logging.getLogger(__name__)

def converter_valor(valor):
    if valor is None:
        return None
    return Decimal(valor) / 100

def transformar(dados):
    resultado = []
    hoje = date.today()

    for itens in dados:
        original_num = converter_valor(itens.get("original_price"))
        final_num = converter_valor(itens.get("final_price"))

        if final_num < 0 or (original_num is not None and final_num > original_num):
            logger.warning("O valor %s não pode ser maior que seu valor original",final_num)
            continue

        timestamp = itens.get("expiration")
        expira = datetime.fromtimestamp(timestamp) if timestamp is not None else None

        resultado.append({
            "appid": itens["appid"],
            "name": itens["name"],
            "original_price": original_num,
            "final_price": final_num,
            "discount_percent": itens["discount_percent"],
            "expiration": expira,
            "collection_date": hoje
        })

    return resultado
