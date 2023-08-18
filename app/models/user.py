from app import db
from flask_login import UserMixin, current_user
from app.models.save import SavedVerse

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    # Define other user fields (e.g., email, password, etc.)

    saved_verses = db.relationship('SavedVerse', backref='user', lazy=True)

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}')"
    
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
