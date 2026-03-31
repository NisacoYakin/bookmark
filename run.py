"""
run.py
Point d'entrée de l'application Bookmark.
Lance le serveur Flask.
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Serveur de développement (pour Termux)
    
    port = int(os.environ.get("PORT", 5000))  # Render injecte PORT
    app.run(host="0.0.0.0", port=port,   debug=True)
    
