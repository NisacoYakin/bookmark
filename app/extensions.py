"""
app/extensions.py

Initialisation centralisée des extensions Flask pour le projet Bookmark.
Permet d'utiliser ces extensions dans tous les modules sans les réinitialiser.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# Initialisation "vide", les objets seront liés à l'app plus tard
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def init_app(app):
    """
    Lie toutes les extensions à l'application Flask.
    À appeler dans app/__init__.py ou run.py après création de l'objet Flask.
    """

    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    print("[EXTENSIONS] Extensions initialisées avec succès.")
