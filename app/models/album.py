from .db import db

class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key = True)
    album_title = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String, nullable=False)
    artist_id = db.Column(db.String(200), db.ForeignKey('artist.id'), nullable=False)
