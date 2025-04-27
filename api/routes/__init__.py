from .user import user_bp

def register_routes(app):

    """Register all routes with the Flask app."""
    
    app.register_blueprint(user_bp)