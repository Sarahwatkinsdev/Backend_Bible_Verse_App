from flask import Blueprint, request, jsonify, make_response
from app.models.feature import Feature
from app import db
import json
from sqlalchemy import desc

feature_bp = Blueprint("feature", __name__, url_prefix="/feature")
@feature_bp.route("/", methods=["GET"])
def get_feature():
    feature = Feature.query.order_by(desc(Feature.date)).first()
    return jsonify({"message": "Latest feature", "feature": feature.serialize()}), 200

@feature_bp.route("/", methods=["POST"])
def create_feature():
    data = request.get_json()
    prefix = data.get("prefix")
    verse_text = data.get("verse_text")
    verse_ref = data.get("verse_ref")

    new_feature = Feature(prefix=prefix, verse_text=verse_text, verse_ref=verse_ref)
    db.session.add(new_feature)
    db.session.commit()

    return jsonify({"message": "Created a new verse Feature.", "feature": new_feature.serialize()}), 201

