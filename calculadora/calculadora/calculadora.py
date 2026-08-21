import math
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return calcular()
    return render_template("calculadora.html", etapas=None, resultados=None)


def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro"
            etapas = f"Erro: Não existe raiz quadrada real de número negativo ({num1})."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

    elif operacao == "baskara":
        valor_b = request.form.get("num2", "").strip()
        valor_c = request.form.get("num3", "").strip()

        if not valor_b or not valor_c:
            return render_template(
                "calculadora.html",
                etapas="Erro: Informe os coeficientes B e C para Bhaskara.",
                resultados="",
            )

        coef_a = num1
        coef_b = float(valor_b)
        coef_c = float(valor_c)

        if coef_a == 0:
            resultado = "Erro"
            etapas = "Erro: O coeficiente 'A' não pode ser zero em uma equação de 2º grau."
        else:
            discriminante = (coef_b**2) - (4 * coef_a * coef_c)
            if discriminante < 0:
                resultado = "Sem raízes reais"
                etapas = f"Δ = {coef_b}² - 4·({coef_a})·({coef_c}) = {discriminante} (Delta negativo)"
            else:
                raiz1 = (-coef_b + math.sqrt(discriminante)) / (2 * coef_a)
                raiz2 = (-coef_b - math.sqrt(discriminante)) / (2 * coef_a)
                resultado = f"x₁ = {raiz1} | x₂ = {raiz2}"
                etapas = f"Δ = {discriminante} | x = (-({coef_b}) ± √{discriminante}) / (2·{coef_a})"

    else:
        valor_b = request.form.get("num2", "").strip()
        if not valor_b:
            return render_template(
                "calculadora.html",
                etapas="Erro: Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(valor_b)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"

        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} × {num2} = {resultado}"

        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro"
                etapas = "Erro: Divisão por zero não é permitida."
            else:
                resultado = num1 / num2
                etapas = f"{num1} ÷ {num2} = {resultado}"

        elif operacao == "**":
            try:
                resultado = math.pow(num1, num2)
                etapas = f"{num1} ^ {num2} = {resultado}"
            except OverflowError:
                resultado = "Erro"
                etapas = "Erro: Resultado muito grande (estouro de memória)."
            except ValueError:
                resultado = "Erro"
                etapas = "Erro: Base negativa com expoente fracionário."

        else:
            resultado = "Erro"
            etapas = "Operação inválida."

    return render_template(
        "calculadora.html", etapas=etapas, resultados=resultado
    )


if __name__ == "__main__":
    app.run(debug=True)