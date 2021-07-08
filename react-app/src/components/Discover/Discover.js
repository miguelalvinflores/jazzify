import React from 'react';
import DiscoverNav from './DiscoverNav/DiscoverNav';
import DiscoverBar from './DiscoverBar/DiscoverBar';
import MainView from './MainView/MainView';
import './Discover.css'
// import { useSelector } from 'react-redux';
const Discover = () => {

    // const tracksQueue = useSelector((state) => state.tracks.trackQueue)

    return (
        <div id='main' >
            <div className='Root'>
                <div className='Root__top-container'>
                    <div className='disc-left-nav'>
                        <DiscoverNav />
                    </div>
                    <DiscoverBar/>
                    <MainView />
                </div>
            </div>
        </div>
    );
};
 export default Discover;
