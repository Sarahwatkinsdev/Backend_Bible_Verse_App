from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required, current_user
from app.models.save import SavedVerse
from app import db

save_bp = Blueprint('save', __name__)

@save_bp.route('/save', methods=['POST'])
@login_required
def save_verse():
    verse_text = request.json.get('verse_text')
    
    if not verse_text:
        return jsonify({'message': 'Verse text is required'}), 400

    saved_verse = SavedVerse(user_id=current_user.id, verse_text=verse_text)
    db.session.add(saved_verse)
    db.session.commit()

    return jsonify({'message': 'Verse saved successfully'}), 201
