"""
scripts/seed_db.py

Script pour insérer des bookmarks de test dans la base de données.
"""

from app import create_app
from app.extensions import db
from app.models import Bookmark

app = create_app()

with app.app_context():
    # Supprimer les anciennes données
    db.session.query(Bookmark).delete()

    # Seed initial
    bookmarks = [
        Bookmark(title="GitHub", url="https://github.com"),
        Bookmark(title="Neon.tech", url="https://neon.tech"),
        Bookmark(title="Supabase", url="https://supabase.com")
    ]

    db.session.add_all(bookmarks)
    db.session.commit()
    print(f"[SEED_DB] {len(bookmarks)} bookmarks ajoutés avec succès.")
