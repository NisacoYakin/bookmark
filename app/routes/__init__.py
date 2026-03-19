from .main_route import main_bp
from .bookmark_routes import bookmark_bp

def register_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(bookmark_bp)