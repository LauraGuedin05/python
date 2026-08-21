from flask import Blueprint, flash, redirect, render_template, request, url_for

from models import Cadastro, db

cadastros_bp = Blueprint("cadastros", __name__, url_prefix="/cadastros")


@cadastros_bp.route("/")
def lista():
    cadastros = Cadastro.listar()
    return render_template("cadastros/lista.html", cadastros=cadastros)


@cadastros_bp.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        try:
            registro = Cadastro.a_partir_de_dict(request.form)
        except ValueError as exc:
            flash(str(exc), "erro")
            return render_template("cadastros/formulario.html"), 400

        if not registro.nome or not registro.profissao:
            flash("Nome e profissão são obrigatórios.", "erro")
            return render_template("cadastros/formulario.html"), 400

        db.session.add(registro)
        db.session.commit()
        return redirect(url_for("cadastros.detalhe", cadastro_id=registro.id))

    return render_template("cadastros/formulario.html")


@cadastros_bp.route("/<int:cadastro_id>")
def detalhe(cadastro_id):
    cadastro = db.session.get(Cadastro, cadastro_id)
    if not cadastro:
        return render_template(
            "cadastros/nao_encontrado.html", cadastro_id=cadastro_id
        ), 404
    return render_template("cadastros/detalhe.html", cadastro=cadastro)
