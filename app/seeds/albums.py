from app.models.album import Album
from app.models import db, Album

def seed_albums():
    album1 = Album(
        album_title="Louis Armstrong Classics"
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg'
        artist_id='1'
    )

    db.session.add(album1)

    # album1 = Album(
    #     album_title=""
    #     image_url=''
    #     artist_id='num'
    # )
