from app import db

class SavedVerse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    verse_text = db.Column(db.Text, nullable=False)

    # Define any additional fields as needed

    def __repr__(self):
        return f"SavedVerse(user_id={self.user_id}, verse_text='{self.verse_text}')"
