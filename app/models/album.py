from .db import db

class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key = True)
    album_title = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)

    tracks = db.relationship('Track', backref='album', lazy='joined')

    def to_dict(self):
        return{
            "id": self.id,
            "album_title": self.album_title,
            "image_url": self.image_url,
            "artist_id": self.artist_id
        }
