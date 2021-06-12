import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
// import { Link } from 'react-router-dom';

import AlbumDisplay from './AlbumDisplay/AlbumDisplay'
import * as albumActions from '../../../store/albums'
import * as artistActions from '../../../store/artists'

import './MainView.css'

const MainView = () => {
    const dispatch = useDispatch();
    const user = useSelector((state) => state.session.user);
    const albums = useSelector((state) => state.albums.allAlbums);

    useEffect(() => {
        // console.log('in USE EFFECT OF MAINVIEW')
        if (user) {
            // console.log('in IF of USE EFFECT')
            dispatch(albumActions.retrieveAlbums());
            dispatch(artistActions.retrieveArtists());
        }
    }, [dispatch, user])
    return (
        <div className='Root__main-view'>
            <main className='main-view-container'>
                <div className='main-view-container__scroll-node'>
                    <div className='main-view-container__padding'>
                        <div className='main-view-container__viewport'>
                            <div className='viewport-content' style={{padding: "0px"}, {height: "100%"}, {width: "100%"}}>
                                <div className='main-view-container__scroll-node-child'>
                                    <section className='home-page'>
                                        <div className='hp-container'>
                                            <div className='content-spacing'>
                                                <section className='recommended-section'>
                                                    <div className='sec-header'>
                                                        <div className='sec-header-container'>
                                                            <div className='sec-header__title-container'>
                                                                <h2 className='sec-header__title'>
                                                                    Recommended for You
                                                                </h2>
                                                            </div>

                                                        </div>
                                                    </div>
                                                    <div className='sec-content' style={ {  } }>
                                                        {Object.entries(albums).map((album, index) => {
                                                            return ((((index > 1) && (index < 4)) || (index === 6) || ((index > 13) && (index < 16))) && (
                                                                <div key={album[0]} >
                                                                    <AlbumDisplay album={album[1]} />
                                                                </div>
                                                            ))
                                                        })}
                                                    </div>
                                                </section>
                                                <section>
                                                    <div className='sec-header'>
                                                        <div className='sec-header-container'>
                                                            <div className='sec-header__title-container'>
                                                                <h2 className='sec-header__title'>
                                                                    For Fans of L. Armstrong
                                                                </h2>
                                                            </div>

                                                        </div>
                                                    </div>
                                                    <div className='sec-content' style={ {  } }>
                                                        {Object.entries(albums).map((album, index) => {
                                                            return ((album[1].artist_id === 1) && (
                                                                <div key={album[0]} >
                                                                    <AlbumDisplay album={album[1]} />
                                                                </div>
                                                            ))
                                                        })}
                                                    </div>
                                                </section>
                                                <section>
                                                    <div className='sec-header'>
                                                        <div className='sec-header-container'>
                                                            <div className='sec-header__title-container'>
                                                                <h2 className='sec-header__title'>
                                                                    For Fans of the Duke
                                                                </h2>
                                                            </div>

                                                        </div>
                                                    </div>
                                                    <div className='sec-content' style={ {  } }>
                                                        {Object.entries(albums).map((album, index) => {
                                                            return ((album[1].artist_id === 2) && (
                                                                <div key={album[0]} >
                                                                    <AlbumDisplay album={album[1]} />
                                                                </div>
                                                            ))
                                                        })}
                                                    </div>
                                                </section>
                                                <section>
                                                    <div className='sec-header'>
                                                        <div className='sec-header-container'>
                                                            <div className='sec-header__title-container'>
                                                                <h2 className='sec-header__title'>
                                                                    Other great Classics
                                                                </h2>
                                                            </div>

                                                        </div>
                                                    </div>
                                                    <div className='sec-content' style={ {  } }>
                                                        {Object.entries(albums).map((album, index) => {
                                                            return ((((index > 15) && (album[1].artist_id !== 2)) && ((album[1].id !== 20) && ((album[1].artist_id !== 1)) || ( album[1].id === 22))) && (
                                                                <div key={album[0]} >
                                                                    <AlbumDisplay album={album[1]} />
                                                                </div>
                                                            ))
                                                        })}
                                                    </div>
                                                </section>
                                            </div>
                                        </div>
                                    </section>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
}

export default MainView;
