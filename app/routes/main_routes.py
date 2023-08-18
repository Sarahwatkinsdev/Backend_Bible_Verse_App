from flask import Blueprint, jsonify

# Create a Blueprint for your routes
main_bp = Blueprint("main", __name__)

# Define a route for the root URL ("/")
@main_bp.route("/")
def index():
    return jsonify(message="Welcome to the Bible Verse App!")
