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

    # track1 = Track(
    #     song_title="",
    #     image_url='https://ia800604.us.archive.org/21/items/78_boogie-woogie-music-vol.-2_meade-lux-lewis-shayne_gbia0003369/78_boogie-woogie-music-vol.-2_meade-lux-lewis-shayne_gbia0003369_itemimage.jpg',
    #     source_url='',
    #     album_id='7',
    #     artist_id='num',
    # )

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
