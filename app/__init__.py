from flask import Flask, render_template
from app.config.config import Config
from app.config.db import db
from app.controllers.heladeria_controller import HeladeriaController
from app.config.routes import crear_bp_ventas


def create_app():
    app = Flask(__name__, template_folder="views")
    app.config.from_object(Config)


    db.init_app(app)

    with app.app_context():
        db.create_all() 

    heladeria_controller = HeladeriaController(app, db) # Crear una instancia del controlador y pasarle app y db

    ventas_bp =crear_bp_ventas (heladeria_controller)
    app.register_blueprint(ventas_bp)

    @app.route("/")
    def home():
        with app.app_context():
            productos = heladeria_controller.listar_productos()
            return render_template("index.html", productos=productos)


    if __name__ == "__main__":
        app.run(debug=True)

    return app