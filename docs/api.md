# Documentation API Bookmark

## 1. Endpoints principaux

| Méthode | URL                 | Description                 |
|----------|-------------------|----------------------------|
| GET      | /bookmarks         | Récupère tous les bookmarks |
| GET      | /bookmarks/<id>    | Récupère un bookmark par id |
| POST     | /bookmarks         | Crée un bookmark            |
| PUT      | /bookmarks/<id>    | Met à jour un bookmark      |
| DELETE   | /bookmarks/<id>    | Supprime un bookmark        |
| GET      | /test-db           | Teste la connexion DB       |

## 2. Payload POST / PUT

```json
{
    "title": "Nom du site",
    "url": "https://exemple.com"
}


3. Réponses
200 OK : action réussie
400 Bad Request : erreur de validation
404 Not Found : bookmark non trouvé
500 Internal Server Error : erreur serveur


