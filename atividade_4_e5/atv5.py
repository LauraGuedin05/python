from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Lista de usuários para acesso (dicionários)
usuarios = [
    {'usuario': 'marcos', 'senha': 'cotemig2026'},
    {'usuario': 'janaina', 'senha': 'cotemig2026'},
    {'usuario': 'laura', 'senha': '145366'}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    falha_login = None
    if request.method == 'POST':
        usuario_informado = request.form['usuario']
        senha_informada = request.form['senha']

        # Percorrer a lista de usuários com for
        credenciais_validas = False
        for conta in usuarios:
            if conta['usuario'] == usuario_informado and conta['senha'] == senha_informada:
                credenciais_validas = True
                break

        if credenciais_validas:
            session['usuario'] = usuario_informado
            return render_template('home.html', mensagem=f"Bem-vindo, {usuario_informado}!")
        else:
            falha_login = "Usuário ou senha inválidos!"

    return render_template('login.html', erro=falha_login)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)