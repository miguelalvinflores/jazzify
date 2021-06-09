from .db import db

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key = True)
    artist_name = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String, nullable=False)

    albums = db.relationship('Album', backref='artist', lazy="joined")
    tracks = db.relationship('Track', backref='artist', lazy='joined')

    def to_dict(self):
        return {
            'id': self.id,
            'artist_name': self.artist_name,
            'image_url': self.image_url
        }
