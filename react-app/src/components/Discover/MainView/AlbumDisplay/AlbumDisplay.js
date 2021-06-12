import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import * as albumActions from '../../../../store/albums'
import * as trackActions from '../../../../store/tracks'

import './AlbumDisplay.css'
function AlbumDisplay({album}) {
    // console.log('ALBUM', album)
    const dispatch = useDispatch();
    const currentAlbum = useSelector((state) => state.albums.album)

    const artists = useSelector((state) => state.artists.allArtists)
    // const albumTracksList = useSelector((state) => state.tracks.albumTracks)
    const albumTracks = useSelector((state) => state.tracks.albumTracks[currentAlbum.album_title])
    const playAlbum = () => {
        // console.log('PLAY ALBUM', album)
        dispatch(albumActions.thisAlbum(album))
        // console.log("ALBUM TRACK LIST", albumTracksList)
        dispatch(trackActions.retrieveTracksByAlbum(album))

    };

    useEffect(() => {

            dispatch(trackActions.playAlbum(albumTracks))

    }, [dispatch, albumTracks])

    return(
        <div className='album-container'>
            <div className='album-content'>
                <div className='album-visual-container'>
                    <div className='album-image-container'>
                        <img className='album-img' src={album.image_url} alt={`${album.album_title} Album Cover`} />
                    </div>
                    <div className='album-play-btn-container'>
                        <button className='album-play-btn' onClick={playAlbum}>
                            <svg height="16" role="img" width="16" viewBox="0 0 24 24" aria-hidden="true">
                                <polygon points="21.57 12 5.98 3 5.98 21 21.57 12" fill="currentColor"></polygon>
                            </svg>
                        </button>
                    </div>
                </div>
                <div className='album-text-container'>
                    <Link className='album-text-link' to={`albums/${album.id}`} >
                        <div className='album-text-title'>
                            {album.album_title}
                        </div>
                    </Link>
                    <div className='album-text-artist'>
                        <span>{artists[album.artist_id]?.artist_name}</span>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default AlbumDisplay;
