from flask import Blueprint, jsonify

main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def index():
    return "Bienvenue sur Bookmark API"

@main_bp.route("/home")
def home():
    return jsonify({"message": "Bienvenue sur Bookmark App! Utilisez /bookmarks pour accéder à vos bookmarks."})