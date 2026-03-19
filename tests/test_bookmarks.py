"""
tests/test_bookmarks.py

Tests unitaires pour l'application Bookmark.
Vérifie le CRUD des bookmarks via la base de données et l'API Flask.
"""

import unittest
from app import create_app
from app.extensions import db
from app.models import Bookmark

class BookmarkTestCase(unittest.TestCase):

    def setUp(self):
        # Créer l'application en mode testing
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        self.client = self.app.test_client()

        # Créer les tables
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        # Supprimer les tables
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_bookmark(self):
        with self.app.app_context():
            bm = Bookmark(title="GitHub", url="https://github.com")
            db.session.add(bm)
            db.session.commit()

            self.assertEqual(Bookmark.query.count(), 1)
            self.assertEqual(Bookmark.query.first().title, "GitHub")

    def test_read_bookmark(self):
        with self.app.app_context():
            bm = Bookmark(title="GitHub", url="https://github.com")
            db.session.add(bm)
            db.session.commit()

            response = self.client.get("/bookmarks")
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
