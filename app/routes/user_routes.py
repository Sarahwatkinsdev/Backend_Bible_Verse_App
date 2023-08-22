from flask import Blueprint, request, jsonify, make_response
from app.models.user import User
from app import db
import json

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return make_response(jsonify({"message": "Username and password are required."}), 400)

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return make_response(jsonify({"message": "Invalid username or password."}), 401)

    return jsonify({"message": "Login successful.", "user": user.serialize()}), 200


@user_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    first_name = data.get("firstName")
    last_name = data.get("lastName")

    if not username or not password or not first_name or not last_name:
        return make_response(jsonify({"message": "Username, password, first name, and last name are required."}), 400)

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return make_response(jsonify({"message": "Username already taken."}), 409)

    new_user = User(username=username, first_name=first_name, last_name=last_name)
    new_user.set_password(password)  
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.serialize()), 201

# @user_bp.route("/profile", methods=["GET"])
# def get_user_profile():
#     user_data = {
#         "id": 1,
#         "username": "Goldfish",
#         "saved_verses": "Luke",
#     }
#     return jsonify(user_data)
