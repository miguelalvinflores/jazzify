import React, { useState } from 'react';
import { useSelector } from 'react-redux';

import './DiscoverBar.css'
import LogoutButton from '../../auth/LogoutButton'


const DiscoverBar = () => {

    const username = useSelector((state) => state.session.user.username)

    const [ profileShowing, setProfileShowing ] = useState(false);


    const profileBtnClick = ( () => {
        if (profileShowing) {
            setProfileShowing(false);
        } else {
            setProfileShowing(true)
        }
    })

    let arrowSvg = ''

    if (profileShowing) {
        arrowSvg = (
            <svg role="img" height="16" width="16" className="profile-arrow-svg" viewBox="0 0 16 16">
                <path d="M13 10L8 4.206 3 10z"></path>
            </svg>
        )
    } else {
        arrowSvg =(
            <svg role="img" height="16" width="16" className="profile-arrow-svg" viewBox="0 0 16 16">
                <path d="M3 6l5 5.794L13 6z"></path>
            </svg>
        )
    }


    return (
        <div className='Root__top-bar'>
            <header className='bar__header'>
                <div className='bar__header-background-container'>
                    <div className='bar__header-background'></div>
                </div>

                {/* <div className='arrow-btn-container'>
                    <button id='top-bar-back-btn'></button>
                    <button id='top-bar-forward-btn'></button>
                </div> */}

                <button
                    className='profile-container-btn'
                    onClick={profileBtnClick}
                >
                    <span className='profile-username'>
                        {username}
                    </span>
                    {arrowSvg}
                </button>
                    {(profileShowing) && (
                        <div

                        className='profile-container'>
                            <LogoutButton profileBtnClick={profileBtnClick} />
                        </div>
                    )}
            </header>
        </div>
    );
};
export default DiscoverBar;
