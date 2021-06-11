from app.models import album
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
    album7 = Album(
        album_title="Teddy Wilson - Billie Holiday",
        image_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368_itemimage.jpg',
        artist_id='4',
    )

    album8 = Album(
        album_title="The King Cole Trio",
        image_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215_itemimage.jpg',
        artist_id='6',
    )

    album9 = Album(
        album_title="The King Cole Trio Vol.2",
        image_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357_itemimage.jpg',
        artist_id='6',
    )

    album10 = Album(
        album_title="Duke Ellington and his famous Orchestra at Carnegie Hall",
        image_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398_itemimage.jpg',
        artist_id='2',
    )

    album11 = Album(
        album_title="Ellington Special",
        image_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027_itemimage.jpg',
        artist_id='2',
    )

    album12 = Album(
        album_title="Louis Armstrong and His Hot 5",
        image_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896_itemimage.jpg',
        artist_id='1',
    )

    album13 = Album(
        album_title="King Louis - Hot Jazz Classics",
        image_url='https://ia902803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774_itemimage.jpg',
        artist_id='1',
    )
    album14 = Album(
        album_title="Louis Armstrong's Hot 5",
        image_url='https://ia803101.us.archive.org/22/items/78_im-not-rough_louis-armstrong-and-his-hot-five-hardin-louis-armstrong-kid-ory-johnn_gbia0039399/78_im-not-rough_louis-armstrong-and-his-hot-five-hardin-louis-armstrong-kid-ory-johnn_gbia0039399_itemimage.jpg',
        artist_id='1',
    )

    album15 = Album(
        album_title="Music of Latin America",
        image_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363_itemimage.jpg',
        artist_id='7',
    )

    album16 = Album(
        album_title='"Fats" Waller Favorites',
        image_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100_itemimage.jpg',
        artist_id='8',
    )

    album17 = Album(
        album_title="King Cole Trio Vol.3",
        image_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699_itemimage.jpg',
        artist_id='6',
    )

    album18 = Album(
        album_title="King Cole Trio Vol.4",
        image_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263_itemimage.jpg',
        artist_id='6',
    )

    album19 = Album(
        album_title="Waller on the Ivories",
        image_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986_itemimage.jpg',
        artist_id='8',
    )

    album20 = Album(
        album_title="Waller at the Console",
        image_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640_itemimage.jpg',
        artist_id='8',
    )

    album21 = Album(
        album_title="London Suite",
        image_url='https://ia903109.us.archive.org/31/items/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014_itemimage.jpg',
        artist_id='8',
    )

    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.add(album4)
    db.session.add(album5)
    db.session.add(album6)
    db.session.add(album7)
    db.session.add(album8)
    db.session.add(album9)
    db.session.add(album10)
    db.session.add(album11)
    db.session.add(album12)
    db.session.add(album13)
    db.session.add(album14)
    db.session.add(album15)
    db.session.add(album16)
    db.session.add(album17)
    db.session.add(album18)
    db.session.add(album19)
    db.session.add(album20)
    db.session.add(album21)

    db.session.commit()

    # album1 = Album(
    #     album_title="",
    #     image_url='',
    #     artist_id='num',
    # )


def undo_albums():
    db.session.execute('TRUNCATE albums RESTART IDENTITY CASCADE;')
    db.session.commit()
