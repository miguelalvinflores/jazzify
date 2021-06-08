import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
// import { Link } from 'react-router-dom';

import AlbumDisplay from './AlbumDisplay/AlbumDisplay'
import * as albumActions from '../../../store/albums'

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
                                                        {Object.entries(albums).map((album) => {
                                                            return (
                                                                <div key={album[0]} >
                                                                    <AlbumDisplay album={album[1]} />
                                                                </div>
                                                            )
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
