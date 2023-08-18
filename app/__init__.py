from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint

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
    from app.routes import register_routes
    register_routes(app)  # Register all routes w/ register_routes func
    
    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = '/static/swagger.json'  # Your API definition file's URL
    
    # Call factory function to create blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Test application"
        }
    )
    
    @login_manager.user_loader
    def load_user(user_id):
        return load_user.query.get(int(user_id))
    
    app.register_blueprint(swaggerui_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
