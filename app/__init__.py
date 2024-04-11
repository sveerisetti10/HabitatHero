import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Set the secret key. Consider adding it to a .env file or your environment variables
    app.secret_key = os.getenv('SECRET_KEY', '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')

    # Ensure you don't use 'your_default_secret_key_here' in production
    from .routes import main as main_routes
    app.register_blueprint(main_routes)

    return app