from app.models import db, Artist

def seed_artists():
    artist1 = Artist(
        artist_name="Louis Armstrong And His Orchestra",
        image_url='https://cdn2.jazztimes.com/2020/09/louis-armstrong-with-luis-russell-band-800x519.jpg',

    )

    artist2 = Artist(
        artist_name="Duke Ellington And His Famous Orchestra",
        image_url='https://cdn.britannica.com/73/201073-050-7A256B9D/big-band-jazz-greats-Duke-Ellington-Otto.jpg',
    )

    artist3 = Artist(
        artist_name="Harry James and the Boogie Woogie Trio",
        image_url='https://m.media-amazon.com/images/I/81QpdPHQeEL._SS500_.jpg',
    )

    artist4 = Artist(
        artist_name="Billie Holiday and her Orchestra",
        image_url='https://images-na.ssl-images-amazon.com/images/I/513REbiChRL._AC_.jpg'
    )

    artist1 = Album(
        artist_name="Louis Armstrong and his Hot Five",
        image_url='',
    )

    db.session.add(artist1)
    db.session.add(artist2)
    db.session.add(artist3)
    db.session.add(artist4)
    db.session.commit()
    # artist1 = Album(
    #     artist_name="",
    #     image_url='',
    # )
def undo_artists():
    db.session.execute('TRUNCATE artists RESTART IDENTITY CASCADE;')
    db.session.commit()
