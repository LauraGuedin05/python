from flask import Blueprint, jsonify, request

from models import Cadastro, db
from services import buscar_cep

api_cadastros_bp = Blueprint("api_cadastros", __name__, url_prefix="/api")


@api_cadastros_bp.route("/cadastros", methods=["GET"])
def listar():
    return jsonify([item.para_dict() for item in Cadastro.listar()])


@api_cadastros_bp.route("/cadastros/<int:cadastro_id>", methods=["GET"])
def detalhe(cadastro_id):
    cadastro = db.session.get(Cadastro, cadastro_id)
    if not cadastro:
        return jsonify({"erro": "Cadastro não encontrado"}), 404
    return jsonify(cadastro.para_dict())


def _completar_endereco_pelo_cep(payload):
    """Preenche logradouro/bairro/cidade/estado via Brasil API quando o CEP vier no JSON."""
    cep = payload.get("cep")
    if not cep:
        return payload

    try:
        dados_endereco = buscar_cep(cep)
    except ValueError as exc:
        raise ValueError(str(exc)) from exc
    except Exception as exc:
        raise ValueError(f"CEP '{cep}' não encontrado") from exc

    resultado = dict(payload)
    for chave in ("cep", "logradouro", "bairro", "cidade", "estado"):
        if not resultado.get(chave):
            resultado[chave] = dados_endereco.get(chave, "")
    return resultado


@api_cadastros_bp.route("/cadastros", methods=["POST"])
def criar():
    payload = request.get_json()
    if not payload:
        return jsonify({"erro": "Envie JSON no body (Content-Type: application/json)"}), 400

    try:
        payload = _completar_endereco_pelo_cep(payload)
        cadastro = Cadastro.a_partir_de_dict(payload)
    except ValueError as exc:
        return jsonify({"erro": str(exc)}), 400

    if not cadastro.nome or not cadastro.profissao:
        return jsonify({"erro": "Nome e profissão não podem ser vazios"}), 400

    db.session.add(cadastro)
    db.session.commit()
    return jsonify(cadastro.para_dict()), 201


@api_cadastros_bp.route("/cadastros/<int:cadastro_id>", methods=["PUT"])
def atualizar(cadastro_id):
    cadastro = db.session.get(Cadastro, cadastro_id)
    if not cadastro:
        return jsonify({"erro": "Cadastro não encontrado"}), 404

    payload = request.get_json()
    if not payload:
        return jsonify({"erro": "Envie JSON no body"}), 400

    cadastro.atualizar_de_dict(payload)
    db.session.commit()
    return jsonify(cadastro.para_dict())


@api_cadastros_bp.route("/cadastros/<int:cadastro_id>", methods=["DELETE"])
def excluir(cadastro_id):
    cadastro = db.session.get(Cadastro, cadastro_id)
    if not cadastro:
        return jsonify({"erro": "Cadastro não encontrado"}), 404

    db.session.delete(cadastro)
    db.session.commit()
    return "", 204


@api_cadastros_bp.route("/cep/<cep>", methods=["GET"])
def consultar_cep(cep):
    try:
        endereco = buscar_cep(cep)
        return jsonify(endereco)
    except ValueError as exc:
        return jsonify({"erro": str(exc)}), 400
    except Exception:
        return jsonify({"erro": f"CEP '{cep}' não encontrado"}), 404
