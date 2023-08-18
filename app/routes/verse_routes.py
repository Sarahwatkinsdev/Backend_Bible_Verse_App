from flask import Blueprint, request, jsonify
from app.models.verse import Verse, Topic
from app import db

verse_bp = Blueprint('verse', __name__)

@verse_bp.route('/assign_topic', methods=['POST'])
def assign_topic():
    verse_id = request.json.get('verse_id')
    topic_id = request.json.get('topic_id')

    verse = Verse.query.get(verse_id)
    topic = Topic.query.get(topic_id)

    if not verse or not topic:
        return jsonify({'message': 'Verse or topic not found'}), 404

    verse.topics.append(topic)
    db.session.commit()

    return jsonify({'message': 'Verse assigned to topic successfully'}), 201

@verse_bp.route('/get_verses_by_topic', methods=['GET'])
def get_verses_by_topic():
    topic_id = request.args.get('topic_id')

    topic = Topic.query.get(topic_id)

    if not topic:
        return jsonify({'message': 'Topic not found'}), 404

    verses = topic.verses.all()
    verse_texts = [verse.text for verse in verses]

    return jsonify({'verses': verse_texts})
