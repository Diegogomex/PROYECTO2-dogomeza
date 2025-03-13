from flask import Flask, render_template
from app.config.config import Config
from app.config.db import db
from app.controllers.heladeria_controller import HeladeriaController

app = Flask(__name__, template_folder="views")
app.config.from_object(Config)

db.init_app(app)

heladeria_controller = HeladeriaController(app, db) # Crear una instancia del controlador y pasarle app y db

@app.route("/")
def home():
    with app.app_context():
        productos = heladeria_controller.listar_productos()
        return render_template("index.html", productos=productos)

with app.app_context():
    db.create_all() 

if __name__ == "__main__":
    app.run(debug=True)