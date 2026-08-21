import math

from flask import Blueprint, render_template, request

from models import Operacao

calculadora_bp = Blueprint("calculadora", __name__)


@calculadora_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return _calcular()
    return render_template(
        "calculadora.html",
        etapas="",
        resultados="",
        historico=Operacao.listar_recentes(),
    )


def _calcular():
    """Controller — lê o formulário, calcula e pede ao Model para salvar."""
    valor1 = float(request.form["num1"])
    acao = request.form["operacao"]
    valor2 = None
    etapas = ""
    resultado = ""

    if acao == "sqrt":
        if valor1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {valor1}."
        else:
            resultado = math.sqrt(valor1)
            etapas = f"√{valor1} = {resultado}"
    else:
        segundo_valor = request.form.get("num2", "").strip()
        if not segundo_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
                historico=Operacao.listar_recentes(),
            )
        valor2 = float(segundo_valor)

        if acao == "+":
            resultado = valor1 + valor2
            etapas = f"{valor1} + {valor2} = {resultado}"
        elif acao == "-":
            resultado = valor1 - valor2
            etapas = f"{valor1} - {valor2} = {resultado}"
        elif acao == "*":
            resultado = valor1 * valor2
            etapas = f"{valor1} * {valor2} = {resultado}"
        elif acao == "/":
            if valor2 != 0:
                resultado = valor1 / valor2
                etapas = f"{valor1} / {valor2} = {resultado}"
            else:
                resultado = "Erro: Divisão por zero"
                etapas = "Não é possível dividir por zero."
        elif acao == "**":
            resultado = valor1 ** valor2
            etapas = f"{valor1} ** {valor2} = {resultado}"
        else:
            resultado = "Operação inválida"
            etapas = "A operação selecionada é inválida."

    Operacao.salvar(valor1, valor2, acao, etapas, resultado)

    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=resultado,
        historico=Operacao.listar_recentes(),
    )