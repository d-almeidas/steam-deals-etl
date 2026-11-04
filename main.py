from extract import extrair_todas
from transform import transformar
from load import carregar_dados
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

def main():
    infos = extrair_todas()
    logger.info("Total de registros extraidos: %s", len(infos))
    if not infos:
        raise RuntimeError("Nenhum registro extraido da API.")

    dados_transformados = transformar(infos)
    logger.info("Total de registros transformados: %s (total descartados %s)",
    len(dados_transformados), len(infos) - len(dados_transformados))

    total = carregar_dados(dados_transformados)
    logger.info("Total gravado no banco: %s (ja existiam %s)", total, len(infos) - total)

if __name__ == "__main__":
    main()