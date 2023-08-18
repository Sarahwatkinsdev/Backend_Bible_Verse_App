from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    # Load environment variables from .env
    load_dotenv()

    # Initialize extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Import and register blueprints
    from app.routes import save_routes, verse_routes, user_routes

    app.register_blueprint(save_routes.save_bp)
    app.register_blueprint(verse_routes.verse_bp)
    app.register_blueprint(user_routes.user_bp)

    return app
