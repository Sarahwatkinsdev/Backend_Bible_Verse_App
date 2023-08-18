from flask import Blueprint, request, jsonify, current_app
from app.models.save import SavedVerse
from app import db
from app.models.user import User


save_bp = Blueprint('save', __name__)

@save_bp.route('/saved_verses', methods=['GET'])
def get_saved_verses():
    saved_verses = SavedVerse.query.filter_by(user_id=User.id).all()

    saved_verses_data = [
        {
            'id': saved_verse.id,
            'verse_text': saved_verse.verse_text
        }
        for saved_verse in saved_verses
    ]

    return jsonify(saved_verses_data), 200


@save_bp.route('/save', methods=['POST'])
def save_verse():
    verse_text = request.json.get('verse_text')
    
    if not verse_text:
        return jsonify({'message': 'Verse text is required'}), 400

    saved_verse = SavedVerse(user_id=User.id, verse_text=verse_text)
    db.session.add(saved_verse)
    db.session.commit()
    
    return jsonify({'message': 'Verse saved successfully'}), 201


@save_bp.route('/saved_verses/<int:verse_id>', methods=['DELETE'])
def delete_saved_verse(verse_id):
    saved_verse = SavedVerse.query.get_or_404(verse_id)

    if saved_verse.user_id != User.id:
        return jsonify({'message': 'Unauthorized'}), 403

    db.session.delete(saved_verse)
    db.session.commit()

    return jsonify({'message': 'Verse deleted successfully'}), 200