import React from 'react';
import { Link } from 'react-router-dom';
import logoText from '../../../images/logoText.png'
import './DiscoverNav.css'

const DiscoverNav = () => {
    return (
        <nav className='Root__nav-bar'>
            <div className='nav-bar__container'>
                <div className='logo-container'>
                    <Link to='/' className='disc-logo-link' >
                        <img src={logoText} alt='Jazzify logo' />
                    </Link>
                </div>
                <ul className='navigation container' >
                    <li className='nav-home'>
                        <Link to='/'>
                            <div className='home-icon'>

                            </div>
                            <div className='home-icon-active'>

                            </div>
                            <span className='home-nav-text'>
                                Home
                            </span>
                        </Link>
                    </li>
                    {/* SPACE HERE FOR OTHER FEATURE IN THE FUTURE
                        (SEARCH, PLAYLISTS, ETC) */}
                </ul>
                <div className='playlists-container'>
                    {/* SPACE HERE FOR PLAYLIST CREATION BUTTON
                        AND LIST OF PLAYLISTS */}
                </div>
            </div>
        </nav>
    );
};

export default DiscoverNav;
