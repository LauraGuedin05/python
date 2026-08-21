import re

import requests

BASE = "https://brasilapi.com.br/api/cep/v2"


def _limpar_cep(valor_cep):
    return re.sub(r"\D", "", str(valor_cep))


def buscar_cep(codigo_postal):
    cep_digitos = _limpar_cep(codigo_postal)
    if len(cep_digitos) != 8:
        raise ValueError("CEP deve ter 8 dígitos")

    endereco_url = f"{BASE}/{cep_digitos}"
    resposta = requests.get(endereco_url, timeout=10)
    resposta.raise_for_status()
    conteudo = resposta.json()

    return {
        "cep": conteudo.get("cep", cep_digitos),
        "logradouro": conteudo.get("street", ""),
        "bairro": conteudo.get("neighborhood", ""),
        "cidade": conteudo.get("city", ""),
        "estado": conteudo.get("state", ""),
        "fonte": "Brasil API",
    }
