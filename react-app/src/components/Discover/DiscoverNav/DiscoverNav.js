import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import logoText from '../../../images/logoText.png'
import './DiscoverNav.css'

const DiscoverNav = () => {
    const tracksQueue = useSelector((state) => state.tracks.trackQueue)
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
                        <Link className='nav-link' to='/'>
                            <div className='home-icon'>

                            </div>
                            <div className='home-icon-active'>
                                <svg viewBox="0 0 512 512" width="24" height="24" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M448 463.746h-149.333v-149.333h-85.334v149.333h-149.333v-315.428l192-111.746 192 110.984v316.19z" fill="currentColor"></path>
                                </svg>
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
                <div className={tracksQueue? 'bio-links bio-links-main bio-links-up' : 'bio-links bio-links-main'}>
                    <div className="github-bio">
                        <a href="https://github.com/miguelalvinflores">
                            <i className="fab fa-github fa-3x"></i>
                        </a>
                    </div>
                    <div className="linkedIn-bio">
                        <a href="https://www.linkedin.com/in/miguelalvinflores/">
                            <i className="fab fa-linkedin-in fa-3x"></i>
                        </a>
                    </div>
                    <div className="AngelList-bio">
                        <a href="https://angel.co/u/miguel-flores-22">
                            <i className="fab fa-angellist fa-3x"></i>
                        </a>
                    </div>
                </div>
            </div>
        </nav>
    );
};

export default DiscoverNav;
