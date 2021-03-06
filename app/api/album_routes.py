from flask import Blueprint, request
from app.models import Album, album, db
import random

album_routes = Blueprint('album', __name__)


@album_routes.route('/allAlbums')
def get_allAlbums():
    # print("INSIDE album route")
    albums = Album.query.all()
    albumlist = {'albums': [album.to_dict() for album in albums]}
    return albumlist


@album_routes.route('/album')
def get_album():
    album = Album.query.filter(Album.id == random.randint(1, 3)).first()
    return album.to_dict()
