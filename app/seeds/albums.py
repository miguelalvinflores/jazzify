from app.models.album import Album
from app.models import db, Album

def seed_albums():
    album1 = Album(
        album_title="Louis Armstrong Classics",
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg',
        artist_id='1',
    )
    album2 = Album(
        album_title="A Duke Ellington Panorama",
        image_url='https://ia600607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362_itemimage.jpg',
        artist_id='2',
    )

    album3 = Album(
        album_title="Boogie Woogie",
        image_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675_itemimage.jpg',
        artist_id='3',
    )
    album4 = Album(
        album_title="Billie Holiday Vol. 1",
        image_url='https://ia800108.us.archive.org/14/items/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202_itemimage.jpg',
        artist_id='3',
    )

    album5 = Album(
        album_title="Louis Armstrong Paris 1934 Spotlight Series",
        image_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403_itemimage.jpg',
        artist_id='1',
    )

    album6 = Album(
        album_title="Duke Ellington Plays the Blues",
        image_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273_itemimage.jpg',
        artist_id='2',
    )

    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.add(album4)
    db.session.add(album5)
    db.session.add(album6)

    db.session.commit()

    # album1 = Album(
    #     album_title="",
    #     image_url='',
    #     artist_id='num',
    # )


def undo_albums():
    db.session.execute('TRUNCATE albums RESTART IDENTITY CASCADE;')
    db.session.commit()
