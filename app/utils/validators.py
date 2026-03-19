"""
utils/validators.py

Fonctions utilitaires pour valider les données des bookmarks.
Peut être étendu pour d'autres validations dans le projet.
"""

import re

def is_valid_url(url: str) -> bool:
    """
    Vérifie si une URL est valide (http, https).
    """
    regex = re.compile(
        r'^(https?://)'             # http:// ou https://
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,})'  # nom de domaine
        r'(:\d+)?'                  # port optionnel
        r'(\/\S*)?$'                # chemin optionnel
    )
    return bool(regex.match(url))


def is_non_empty_string(value: str) -> bool:
    """
    Vérifie si une chaîne est non vide et non composée que d'espaces.
    """
    return isinstance(value, str) and value.strip() != ""


def validate_bookmark_data(title: str, url: str) -> tuple[bool, str]:
    """
    Valide les données d'un bookmark.
    Retourne (True, "") si valide, sinon (False, "erreur").
    """
    if not is_non_empty_string(title):
        return False, "Le titre ne peut pas être vide."
    if not is_non_empty_string(url):
        return False, "L'URL ne peut pas être vide."
    if not is_valid_url(url):
        return False, "L'URL n'est pas valide."
    return True, ""
