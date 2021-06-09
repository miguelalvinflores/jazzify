import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import './PlayingBar.css'



const PlayingBar = () => {
    const album = useSelector((state) => state.albums.album )
    return (
        <div className='Root__now-playing-bar'>
            <footer className='play-footer'>
                <div className='playing-container' >
                    <div className='playing-track-info-container'>
                        <div className='playing-track-info'>
                            <div className='playing-track-img-container'>
                                <Link to={`/albums/${album.id}`} className='playing-track-img-link' >
                                    <div className='playing-album-img-container'>
                                        <div className='playing-album-cover-art'>
                                            <img className='playing-album-img' src={album.image_url} alt={`${album.album_title} Album Cover`} />
                                        </div>
                                    </div>
                                </Link>
                            </div>
                        </div>

                    </div>
                </div>
            </footer>
        </div>
    );
};

export default PlayingBar;
