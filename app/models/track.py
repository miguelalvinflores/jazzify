from .db import db

class Track(db.Model):
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key = True)
    artist_name = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String, nullable=False)

    albums = db.relationship('Albums', backref='person', lazy=True)
