from app.models import db, Track

def seed_tracks():
    track1 = Track(
        song_title="Mahogany Hall Stomp",
        image_url="https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg",
        source_url="https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/01%20-%20Mahogany%20Hall%20Stomp%20-%20Louis%20Armstrong%20And%20His%20Orchestra.mp3",
        album_id=1,
        artist_id=1,
    )

    track2 = Track(
        song_title='West End Blues',
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/02%20-%20West%20End%20Blues%20-%20Louis%20Armstrong%20And%20His%20Orchestra-Restored.mp3',
        album_id='1',
        artist_id='1',
    )

    track3 = Track(
        song_title='On the Sunny Side of the Street',
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/03%20-%20On%20the%20Sunny%20Side%20of%20t%20-%20Louis%20Armstrong%20And%20His%20Orchestra-Restored.mp3',
        album_id='1',
        artist_id='1',
    )

    track4 = Track(
        song_title='Satchel Mouth Swing',
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/04%20-%20Satchel%20Mouth%20Swing%20-%20Louis%20Armstrong%20And%20His%20Orchestra-Restored.mp3',
        album_id='1',
        artist_id='1',
    )

    track5 = Track(
        song_title="Struttin' with Some Barbecue",
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/05%20-%20Struttin%27%20with%20Some%20Barbecue%20-%20Louis%20Armstrong%20And%20His%20Orchestra.mp3',
        album_id='1',
        artist_id='1',
    )

    track6 = Track(
        song_title="Confessin' That I Love You",
        image_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/13/items/78_west-end-blues_louis-armstrong-and-his-orchestra-spencer-williams_gbia0031327/06%20-%20Confessin%27%20That%20I%20Love%20You%20-%20Louis%20Armstrong%20And%20His%20Orchcestra.mp3',
        album_id='1',
        artist_id='1',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)

    db.session.commit()


    track1 = Track(
        song_title="Delta Serenade",
        image_url='https://ia600607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362_itemimage.jpg',
        source_url='https://ia800607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/Delta%20Serenade%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='2',
        artist_id='2',
    )

    track2 = Track(
        song_title="Dusk",
        image_url='https://ia600607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362_itemimage.jpg',
        source_url='https://ia600607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/Dusk%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='2',
        artist_id='2',
    )

    track3 = Track(
        song_title="East St.Louis Toodle-oo",
        image_url='https://ia600607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362_itemimage.jpg',
        source_url='https://ia800607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/East%20St.%20Louis%20Toodle-oo%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='2',
        artist_id='2',
    )

    track4 = Track(
        song_title="Mood Indigo",
        image_url='https://ia600607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362_itemimage.jpg',
        source_url='https://ia800607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/Mood%20Indigo%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='2',
        artist_id='2',
    )

    track5 = Track(
        song_title="Ring Dem Bells",
        image_url='https://ia600607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362_itemimage.jpg',
        source_url='https://ia800607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/Ring%20Dem%20Bells%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='2',
        artist_id='2',
    )

    track6 = Track(
        song_title="Stompy Jones",
        image_url='https://ia600607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362_itemimage.jpg',
        source_url='https://ia800607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/Stompy%20Jones%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='2',
        artist_id='2',
    )

    track7 = Track(
        song_title="The Mooche",
        image_url='https://ia600607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362_itemimage.jpg',
        source_url='https://ia800607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/The%20Mooche%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='2',
        artist_id='2',
    )

    track8 = Track(
        song_title="Warm Valley",
        image_url='https://ia600607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362_itemimage.jpg',
        source_url='https://ia800607.us.archive.org/21/items/78_a-duke-ellington-panorama_duke-ellington-and-his-famous-orchestra-ellington-miley-d_gbia0003362/Warm%20Valley%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='2',
        artist_id='2',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()

    track1 = Track(
        song_title="Boo-Woo",
        image_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675_itemimage.jpg',
        source_url='https://ia801603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/01%20-%20Boo-Woo%20-%20Harry%20James%20and%20the%20Boogie%20Woogie%20Trio-restored.mp3',
        album_id='3',
        artist_id='3',
    )

    track2 = Track(
        song_title="Woo Woo",
        image_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675_itemimage.jpg',
        source_url='https://ia801603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/02%20-%20Woo%20Woo%20-%20Harry%20James%20and%20the%20Boogie%20Woogie%20Trio-restored.mp3',
        album_id='3',
        artist_id='3',
    )

    track3 = Track(
        song_title="Roll'Em Pete",
        image_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675_itemimage.jpg',
        source_url='https://ia801603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/03%20-%20Roll%20%27Em%20Pete%20-%20Joe%20Turner%20and%20Pete%20Johnson-restored.mp3',
        album_id='3',
        artist_id='3',
    )

    track4 = Track(
        song_title="Boogie Woogie",
        image_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675_itemimage.jpg',
        source_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/04%20-%20Boogie%20Woogie%20-%20Count%20Basie%27s%20Bue%20Five%20-%20Pinetop%20Smith-restored.mp3',
        album_id='3',
        artist_id='3',
    )

    track5 = Track(
        song_title="Boogie Woogie Prayer (Part One)",
        image_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675_itemimage.jpg',
        source_url='https://ia801603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/05%20-%20Boogie%20Woogie%20Prayer%20%28Part%20One%29%20-%20Meade%20Lux%20Lewis-restored.mp3',
        album_id='3',
        artist_id='3',
    )

    track6 = Track(
        song_title="Boogie Woogie Prayer (Part Two)",
        image_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675_itemimage.jpg',
        source_url='https://ia801603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/06%20-%20Boogie%20Woogie%20Prayer%20%28Part%20Two%29%20-%20Meade%20Lux%20Lewis-restored.mp3',
        album_id='3',
        artist_id='3',
    )

    track7 = Track(
        song_title="Shout For Joy",
        image_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675_itemimage.jpg',
        source_url='https://ia801603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/07%20-%20Shout%20For%20Joy%20-%20Albert%20Ammons%20-%20Ammons-restored.mp3',
        album_id='3',
        artist_id='3',
    )

    track8 = Track(
        song_title="Bear Cat Crawl",
        image_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675_itemimage.jpg',
        source_url='https://ia601603.us.archive.org/12/items/78_boogie-woogie_harry-james-and-the-boogie-woogie-trio-james-pete-johnson-eddie-dough_gbia0005675/08%20-%20Bear%20Cat%20Crawl%20-%20Meade%20Lux%20Lewis%20-%20Lewis-restored.mp3',
        album_id='3',
        artist_id='3',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()


    track1 = Track(
        song_title="I Can't Get Started",
        image_url='https://ia800108.us.archive.org/14/items/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/14/items/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202/03%20-%20I%20Can%27t%20Get%20Started%20-%20Billie%20Holiday%20and%20her%20Orchestra.mp3',
        album_id='4',
        artist_id='4',
    )

    track2 = Track(
        song_title="When a Woman Loves a Man",
        image_url='https://ia800108.us.archive.org/14/items/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/14/items/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202/04%20-%20When%20a%20Woman%20Loves%20a%20Man%20-%20Billie%20Holiday%20and%20her%20Orchestra-restored.mp3',
        album_id='4',
        artist_id='4',
    )

    track3 = Track(
        song_title="I've Got A Man",
        image_url='https://ia800108.us.archive.org/14/items/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/14/items/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202/05%20-%20%28I%27ve%20Got%20A%20Man%2C%20Crazy%20%20-%20Billie%20Holiday%20and%20her%20Orchestra.mp3',
        album_id='4',
        artist_id='4',
    )

    track4 = Track(
        song_title="A Sailboat in the Moonlight",
        image_url='https://ia800108.us.archive.org/14/items/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/14/items/78_when-a-woman-loves-a-man_billie-holiday-and-her-orchestra-billie-holiday-buck-clayt_gbia0031202/06%20-%20A%20Sailboat%20in%20the%20Moonlight%20-%20Billie%20Holiday%20and%20her%20Orchestra.mp3',
        album_id='4',
        artist_id='4',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)

    db.session.commit()

    track1 = Track(
        song_title="Tiger Rag",
        image_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403_itemimage.jpg',
        source_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/01%20-%20Tiger%20Rag%20-%20Louis%20Armstrong%20and%20his%20Orchestra.mp3',
        album_id='5',
        artist_id='1',
    )

    track2 = Track(
        song_title="St. Louis Blues",
        image_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403_itemimage.jpg',
        source_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/02%20-%20St.%20Louis%20Blues%20-%20Louis%20Armstrong%20and%20his%20Orchestra.mp3',
        album_id='5',
        artist_id='1',
    )

    track3 = Track(
        song_title="Song of the Vipers",
        image_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403_itemimage.jpg',
        source_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/03%20-%20Song%20of%20the%20Vipers%20-%20Louis%20Armstrong%20and%20his%20Orchestra.mp3',
        album_id='5',
        artist_id='1',
    )

    track4 = Track(
        song_title="Will You, Won't You Be My Babe",
        image_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403_itemimage.jpg',
        source_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/04%20-%20Will%20You%2C%20Won%27t%20You%20Be%20My%20Babe%20-%20Louis%20Armstrong%20and%20his%20Orchestra.mp3',
        album_id='5',
        artist_id='1',
    )

    track5 = Track(
        song_title="On the Sunny Side of the Street",
        image_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403_itemimage.jpg',
        source_url='https://ia801008.us.archive.org/10/items/78_st-louis-blues_louis-armstrong-and-his-orchestra-original-dixieland-jazz-band_gbia0039403/05%20-%20On%20the%20Sunny%20Side%20of%20t%20-%20Louis%20Armstrong%20and%20his%20Orchestra.mp3',
        album_id='5',
        artist_id='1',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)

    db.session.commit()

    track1 = Track(
        song_title="Royal Garden Blues",
        image_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273_itemimage.jpg',
        source_url='https://ia600601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/01%20-%20Royal%20Garden%20Blues%20-%20Duke%20Ellington%20and%20his%20Orchestra.mp3',
        album_id='6',
        artist_id='2',
    )

    track2 = Track(
        song_title="Frankie and Johnie",
        image_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273_itemimage.jpg',
        source_url='https://ia600601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/02%20-%20Frankie%20and%20Johnnie%20-%20Duke%20Ellington%20and%20his%20Rhythm.mp3',
        album_id='6',
        artist_id='2',
    )

    track3 = Track(
        song_title="Memphis Blues",
        image_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273_itemimage.jpg',
        source_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/03%20-%20Memphis%20Blues%20-%20Duke%20Ellignton%20and%20his%20Orchestra.mp3',
        album_id='6',
        artist_id='2',
    )

    track4 = Track(
        song_title="Pretty Woman",
        image_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273_itemimage.jpg',
        source_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/04%20-%20Pretty%20Woman%20-%20Duke%20Ellington%20and%20his%20Orchestra.mp3',
        album_id='6',
        artist_id='2',
    )

    track5 = Track(
        song_title="Beale Street Blues",
        image_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273_itemimage.jpg',
        source_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/05%20-%20Beale%20Street%20Blues%20-%20Duke%20Ellington%20and%20his%20Orchestra.mp3',
        album_id='6',
        artist_id='2',
    )

    track6 = Track(
        song_title="Transblucency",
        image_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273_itemimage.jpg',
        source_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/06%20-%20Transblucency%20%28A%20Blue%20F%20-%20Duke%20Ellington%20and%20his%20Orchestra.mp3',
        album_id='6',
        artist_id='2',
    )

    track7 = Track(
        song_title="St. Louis Blues",
        image_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273_itemimage.jpg',
        source_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/07%20-%20St.%20Louis%20Blues%20-%20Duke%20Ellington%20and%20his%20Orchestra.mp3',
        album_id='6',
        artist_id='2',
    )

    track8 = Track(
        song_title="Drawing Room Blues",
        image_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273_itemimage.jpg',
        source_url='https://ia800601.us.archive.org/20/items/78_frankie-and-johnnie_duke-ellington-and-his-orchestra-clarence-and-spencer-williams_gbia0020273/08%20-%20Drawing%20Room%20Blues%20-%20Duke%20Ellington%20and%20Billy%20Strayhorn.mp3',
        album_id='6',
        artist_id='2',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()

    track1 = Track(
        song_title="Easy Living",
        image_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368_itemimage.jpg',
        source_url='https://ia600605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/Easy%20Living%20-%20Teddy%20Wilson%20and%20his%20Orchestra-restored.mp3',
        album_id='7',
        artist_id='4',
    )

    track2 = Track(
        song_title="Foolin Myself",
        image_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/Foolin%27%20Myself%20-%20Teddy%20Wilson%20and%20his%20Orchestra.mp3',
        album_id='7',
        artist_id='4',
    )

    track3 = Track(
        song_title="I Must Have That Man!",
        image_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/I%20Must%20Have%20That%20Man%21%20-%20Teddy%20Wilson%20and%20his%20Orchestra-restored.mp3',
        album_id='7',
        artist_id='4',
    )

    track4 = Track(
        song_title="I Wished On the Moon",
        image_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/I%20Wished%20On%20The%20Moon%20-%20Teddy%20Wilson%20and%20his%20Orchestra-restored.mp3',
        album_id='7',
        artist_id='4',
    )

    track5 = Track(
        song_title="If You Were Mine",
        image_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/If%20You%20Were%20Mine%20-%20Teddy%20Wilson%20and%20his%20Orchestra-restored.mp3',
        album_id='7',
        artist_id='4',
    )

    track6 = Track(
        song_title="Miss Brown To You",
        image_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/Miss%20Brown%20To%20You%20-%20Teddy%20Wilson%20and%20his%20Orchestra-restored.mp3',
        album_id='7',
        artist_id='4',
    )

    track7 = Track(
        song_title="What A Little Moonlight Can Do",
        image_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/What%20A%20Little%20Moonlight%20Can%20Do%20-%20Teddy%20Wilson%20and%20his%20Orchestra-restored.mp3',
        album_id='7',
        artist_id='4',
    )

    track8 = Track(
        song_title="When You're Smiling (The Whole World Smiles With You)",
        image_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/14/items/78_teddy-wilson---billie-holiday_teddy-wilson-and-his-orchestra-billie-holiday-teddy-w_gbia0003368/When%20You%27re%20Smiling%20%28The%20%20-%20Teddy%20Wilson%20and%20his%20Orchestra.mp3',
        album_id='7',
        artist_id='4',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()

    track1 = Track(
        song_title="Sweet Lorraine",
        image_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215_itemimage.jpg',
        source_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/01%20-%20Sweet%20Lorraine%20-%20The%20King%20Cole%20Trio%20-%20King%20Cole.mp3',
        album_id='8',
        artist_id='6',
    )

    track2 = Track(
        song_title="Embraceable You",
        image_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215_itemimage.jpg',
        source_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/02%20-%20Embraceable%20You%20-%20The%20King%20Cole%20Trio%20-%20King%20Cole.mp3',
        album_id='8',
        artist_id='6',
    )

    track3 = Track(
        song_title="The Man I Love",
        image_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215_itemimage.jpg',
        source_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/03%20-%20The%20Man%20I%20Love%20-%20The%20King%20Cole%20Trio%20-%20George%20and%20Ira%20Gershwin.mp3',
        album_id='8',
        artist_id='6',
    )

    track4 = Track(
        song_title="Body and Soul",
        image_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215_itemimage.jpg',
        source_url='https://ia600105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/04%20-%20Body%20and%20Soul%20-%20The%20King%20Cole%20Trio%20-%20Green.mp3',
        album_id='8',
        artist_id='6',
    )

    track5 = Track(
        song_title="Prelude in C Sharp Minor",
        image_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215_itemimage.jpg',
        source_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/05%20-%20Prelude%20in%20C%20Sharp%20Minor%20-%20The%20King%20Cole%20Trio.mp3',
        album_id='8',
        artist_id='6',
    )

    track6 = Track(
        song_title="What Is This Thing Called Love?",
        image_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215_itemimage.jpg',
        source_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/06%20-%20What%20Is%20This%20Thing%20Called%20Love%3F%20-%20The%20King%20Cole%20Trio.mp3',
        album_id='8',
        artist_id='6',
    )

    track7 = Track(
        song_title="It's Only a Paper Moon",
        image_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215_itemimage.jpg',
        source_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/07%20-%20It%27s%20Only%20a%20Paper%20Moon%20-%20The%20King%20Cole%20Trio.mp3',
        album_id='8',
        artist_id='6',
    )

    track8 = Track(
        song_title="Easy Listening Blues",
        image_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215_itemimage.jpg',
        source_url='https://ia800105.us.archive.org/25/items/78_embraceable-you_the-king-cole-trio-king-cole-burwell-parish_gbia0031215/08%20-%20Easy%20Listening%20Blues%20-%20The%20King%20Cole%20Trio.mp3',
        album_id='8',
        artist_id='6',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()

    track1 = Track(
        song_title="I Don't Know Why",
        image_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357_itemimage.jpg',
        source_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/I%20Don%27t%20Know%20Why%20-%20The%20King%20Cole%20Trio%20-%20King%20Cole-restored.mp3',
        album_id='9',
        artist_id='6',
    )

    track2 = Track(
        song_title="I Know That You Know",
        image_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357_itemimage.jpg',
        source_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/I%20Know%20That%20You%20Know%20-%20The%20King%20Cole%20Trio-restored.mp3',
        album_id='9',
        artist_id='6',
    )

    track3 = Track(
        song_title="I'm In The Mood For Love",
        image_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357_itemimage.jpg',
        source_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/I%27m%20In%20The%20Mood%20For%20Love%20-%20The%20King%20Cole%20Trio-restored.mp3',
        album_id='9',
        artist_id='6',
    )

    track4 = Track(
        song_title="I'm Thru With Love",
        image_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357_itemimage.jpg',
        source_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/I%27m%20Thru%20With%20Love%20-%20The%20King%20Cole%20Trio%20-%20King%20Cole-restored.mp3',
        album_id='9',
        artist_id='6',
    )

    track5 = Track(
        song_title="Look What You've Done To Me",
        image_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357_itemimage.jpg',
        source_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/Look%20What%20You%27ve%20Done%20To%20Me%20-%20The%20King%20Cole%20Trio-restored.mp3',
        album_id='9',
        artist_id='6',
    )

    track6 = Track(
        song_title="This Way Out",
        image_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357_itemimage.jpg',
        source_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/This%20Way%20Out%20-%20The%20King%20Cole%20Trio%20-%20Nat%20Cole-restored.mp3',
        album_id='9',
        artist_id='6',
    )

    track7 = Track(
        song_title="To A Wild Rose",
        image_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357_itemimage.jpg',
        source_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/To%20A%20Wild%20Rose%20-%20The%20King%20Cole%20Trio%20-%20Edward%20MacDowell-restored.mp3',
        album_id='9',
        artist_id='6',
    )

    track8 = Track(
        song_title="What Can I Say After I Say I'm Sorry",
        image_url='https://ia800608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357_itemimage.jpg',
        source_url='https://ia600608.us.archive.org/33/items/78_king-cole-trio-vol.-2_the-king-cole-trio-nat-cole_gbia0003357/What%20Can%20I%20Say%20After%20I%20Say%20I%27m%20Sorry%20-%20The%20King%20Cole%20Trio-restored.mp3',
        album_id='9',
        artist_id='6',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()

    track1 = Track(
        song_title="Overture to a Jam Session - Part I",
        image_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398_itemimage.jpg',
        source_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/01%20-%20Overture%20to%20a%20Jam%20Sessi%20-%20Duke%20Ellington%20and%20his%20Orchestra-restored.mp3',
        album_id='10',
        artist_id='2',
    )

    track2 = Track(
        song_title="Overture to a Jam Session - Part II",
        image_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398_itemimage.jpg',
        source_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/02%20-%20Overture%20to%20a%20Jam%20Sessi%20-%20Duke%20Ellington%20and%20his%20Orchestra-restored.mp3',
        album_id='10',
        artist_id='2',
    )

    track3 = Track(
        song_title="Beautiful Indians (Hiawatha) - Part I",
        image_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398_itemimage.jpg',
        source_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/03%20-%20Beautiful%20Indians%20%28Hiaw%20-%20Duke%20Ellington%20and%20his%20Orchestra-restored.mp3',
        album_id='10',
        artist_id='2',
    )

    track4 = Track(
        song_title="Beautiful Indians (Minnehaha) - Part II",
        image_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398_itemimage.jpg',
        source_url='https://ia600107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/04%20-%20Beautiful%20Indians%20%28Minn%20-%20Duke%20Ellington%20and%20his%20Orchestra-restored.mp3',
        album_id='10',
        artist_id='2',
    )

    track5 = Track(
        song_title="Flippant Flurry",
        image_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398_itemimage.jpg',
        source_url='https://ia600107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/05%20-%20Flippant%20Flurry%20-%20Duke%20Ellington%20and%20his%20Orchestra-restored.mp3',
        album_id='10',
        artist_id='2',
    )

    track6 = Track(
        song_title="Golden Feather",
        image_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398_itemimage.jpg',
        source_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/06%20-%20Golden%20Feather%20-%20Duke%20Ellington%20and%20his%20Orchestra-restored.mp3',
        album_id='10',
        artist_id='2',
    )

    track7 = Track(
        song_title="Sultry Sunset",
        image_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398_itemimage.jpg',
        source_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/07%20-%20Sultry%20Sunset%20-%20Duke%20Ellington%20and%20his%20Orchestra-restored.mp3',
        album_id='10',
        artist_id='2',
    )

    track8 = Track(
        song_title="Jam-a-Ditty",
        image_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398_itemimage.jpg',
        source_url='https://ia800107.us.archive.org/30/items/78_overture-to-a-jam-session-part-2_duke-ellington-and-his-orchestra-strayhorn_gbia0039398/08%20-%20Jam-a-Ditty%20%28Concerto%20f%20-%20Duke%20Ellington%20and%20his%20Orchestra-restored.mp3',
        album_id='10',
        artist_id='2',
    )
    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()


    track1 = Track(
        song_title="Tough Truckin'",
        image_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027_itemimage.jpg',
        source_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/03%20-%20Tough%20Truckin%27%20-%20Duke%20Ellington%27s%20Sextet-restored.mp3',
        album_id='11',
        artist_id='2',
    )

    track2 = Track(
        song_title="Indigo Echoes",
        image_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027_itemimage.jpg',
        source_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/04%20-%20Indigo%20Echoes%20-%20Duke%20Ellington%27s%20Sextet%20-%20Ellington-restored.mp3',
        album_id='11',
        artist_id='2',
    )

    track3 = Track(
        song_title="Blue Mood",
        image_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027_itemimage.jpg',
        source_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/05%20-%20Blue%20Mood%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='11',
        artist_id='2',
    )

    track4 = Track(
        song_title="Delta Bound",
        image_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027_itemimage.jpg',
        source_url='https://ia600800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/06%20-%20Delta%20Bound%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='11',
        artist_id='2',
    )

    track5 = Track(
        song_title="Clouds In My Heart",
        image_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027_itemimage.jpg',
        source_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/07%20-%20Clouds%20in%20My%20Heart%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='11',
        artist_id='2',
    )

    track6 = Track(
        song_title="Slippery Horn",
        image_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027_itemimage.jpg',
        source_url='https://ia800800.us.archive.org/3/items/78_indigo-echoes_duke-ellingtons-sextet-ellington-mills-rex-stewart-johnny-hodges-har_gbia0020027/08%20-%20Slippery%20Horn%20-%20Duke%20Ellington%20and%20his%20Famous%20Orchestra-restored.mp3',
        album_id='11',
        artist_id='2',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)

    db.session.commit()

    track1 = Track(
        song_title="Gut Bucket Blues",
        image_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896_itemimage.jpg',
        source_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/01%20-%20Gut%20Bucket%20Blues%20-%20Louis%20Armstrong%20and%20his%20Hot%20Five-restored.mp3',
        album_id='12',
        artist_id='1',
    )
    track2 = Track(
        song_title="Yes! I'm in the Barrel",
        image_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896_itemimage.jpg',
        source_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/02%20-%20Yes%21%20I%27m%20in%20the%20Barrel%20-%20Louis%20Armstrong%20and%20his%20Hot%20Five-restored-restored.mp3',
        album_id='12',
        artist_id='1',
    )
    track3 = Track(
        song_title="Muskrat Ramble",
        image_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896_itemimage.jpg',
        source_url='https://ia600104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/03%20-%20Muskrat%20Ramble%20-%20Louis%20Armstrong%20and%20his%20Hot%20Five-restored.mp3',
        album_id='12',
        artist_id='1',
    )
    track4 = Track(
        song_title="Skid-Dat-De-Dat",
        image_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896_itemimage.jpg',
        source_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/04%20-%20Skid-Dat-De-Dat%20-%20Louis%20Armstrong%20and%20his%20Hot%20Five-restored.mp3',
        album_id='12',
        artist_id='1',
    )
    track5 = Track(
        song_title="Cornet Chop Suey",
        image_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896_itemimage.jpg',
        source_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/05%20-%20Cornet%20Chop%20Suey%20-%20Louis%20Armstrong%20and%20his%20Hot%20Five-retored.mp3',
        album_id='12',
        artist_id='1',
    )
    track6 = Track(
        song_title="My Heart",
        image_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896_itemimage.jpg',
        source_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/06%20-%20My%20Heart%20-%20Louis%20Armstrong%20and%20his%20Hot%20Five-restored.mp3',
        album_id='12',
        artist_id='1',
    )
    track7 = Track(
        song_title="You're Next",
        image_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896_itemimage.jpg',
        source_url='https://ia600104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/07%20-%20You%27re%20Next%20-%20Louis%20Armstrong%20and%20his%20Hot%20Five-restored.mp3',
        album_id='12',
        artist_id='1',
    )
    track8 = Track(
        song_title="Oriental Strut",
        image_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896_itemimage.jpg',
        source_url='https://ia800104.us.archive.org/29/items/78_yes-im-in-the-barrel_louis-armstrong-and-his-hot-five-louis-armstrong-and-kid-ory_gbia0022896/08%20-%20Oriental%20Strut%20-%20Louis%20Armstrong%20and%20his%20Hot%20Five-restored.mp3',
        album_id='12',
        artist_id='1',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()


    track1 = Track(
        song_title="I Can't Give You Anything but Love",
        image_url='https://ia902803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774_itemimage.jpg',
        source_url='https://ia802803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/01%20-%20I%20Can%27t%20Give%20You%20Anyth%20-%20Louis%20Armstrong%20and%20his%20Orchestra.mp3',
        album_id='13',
        artist_id='1',
    )

    track2 = Track(
        song_title="(What Did I Do To Be So) Black and Blue",
        image_url='https://ia902803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774_itemimage.jpg',
        source_url='https://ia802803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/02%20-%20%28What%20Did%20I%20Do%20To%20Be%20S%20-%20Louis%20Armstrong%20and%20his%20Orchestra.mp3',
        album_id='13',
        artist_id='1',
    )

    track3 = Track(
        song_title="Wrap Your Troubles in Dreams (And Dream Your Troubles Away)",
        image_url='https://ia902803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774_itemimage.jpg',
        source_url='https://ia802803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/03%20-%20Wrap%20Your%20Troubles%20in%20%20-%20Louis%20Armstrong%20and%20his%20Orchestra.mp3',
        album_id='13',
        artist_id='1',
    )

    track4 = Track(
        song_title="Star Dust",
        image_url='https://ia902803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774_itemimage.jpg',
        source_url='https://ia802803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/04%20-%20Star%20Dust%20-%20Louis%20Armstrong%20and%20his%20Orchestra.mp3',
        album_id='13',
        artist_id='1',
    )

    track5 = Track(
        song_title="Save It Pretty Mama",
        image_url='https://ia902803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774_itemimage.jpg',
        source_url='https://ia802803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/05%20-%20Save%20It%20Pretty%20Mama%20-%20Louis%20Armstrong%20and%20his%20Savoy%20Ballroom%20Five.mp3',
        album_id='13',
        artist_id='1',
    )

    track6 = Track(
        song_title="No One Else but You",
        image_url='https://ia902803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774_itemimage.jpg',
        source_url='https://ia802803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/06%20-%20No%20One%20Else%20but%20You%20-%20Louis%20Armstrong%20and%20his%20Savoy%20Ballroom%20Five.mp3',
        album_id='13',
        artist_id='1',
    )

    track7 = Track(
        song_title="Twelfth Street Rag",
        image_url='https://ia902803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774_itemimage.jpg',
        source_url='https://ia802803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/07%20-%20Twelfth%20Street%20Rag%20-%20Louis%20Armstrong%20and%20his%20Hot%20Seven.mp3',
        album_id='13',
        artist_id='1',
    )

    track8 = Track(
        song_title="Knockin' on a Jug",
        image_url='https://ia902803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774_itemimage.jpg',
        source_url='https://ia902803.us.archive.org/16/items/78_what-did-i-do-to-be-so-black-and-blue_louis-armstrong-and-his-orchestra-louis-arm_gbia0067774/08%20-%20Knockin%27%20on%20a%20Jug%20-%20Louis%20Armstrong%20and%20his%20Orchestra.mp3',
        album_id='13',
        artist_id='1',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()

    track1 = Track(
        song_title="Got No Blues",
        image_url='https://ia803101.us.archive.org/22/items/78_im-not-rough_louis-armstrong-and-his-hot-five-hardin-louis-armstrong-kid-ory-johnn_gbia0039399/78_im-not-rough_louis-armstrong-and-his-hot-five-hardin-louis-armstrong-kid-ory-johnn_gbia0039399_itemimage.jpg',
        source_url='https://ia803101.us.archive.org/22/items/78_im-not-rough_louis-armstrong-and-his-hot-five-hardin-louis-armstrong-kid-ory-johnn_gbia0039399/_%2205%20-%20Got%20No%20Blues%20-%20Louis%20Armstrong%20and%20his%20Hot%20Five.mp3',
        album_id='14',
        artist_id='1',
    )
    track2 = Track(
        song_title="I'm Not Rough",
        image_url='https://ia803101.us.archive.org/22/items/78_im-not-rough_louis-armstrong-and-his-hot-five-hardin-louis-armstrong-kid-ory-johnn_gbia0039399/78_im-not-rough_louis-armstrong-and-his-hot-five-hardin-louis-armstrong-kid-ory-johnn_gbia0039399_itemimage.jpg',
        source_url='https://ia803101.us.archive.org/22/items/78_im-not-rough_louis-armstrong-and-his-hot-five-hardin-louis-armstrong-kid-ory-johnn_gbia0039399/06%20-%20I%27m%20Not%20Rough%20-%20Louis%20Armstrong%20and%20his%20Hot%20Five-restored.mp3',
        album_id='14',
        artist_id='1',
    )

    db.session.add(track1)
    db.session.add(track2)

    db.session.commit()

    track1 = Track(
        song_title="Besame Mucho",
        image_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/Besame%20Mucho%20-%20Enric%20Madriguera%20and%20Orchestra.mp3',
        album_id='15',
        artist_id='7',
    )

    track2 = Track(
        song_title="Cae Cae",
        image_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/Cae%20Cae%20-%20Enric%20Madriguera%20and%20Orchestra.mp3',
        album_id='15',
        artist_id='7',
    )

    track3 = Track(
        song_title="Cansado",
        image_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/Cansado%20%28I%27m%20Tired%29%20-%20Enric%20Madriguera%20and%20Orchestra.mp3',
        album_id='15',
        artist_id='7',
    )

    track4 = Track(
        song_title="Chiu Chiu",
        image_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/Chiu%20Chiu%20-%20Enric%20Madriguera%20and%20Orchestra.mp3',
        album_id='15',
        artist_id='7',
    )

    track5 = Track(
        song_title="Come Tru-Cu-Tu",
        image_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/Come%20Tru-Cu-Tu%20-%20Enric%20Madriguera%20and%20Orchestra.mp3',
        album_id='15',
        artist_id='7',
    )

    track6 = Track(
        song_title="I'm Living From Kiss to Kiss",
        image_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/I%27m%20Living%20From%20Kiss%20to%20Kiss%20-%20Enric%20Madriguera%20and%20Orchestra.mp3',
        album_id='15',
        artist_id='7',
    )

    track7 = Track(
        song_title="Llumbele",
        image_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/Llumbele%20-%20Enric%20Madriguera%20and%20Orchestra-restored.mp3',
        album_id='15',
        artist_id='7',
    )

    track8 = Track(
        song_title="Os Quindis De Yaya",
        image_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363_itemimage.jpg',
        source_url='https://ia800605.us.archive.org/17/items/78_music-of-latin-america_enric-madriguera-and-orchestra-marcelino-guerra_gbia0002363/Os%20Quindis%20De%20Yaya%20-%20Enric%20Madriguera%20and%20Orchestra.mp3',
        album_id='15',
        artist_id='7',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()

    track1 = Track(
        song_title="Honeysuckle Rose",
        image_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100_itemimage.jpg',
        source_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/01%20-%20Honeysuckle%20Rose%20-%20%22Fats%22%20Waller%20-%20Thomas%20%22Fats%22%20Waller.mp3',
        album_id='16',
        artist_id='8',
    )

    track2 = Track(
        song_title="Your Feet's Too Big",
        image_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100_itemimage.jpg',
        source_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/02%20-%20Your%20Feet%27s%20Too%20Big%20-%20%22Fats%22%20Waller%20and%20his%20Rhythm.mp3',
        album_id='16',
        artist_id='8',
    )

    track3 = Track(
        song_title="Ain't Misbehavin'",
        image_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100_itemimage.jpg',
        source_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/03%20-%20Ain%27t%20Misbehavin%27%20-%20%22Fats%22%20Waller%20-%20Razaf.mp3',
        album_id='16',
        artist_id='8',
    )

    track4 = Track(
        song_title="Hold Tight (Want Some Seafood Mama)",
        image_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100_itemimage.jpg',
        source_url='https://ia600907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/04%20-%20Hold%20Tight%20%28Want%20Some%20Seafo%20-%20%22Fats%22%20Waller%20and%20his%20Rhythm.mp3',
        album_id='16',
        artist_id='8',
    )

    track5 = Track(
        song_title="I Can't Give You Anything but Love, Baby",
        image_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100_itemimage.jpg',
        source_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/05%20-%20I%20Can%27t%20Give%20You%20Anything%20b%20-%20%22Fats%22%20Waller%20and%20his%20Rhythm.mp3',
        album_id='16',
        artist_id='8',
    )

    track6 = Track(
        song_title="The Joint is Jumpin'",
        image_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100_itemimage.jpg',
        source_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/06%20-%20The%20Joint%20Is%20Jumpin%27%20-%20%22Fats%22%20Waller%20and%20his%20Rhythm.mp3',
        album_id='16',
        artist_id='8',
    )

    track7 = Track(
        song_title="Two Sleepy People",
        image_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100_itemimage.jpg',
        source_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/07%20-%20Two%20Sleepy%20People%20-%20%22Fats%22%20Waller%20and%20his%20Rhythm.mp3',
        album_id='16',
        artist_id='8',
    )

    track8 = Track(
        song_title="The Minor Drag",
        image_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100_itemimage.jpg',
        source_url='https://ia800907.us.archive.org/16/items/78_your-feets-too-big_fats-waller-thomas-fats-waller-bach-beethoven-brahams-walle_gbia0092100/08%20-%20The%20Minor%20Drag%20-%20%22Fats%22%20Waller%20and%20his%20Buddies.mp3',
        album_id='16',
        artist_id='8',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)
    db.session.add(track7)
    db.session.add(track8)

    db.session.commit()

    track1 = Track(
        song_title="Makin' Whoopee",
        image_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699_itemimage.jpg',
        source_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/01%20-%20MAKIN%27%20WHOOPEE%20-%20THE%20KING%20COLE%20TRIO%20-%20King%20Cole.mp3',
        album_id='17',
        artist_id='6',
    )

    track2 = Track(
        song_title="Too Marvelous For Words",
        image_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699_itemimage.jpg',
        source_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/02%20-%20TOO%20MARVELOUS%20FOR%20WORDS%20-%20THE%20KING%20COLE%20TRIO.mp3',
        album_id='17',
        artist_id='6',
    )

    track3 = Track(
        song_title="Honeysuckle Rose",
        image_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699_itemimage.jpg',
        source_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/03%20-%20HONEYSUCKLE%20ROSE%20-%20THE%20KING%20COLE%20TRIO%20-%20Thomas%20Waller.mp3',
        album_id='17',
        artist_id='6',
    )

    track4 = Track(
        song_title="I'll String Along with You",
        image_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699_itemimage.jpg',
        source_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/04%20-%20I%27LL%20STRING%20ALONG%20WITH%20YOU%20-%20THE%20KING%20COLE%20TRIO.mp3',
        album_id='17',
        artist_id='6',
    )

    track5 = Track(
        song_title="Rhumba Azul",
        image_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699_itemimage.jpg',
        source_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/05%20-%20RHUMBA%20AZUL%20-%20THE%20KING%20COLE%20TRIO%20-%20Nat%20Cole.mp3',
        album_id='17',
        artist_id='6',
    )

    track6 = Track(
        song_title="This is My Night To Dream",
        image_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699_itemimage.jpg',
        source_url='https://ia803207.us.archive.org/1/items/78_too-marvelous-for-words_the-king-cole-trio-king-cole-walter-donaldson-gus-kahn_gbia8000699/06%20-%20THIS%20IS%20MY%20NIGHT%20TO%20DREAM%20-%20THE%20KING%20COLE%20TRIO.mp3',
        album_id='17',
        artist_id='6',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)

    db.session.commit()

    track1 = Track(
        song_title="Bop-Kick",
        image_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263_itemimage.jpg',
        source_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/01%20-%20Bop-Kick%20-%20Nat%20%28King%29%20Cole%20And%20The%20Trio%20-%20King%20Cole.mp3',
        album_id='18',
        artist_id='6',
    )

    track2 = Track(
        song_title="I Used to Love You",
        image_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263_itemimage.jpg',
        source_url='https://ia601604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/02%20-%20I%20Used%20to%20Love%20You%20%28But%20It%27%20-%20Nat%20%28King%29%20Cole%20And%20The%20Trio.mp3',
        album_id='18',
        artist_id='6',
    )

    track3 = Track(
        song_title="Tis' Autumn",
        image_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263_itemimage.jpg',
        source_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/03%20-%20%27Tis%20Autumn%20-%20King%20Cole%20And%20His%20Trio%20-%20King%20Cole.mp3',
        album_id='18',
        artist_id='6',
    )

    track4 = Track(
        song_title="Yes Sir, That's My Baby",
        image_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263_itemimage.jpg',
        source_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/04%20-%20Yes%20Sir%2C%20That%27s%20My%20Baby%20-%20King%20Cole%20And%20His%20Trio.mp3',
        album_id='18',
        artist_id='6',
    )

    track5 = Track(
        song_title="Laugh! Cool Clown",
        image_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263_itemimage.jpg',
        source_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/05%20-%20Laugh%21%20Cool%20Clown%20-%20Nat%20%28King%29%20Cole%20And%20The%20Trio.mp3',
        album_id='18',
        artist_id='6',
    )

    track6 = Track(
        song_title="For All We Know",
        image_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263_itemimage.jpg',
        source_url='https://ia801604.us.archive.org/32/items/78_i-used-to-love-you-but-its-all-over-now_nat-king-cole-and-the-trio-king-cole-i_gbia0067263/06%20-%20For%20All%20We%20Know%20-%20Nat%20%28King%29%20Cole%20And%20The%20Trio.mp3',
        album_id='18',
        artist_id='6',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)

    db.session.commit()

    track1 = Track(
        song_title="Rockin' Chair",
        image_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/01%20-%20Rockin%27%20Chair%20-%20%22Fats%22%20Waller%20-%20Hoagy%20Carmichael.mp3',
        album_id='19',
        artist_id='8',
    )

    track2 = Track(
        song_title="Georgia on My Mind",
        image_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/02%20-%20Georgia%20on%20My%20Mind%20-%20%22Fats%22%20Waller%20-%20Hoagy%20Carmichael.mp3',
        album_id='19',
        artist_id='8',
    )

    track3 = Track(
        song_title="Tea For Two",
        image_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/03%20-%20Tea%20For%20Two%20-%20%22Fats%22%20Waller%20-%20Irving%20Caesar.mp3',
        album_id='19',
        artist_id='8',
    )

    track4 = Track(
        song_title="I Ain't Got Nobody (And Nobody Cares for Me)",
        image_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/04%20-%20I%20Ain%27t%20Got%20Nobody%20%28And%20Nobody%20Cares%20for%20M%20-%20%22Fats%22%20Waller.mp3',
        album_id='19',
        artist_id='8',
    )

    track5 = Track(
        song_title="Basin Street Blues",
        image_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/05%20-%20Basin%20Street%20Blues%20-%20%22Fats%22%20Waller%20-%20Spencer%20Williams.mp3',
        album_id='19',
        artist_id='8',
    )

    track6 = Track(
        song_title="Keepin' Out of Mischief Now",
        image_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986_itemimage.jpg',
        source_url='https://ia800108.us.archive.org/2/items/78_georgia-on-my-mind_fats-waller-hoagy-carmichael_gbia0031986/06%20-%20Keepin%27%20out%20of%20Mischief%20Now%20-%20%22Fats%22%20Waller.mp3',
        album_id='19',
        artist_id='8',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)

    db.session.commit()

    track1 = Track(
        song_title="Swing Low Sweet Chariot",
        image_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640_itemimage.jpg',
        source_url='https://ia902801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/01%20-%20Swing%20Low%20Sweet%20Chariot%20-%20%22Fats%22%20Waller%20-%20Waller.mp3',
        album_id='20',
        artist_id='8',
    )
    track2 = Track(
        song_title="Go Down Moses",
        image_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640_itemimage.jpg',
        source_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/02%20-%20Go%20Down%20Moses%20%28Let%20My%20People%20Go%29%20-%20%22Fats%22%20Waller.mp3',
        album_id='20',
        artist_id='8',
    )
    track3 = Track(
        song_title="Deep River",
        image_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640_itemimage.jpg',
        source_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/03%20-%20Deep%20River%20-%20%22Fats%22%20Waller%20-%20Waller.mp3',
        album_id='20',
        artist_id='8',
    )
    track4 = Track(
        song_title="Lonesome Road",
        image_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640_itemimage.jpg',
        source_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/04%20-%20Lonesome%20Road%20-%20%22Fats%22%20Waller%20-%20G.%20Austin.mp3',
        album_id='20',
        artist_id='8',
    )
    track5 = Track(
        song_title="Water Boy",
        image_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640_itemimage.jpg',
        source_url='https://ia902801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/05%20-%20Water%20Boy%20-%20%22Fats%22%20Waller%20-%20Avery%20Robinson.mp3',
        album_id='20',
        artist_id='8',
    )
    track6 = Track(
        song_title="All God's Chillun Got Wings",
        image_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640_itemimage.jpg',
        source_url='https://ia802801.us.archive.org/16/items/78_go-down-moses-let-my-people-go_fats-waller-waller_gbia0067640/06%20-%20All%20God%27s%20Chillun%20Got%20Wings%20-%20%22Fats%22%20Waller.mp3',
        album_id='20',
        artist_id='8',
    )

    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.add(track5)
    db.session.add(track6)

    db.session.commit()

    track1 = Track(
        song_title="",
        image_url='https://ia903109.us.archive.org/31/items/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014_itemimage.jpg',
        source_url='',
        album_id='21',
        artist_id='8',
    )
    track2 = Track(
        song_title="",
        image_url='https://ia903109.us.archive.org/31/items/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014_itemimage.jpg',
        source_url='',
        album_id='21',
        artist_id='8',
    )
    track3 = Track(
        song_title="",
        image_url='https://ia903109.us.archive.org/31/items/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014_itemimage.jpg',
        source_url='',
        album_id='21',
        artist_id='8',
    )
    track4 = Track(
        song_title="",
        image_url='https://ia903109.us.archive.org/31/items/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014_itemimage.jpg',
        source_url='',
        album_id='21',
        artist_id='8',
    )
    track5 = Track(
        song_title="",
        image_url='https://ia903109.us.archive.org/31/items/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014_itemimage.jpg',
        source_url='',
        album_id='21',
        artist_id='8',
    )
    track6 = Track(
        song_title="",
        image_url='https://ia903109.us.archive.org/31/items/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014/78_whitechapel_ted-heath-his-music-fats-waller_gbia0072014_itemimage.jpg',
        source_url='',
        album_id='21',
        artist_id='8',
    )


    # track3 = Track(
    #     song_title="",
    #     image_url='',
    #     source_url='',
    #     album_id='num',
    #     artist_id='num',
    # )

def undo_tracks():
    db.session.execute('TRUNCATE tracks RESTART IDENTITY CASCADE;')
    db.session.commit()
