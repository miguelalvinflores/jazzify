import React from 'react';
import DiscoverNav from './DiscoverNav/DiscoverNav';
import PlayingBar from './PlayingBar/PlayingBar';
import MainView from './MainView/MainView';
import './Discover.css'
import { useSelector } from 'react-redux';
const Discover = () => {

    const tracksQueue = useSelector((state) => state.tracks.trackQueue)

    return (
        <div id='main' >
            <div className='Root'>
                <div className='Root__top-container'>
                    <div className='disc-left-nav'>
                        <DiscoverNav />
                    </div>
                    {tracksQueue && (
                        <PlayingBar
                        tracksQueue={tracksQueue} />
                    )}
                    <MainView />
                </div>
            </div>
        </div>
    );
};
 export default Discover;
