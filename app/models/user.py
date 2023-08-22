from app import db
from app.models.save import SavedVerse

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    # Define other user fields (e.g., email, password, etc.)

    saved_verses = db.relationship('SavedVerse', backref='user', lazy=True)

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}')"
    

