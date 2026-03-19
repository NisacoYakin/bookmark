# scripts/test_db.py
import json
from app import create_app
from app.extensions import db
from flask import url_for

# Création de l'app Flask
app = create_app()

# On utilise le contexte de l'application pour accéder à db et aux routes
with app.app_context():
    # Test de la connexion à la base de données
    try:
        conn = db.engine.connect()
        print("✅ Connexion DB réussie:", conn)
        conn.close()
    except Exception as e:
        print("❌ Échec connexion DB:", e)

# Import de la librairie de test Flask
from flask.testing import FlaskClient

# Client de test Flask
client = app.test_client()

# --- TEST ROUTE HOME ---
print("\n--- TEST /home ---")
response = client.get("/home")
print(f"Status: {response.status_code}")
print(f"Response: {response.data.decode('utf-8')}")

# --- TEST CRUD /bookmarks ---
print("\n--- TEST CRUD /bookmarks ---")

# 1️⃣ CREATE
bookmark_data = {"title": "Test Bookmark", "url": "https://example.com", "description": "Test description"}
response = client.post("/bookmarks", data=json.dumps(bookmark_data),
                       content_type='application/json')
print(f"POST /bookmarks → Status: {response.status_code}, Response: {response.get_json()}")

# Récupération de l'ID créé
bookmark_id = response.get_json().get("id")

# 2️⃣ READ ALL
response = client.get("/bookmarks")
print(f"GET /bookmarks → Status: {response.status_code}, Response: {response.get_json()}")

# 3️⃣ READ ONE
response = client.get(f"/bookmarks/{bookmark_id}")
print(f"GET /bookmarks/{bookmark_id} → Status: {response.status_code}, Response: {response.get_json()}")

# 4️⃣ UPDATE
update_data = {"title": "Updated Bookmark", "description": "Updated description"}
response = client.put(f"/bookmarks/{bookmark_id}", data=json.dumps(update_data),
                      content_type='application/json')
print(f"PUT /bookmarks/{bookmark_id} → Status: {response.status_code}, Response: {response.get_json()}")

# 5️⃣ DELETE
response = client.delete(f"/bookmarks/{bookmark_id}")
print(f"DELETE /bookmarks/{bookmark_id} → Status: {response.status_code}, Response: {response.get_json()}")

print("\n✅ Tous les tests CRUD ont été exécutés.")



