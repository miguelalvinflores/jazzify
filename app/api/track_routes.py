from flask import Blueprint
from app.models import Track, Album, db

track_routes = Blueprint('track', __name__)


@track_routes.route('album/<int:albumId>')
def get_tracks_by_albumId(albumId):
    album = Album.query.filter(Album.id == albumId).first()
    tracks = Track.query.filter(Track.album_id == albumId).all()
    albumTracks = {album.album_title: [track.to_dict() for track in tracks]}
    return albumTracks
