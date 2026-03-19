from flask import Flask
from flask_cors import CORS                # ⚡ importer CORS
from .extensions import db, migrate
from .routes import register_routes
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialisation des extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # ⚡ Appliquer CORS après la création de l'app
    CORS(app)

    # Enregistrement des routes
    register_routes(app)

    return app