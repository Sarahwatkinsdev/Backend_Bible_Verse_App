from app import db
from app.models.save import SavedVerse
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    password_hash = db.Column(db.String(150), unique=False, nullable=False)

    # Define other user fields (e.g., email, password, etc.)

    saved_verses = db.relationship('SavedVerse', backref='user', lazy=True)

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}')"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)      
    
    def serialize(self):
        return {
        'username': self.username,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'saved_verses': self.saved_verses
        }