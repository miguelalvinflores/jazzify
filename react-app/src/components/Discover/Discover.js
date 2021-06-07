import React from 'react';
import ResizePanel from "react-resize-panel";
import DiscoverNav from './DiscoverNav/DiscoverNav';
import PlayingBar from './PlayingBar/PlayingBar';
import MainView from './MainView/MainView';
import './Discover.css'
const Discover = () => {

    return (
        <div id='main' >
            <div className='Root'>
                <div className='Root__top-container'>
                    <ResizePanel direction='e'>
                        <DiscoverNav />
                    </ResizePanel>
                    <PlayingBar />
                    <MainView />
                </div>
            </div>
        </div>
    );
};
 export default Discover;
