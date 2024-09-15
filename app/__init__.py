from flask import Flask
from .routes import main as main_bp  # Import the 'main' blueprint

def create_app():
    app = Flask(__name__)
    
    # Registrar blueprint
    app.register_blueprint(main_bp)  # Register the 'main' blueprint
    
    return app
