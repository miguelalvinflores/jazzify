import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import * as albumActions from '../../../store/albums'

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
                            <div className='viewport-content'>
                                <div className='main-view-container__scroll-node-child'>
                                    <section className='home-page'>

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
