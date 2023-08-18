from app import db

verse_topics = db.Table(
    'verse_topics',
    db.Column('verse_id', db.Integer, db.ForeignKey('verse.id')),
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'))
)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Topic(id={self.id}, name='{self.name}')"

class Verse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    topics = db.relationship('Topic', secondary=verse_topics, backref=db.backref('verses', lazy='dynamic'))

    def __repr__(self):
        return f"Verse(id={self.id}, text='{self.text}')"
