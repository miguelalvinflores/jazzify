import React from 'react';
import ResizePanel from "react-resize-panel";
import DiscoverNav from '../Discover/DiscoverNav/DiscoverNav';
import './Discover.css'
const Discover = () => {

    return (
        <div id='main' >
            <div className='Root'>
                <div className='Root__top-container'>
                    <ResizePanel direction='e'>
                        <DiscoverNav />
                    </ResizePanel>
                </div>
            </div>
        </div>
    );
};
 export default Discover;
