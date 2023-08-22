from app import db
from datetime import datetime

class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.String(50), unique=False, nullable=False)
    verse_text = db.Column(db.String(1000), unique=False, nullable=False)
    verse_ref = db.Column(db.String(50), unique=False, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Feature(id={self.id}, verse_ref='{self.verse_ref}')"

    def serialize(self):
        return {
        'prefix': self.prefix,
        'verse_text': self.verse_text,
        'verse_ref': self.verse_ref,
        'date': self.date
        }