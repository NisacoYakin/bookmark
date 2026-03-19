from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.bookmark import Bookmark

bookmark_bp = Blueprint("bookmark_bp", __name__, url_prefix="/bookmarks")

# CREATE
@bookmark_bp.route("/", methods=["POST"])
def create_bookmark():
    data = request.json
    if not data or "title" not in data or "url" not in data:
        return jsonify({"error": "Les champs 'title' et 'url' sont requis."}), 400

    new_bm = Bookmark(
        title=data["title"],
        url=data["url"],
        description=data.get("description")
    )
    db.session.add(new_bm)
    db.session.commit()
    return jsonify(new_bm.to_dict()), 201

# READ ALL
@bookmark_bp.route("/", methods=["GET"])
def get_bookmarks():
    bookmarks = Bookmark.query.all()
    return jsonify([b.to_dict() for b in bookmarks]), 200

# READ ONE
@bookmark_bp.route("/<int:id>", methods=["GET"])
def get_bookmark(id):
    bm = Bookmark.query.get_or_404(id)
    return jsonify(bm.to_dict()), 200

# UPDATE
@bookmark_bp.route("/<int:id>", methods=["PUT"])
def update_bookmark(id):
    bm = Bookmark.query.get_or_404(id)

    data = request.get_json()

    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400

    print("DATA RECEIVED:", data)  # DEBUG

    bm.title = data.get("title", bm.title)
    bm.url = data.get("url", bm.url)
    bm.description = data.get("description", bm.description)

    db.session.commit()

    return jsonify(bm.to_dict()), 200
    

# DELETE
@bookmark_bp.route("/<int:id>", methods=["DELETE"])
def delete_bookmark(id):
    bm = Bookmark.query.get_or_404(id)
    db.session.delete(bm)
    db.session.commit()
    return jsonify({"message": f"Bookmark {id} supprimé avec succès."}), 200