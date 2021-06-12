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
        artist_name="Billie Holiday and Her Orchestra",
        image_url='https://images-na.ssl-images-amazon.com/images/I/513REbiChRL._AC_.jpg'
    )

    artist5 = Artist(
        artist_name="Teddy Wilson and His Orchestra",
        image_url='https://www.hepjazz.com/images/artists/teddy_wilson_2.jpg',
    )

    artist6 = Artist(
        artist_name="The King Cole Trio",
        image_url='https://syncopatedtimes.com/wp-content/uploads/2019/11/King-Cole-Trio.jpg',
    )

    artist7 = Artist(
        artist_name="Enric Madriguera and Orchestra",
        image_url='https://i.ytimg.com/vi/L9lhMa2aokA/mqdefault.jpg',
    )

    artist8 = Artist(
        artist_name='"Fats" Waller and His Buddies',
        image_url='https://www.vocalgroupharmony.com/3ROWNEW/FatsWallerDeeps.jpg',
    )

    # artist9 = Artist(
    #     artist_name="Bessie Smith",
    #     image_url='https://www.liveabout.com/thmb/8I3V8RuA7MlpkYdPpCkRaq6vFHE=/1785x1339/smart/filters:no_upscale()/Bessie_Smith_on_stage-5b224d293037130036633665.jpg',
    # )


    db.session.add(artist1)
    db.session.add(artist2)
    db.session.add(artist3)
    db.session.add(artist4)
    db.session.add(artist5)
    db.session.add(artist6)
    db.session.add(artist7)
    db.session.add(artist8)
    # db.session.add(artist9)

    db.session.commit()
    # artist1 = Artist(
    #     artist_name="Bessie Smith",
    #     image_url='https://www.liveabout.com/thmb/8I3V8RuA7MlpkYdPpCkRaq6vFHE=/1785x1339/smart/filters:no_upscale()/Bessie_Smith_on_stage-5b224d293037130036633665.jpg',
    # )
def undo_artists():
    db.session.execute('TRUNCATE artists RESTART IDENTITY CASCADE;')
    db.session.commit()
