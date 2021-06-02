from app.models import db, Track

def seed_tracks():
    track1 = Track(
        song_title="Mahogany Hall Stomp"
        image_url="https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg"
        source_url="https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/01%20-%20Mahogany%20Hall%20Stomp%20-%20Louis%20Armstrong%20And%20His%20Orchestra.mp3"
        album_id=1
        artist_id=1
    )

    track2 = Track(
        song_title='West End Blues'
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg'
        source_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/02%20-%20West%20End%20Blues%20-%20Louis%20Armstrong%20And%20His%20Orchestra-Restored.mp3'
        album_id='1'
        artist_id='1'
    )

    track3 = Track(
        song_title='On the Sunny Side of the Street'
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg'
        source_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/03%20-%20On%20the%20Sunny%20Side%20of%20t%20-%20Louis%20Armstrong%20And%20His%20Orchestra-Restored.mp3'
        album_id='1'
        artist_id='1'
    )

    track4 = Track(
        song_title='Satchel Mouth Swing'
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg'
        source_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/04%20-%20Satchel%20Mouth%20Swing%20-%20Louis%20Armstrong%20And%20His%20Orchestra-Restored.mp3'
        album_id='1'
        artist_id='1'
    )

    track5 = Track(
        song_title="Struttin' with Some Barbecue"
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg'
        source_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/05%20-%20Struttin%27%20with%20Some%20Barbecue%20-%20Louis%20Armstrong%20And%20His%20Orchestra.mp3'
        album_id='1'
        artist_id='1'
    )

    track6 = Track(
        song_title="Confessin' That I Love You"
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg'
        source_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/06%20-%20Confessin%27%20That%20I%20Love%20You%20-%20Louis%20Armstrong%20And%20His%20Orchcestra.mp3'
        album_id='1'
        artist_id='1'
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)

    


    # track3 = Track(
    #     song_title=""
    #     image_url=''
    #     source_url=''
    #     album_id='num'
    #     artist_id='num'
    # )
