import os
from flask import Blueprint, request, jsonify, current_app
import requests
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


@verse_bp.route('/search_verses', methods=['GET'])
def search_verses():
    search_query = request.args.get('query')

    if not search_query:
        return jsonify({'message': 'Search query is required'}), 400

    
    # Retrieve the BIBLE_API_KEY from .env file
    api_key = current_app.config['BIBLE_API_KEY']
    bibleVersionID = 'de4e12af7f28f599-01'
    offset = 0

    if not api_key:
        return jsonify({'message': 'Bible API key is missing'}), 500

    # Retrieve verses from the Bible API based on search query

    headers = {'api-key': api_key, 'accept': 'application/json'}
    api_url = f'https://api.scripture.api.bible/v1/bibles/{bibleVersionID}/search?query={search_query}&offset={offset}'

    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        return jsonify({'message': 'Failed to retrieve verses from the API'}), 500

    verses_data = response.json()['data']['verses']
    # Extract and format the relevant verse information from the API response
    verses = [{'text': verse_data['text'], 'reference': verse_data['reference']} for verse_data in verses_data]

    return jsonify({'verses': verses})