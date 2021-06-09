from flask import Blueprint
from app.models import Artist, artist,  db

artist_routes = Blueprint('artist', __name__)


@artist_routes.route('/allArtists')
def get_AllArtists():
    artists = Artist.query.all()
    artistlist = {'artists': [artist.to_dict() for artist in artists]}
    return artistlist
