from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def curriculo():
    informacoes = {
        "nome": "Laura Guedin",
        "email": "lauraguedin3@gmail.com",
        "escola": "Escola Técnica do COTEMIG",
        "tecnologias": ["MySQL", "C#", "N8N", "Python", "React"]
    }
    return render_template('index.html', **informacoes)

@app.route('/cotemig/<nome_escola>')
def rota_cotemig(nome_escola):
    return f"<h1>{nome_escola}</h1>"

@app.route('/a')
def curriculo2():
    informacoes = {
        "nome": "Laura Guedin",
        "email": "lauraguedin3@gmail.com",
        "escola": "Escola Técnica do COTEMIG",
        "tecnologias": ["MySQL", "C#", "N8N", "Python", "React"]
    }
    return render_template('index.html', **informacoes)


if __name__ == '__main__':
    app.run(debug=True)
