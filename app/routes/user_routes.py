from flask import Blueprint, jsonify, current_app
from flask_login import login_required, current_user
from app.models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@login_required
def get_user_profile():
    user_data = {
        'id': current_user.id,
        'username': current_user.username,
        'saved_verses': current_user.saved_verses,
    }
    return jsonify(user_data)
