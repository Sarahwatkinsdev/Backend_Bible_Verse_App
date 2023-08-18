from flask import Blueprint, jsonify
from app.routes.main_routes import main_bp


main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return jsonify(message="Welcome to the Bible Verse App!")

def register_routes(app):
    app.register_blueprint(main_bp)
