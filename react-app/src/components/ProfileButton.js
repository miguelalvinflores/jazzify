import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import LogoutButton from './auth/LogoutButton';


const ProfileButton = ({ user }) => {

    const[showMenu, setShowMenu] = useState(false);

    const openMenu = () => {
        if (showMenu) return;
        setShowMenu(true);
    };

    const closeMenu = () => {
        if (!showMenu) return;
        setShowMenu(false);
    };

    useEffect(() => {
        if (!showMenu) return;

        document.addEventListener('click', closeMenu);

        return () => document.removeEventListener('click', closeMenu);
    }, [ showMenu ]);


    return (
        <div className='profile-container' onMouseEnter={openMenu} onMouseLeave={closeMenu}>
            <div className='profile-btn' >
                <h1>P</h1>
            </div>
            {showMenu && (
                <>
                <img className='triangle-dropdown' src='images/nav-triangle.png' alt='dropdown traingle'/>
                <ul className='profile-dropdown' >
                    <hr/>
                    <LogoutButton />
                </ul>
                </>
            )}
        </div>
    )
};

export default ProfileButton;
