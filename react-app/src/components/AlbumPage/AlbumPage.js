import React from 'react';
import DiscoverNav from '../Discover/DiscoverNav/DiscoverNav';
import DiscoverBar from '../Discover/DiscoverBar/DiscoverBar';
import './AlbumPage.css'
const AlbumPage = () => {
    return (
        <div id='main'>
            <div className='Root'>
                <div className='Root_top-container'>
                    <div className='disc-left-nav'>
                        <DiscoverNav />
                    </div>
                    <DiscoverBar />
                </div>
            </div>

        </div>
    );
};

export default AlbumPage;
