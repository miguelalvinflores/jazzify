import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import * as albumActions from '../../../../store/albums'

import './AlbumDisplay.css'
function AlbumDisplay({album}) {
    // console.log('ALBUM', album)
    const dispatch = useDispatch();
    const currentAlbum = useSelector((state) => state.albums.album)

    const playAlbum = () => {
        console.log('PLAY ALBUM', album)
        dispatch(albumActions.thisAlbum(album))
    };

    if(currentAlbum) {

    }

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
            </div>
        </div>
    )
}

export default AlbumDisplay;
