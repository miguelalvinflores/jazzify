import React from 'react';
import './AlbumDisplay.css'
function AlbumDisplay({album}) {
    // console.log('ALBUM', album)
    return(
        <div className='album-container'>
            <div className='album-content'>
                <div className='album-visual-container'>
                    <div className='album-image-container'>
                        <img className='album-img' src={album.image_url} alt={`${album.album_title} Album Cover`} />
                    </div>
                </div>
            </div>
        </div>
    )
}

export default AlbumDisplay;
