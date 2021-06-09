import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import './PlayingBar.css'



const PlayingBar = () => {
    const album = useSelector((state) => state.albums.album )
    const artists = useSelector((state => state.artists.allArtists))
    const tracksQueue = useSelector((state) => state.tracks.trackQueue)
    const track = tracksQueue? tracksQueue[0] : undefined;
    // console.log('TRACK', track)
    return (
        <div className='Root__now-playing-bar'>
            {(track && (
                <footer className='play-footer'>
                    <div className='playing-container' >
                        <div className='playing-track-info-container'>
                            <div className='playing-track-info'>
                                <div className='playing-track-img-container'>
                                    <Link to={`/albums/${track?.album_id}`} className='playing-track-img-link' >
                                        <div className='playing-album-img-container'>
                                            <div className='playing-album-cover-art'>
                                                <img className='playing-album-img' src={track?.image_url} alt={`${album.album_title} Album Cover`} />
                                            </div>
                                        </div>
                                    </Link>
                                </div>
                                <div className='playing-track-text-container'>
                                    <div className='playing-track-title'>
                                        <span>
                                            <Link to={`/albums/${track?.album_id}`} className='playing-track-title-link'>
                                                {track?.song_title}
                                            </Link>
                                        </span>
                                    </div>
                                    <div className='playing-track-artist'>
                                        <span>
                                            <span>
                                                {artists[track?.artist_id]?.artist_name}
                                            </span>
                                        </span>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>
                </footer>
            ))};
        </div>
    );
};

export default PlayingBar;
