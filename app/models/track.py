from .db import db

class Track(db.Model):
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key = True)
    song_title = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String, nullable=False)
    source_url = db.Column(db.String, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
