from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cadastro_alunos = [
        {"nome": "Bruno", "idade": 15, "nota": 8.5},
        {"nome": "Camila", "idade": 16, "nota": 6.0},
        {"nome": "Daniel", "idade": 15, "nota": 7.0},
        {"nome": "Fernanda", "idade": 17, "nota": 4.5}
    ]

    return render_template('index.html', alunos=cadastro_alunos)

if __name__ == '__main__':
    app.run(debug=True)