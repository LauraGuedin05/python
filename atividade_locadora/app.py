from flask import Flask, redirect
from models import db
from controllers.locadora_controller import locadora_bp

app = Flask(__name__, template_folder="views/templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///locadora.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(locadora_bp)


@app.route("/")
def home():
    return redirect("/locadora/")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
