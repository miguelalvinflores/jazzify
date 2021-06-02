from .db import db

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key = True)
    artist_name = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String, nullable=False)

    albums = db.relationship('Albums', backref='person', lazy=True)
