import React, { useEffect } from 'react';
import { usePalette } from 'react-palette'
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link} from 'react-router-dom';

import * as albumActions from '../../../store/albums';
import * as trackActions from '../../../store/tracks';

import './AlbumView.css'

const AlbumView = () => {
    const dispatch = useDispatch();
    const { albumId } = useParams();
    const album = useSelector((state) => state.albums.allAlbums[albumId]);
    const artist = useSelector((state) => state.artists.allArtists[album.artist_id])
    const { data, loading, error } = usePalette(album.image_url)
    // need to bring in the state for the album list here

    useEffect(() => {
        dispatch(albumActions.thisAlbum(album))
        dispatch(trackActions.retrieveTracksByAlbum(album))
    })

    return (
        <div className='Root__album-view'>
            <main className='album-view-container'>
            <div className='album-view-container__scroll-node'>
                    <div className='album-view-container__padding'>
                        <div className='album-view-container__viewport'>
                            <div className='viewport-content' style={{padding: "0px"}, {height: "100%"}, {width: "100%"}}>
                                <div className='album-view-container__scroll-node-child'>
                                    <section className='album-page'>
                                        {/* <div className='ap-container'> */}
                                            <div className='contentSpacing'>
                                                <div style={{ backgroundColor: data.darkVibrant }} className='billboard-background' />
                                                <div className='billboard-background-gradient' />
                                                <div className='album-visuals-container'>
                                                    <div className='album-cover-container'>
                                                        <img className='album-cover' src={album.image_url} alt={`${album.album_title} Album Cover`} />
                                                    </div>
                                                </div>
                                                <div className='albumpage__album-info'>
                                                    <h2 className='page-type'>ALBUM</h2>
                                                    <span className='albumpage-albumtitle'>{album?.album_title}</span>
                                                    <div className='albumpage-albuminfo-container'>
                                                        <div className='albumpage-albuminfo'>
                                                            <figure className='albumpage-artistimg-container'>
                                                                <img className='albumpage-artistimg' src={artist.image_url} alt={`${artist.artist_name}'s profile pic`}/>
                                                            </figure>
                                                            <Link className='albumpage-artistname' to={`/artist/${artist.id}`}>
                                                                {artist.artist_name}
                                                            </Link>
                                                            <span className='albumpage-songnum'>
                                                                {/* length of album song array */}

                                                            </span>
                                                        </div>
                                                    </div>
                                                </div>
                                                {/* rest of songs go here */}
                                            </div>
                                        {/* </div> */}
                                    </section>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    )
}

export default AlbumView;
