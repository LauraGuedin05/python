from flask import Blueprint, redirect, render_template, request, url_for

from models import Jogador, db

jogador_bp = Blueprint("jogador", __name__, url_prefix="/jogadores")


@jogador_bp.route("/")
def index():
    atletas = Jogador.listar()
    return render_template("jogadores/lista.html", jogadores=atletas)


@jogador_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        novo_jogador = Jogador(
            nome=request.form["nome"],
            posicao=request.form["posicao"],
            clube=request.form["clube"],
            cabeceio=int(request.form["cabeceio"]),
            forca=int(request.form["forca"]),
        )
        db.session.add(novo_jogador)
        db.session.commit()
        return redirect(url_for("jogador.index"))
    return render_template("jogadores/formulario.html")


@jogador_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    atleta = db.session.get(Jogador, id)
    if request.method == "POST":
        atleta.nome = request.form["nome"]
        atleta.posicao = request.form["posicao"]
        atleta.clube = request.form["clube"]
        atleta.cabeceio = int(request.form["cabeceio"])
        atleta.forca = int(request.form["forca"])
        db.session.commit()
        return redirect(url_for("jogador.index"))
    return render_template("jogadores/formulario.html", jogador=atleta)


@jogador_bp.route("/excluir/<int:id>")
def excluir(id):
    atleta = db.session.get(Jogador, id)
    db.session.delete(atleta)
    db.session.commit()
    return redirect(url_for("jogador.index"))
