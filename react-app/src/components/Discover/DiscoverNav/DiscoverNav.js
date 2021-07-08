import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { Link, useLocation } from 'react-router-dom';
import logoText from '../../../images/logoText.png'
import './DiscoverNav.css'

const DiscoverNav = () => {
    const tracksQueue = useSelector((state) => state.tracks.trackQueue)
    const location = useLocation();

    const [isHome, setIsHome] = useState(false);

    useEffect(() => {
        let hometab = document.querySelector('.nav-home')
        if(location.pathname === '/discover') {
            setIsHome(true);
            hometab.classList.add('isHome')
        } else {
            setIsHome(false);
            hometab.classList.remove('isHome')
        }
    }, [ location.pathname ])

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
                            {isHome?(
                                <div className='home-icon-active'>
                                    <svg viewBox="0 0 512 512" width="24" height="24" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M448 463.746h-149.333v-149.333h-85.334v149.333h-149.333v-315.428l192-111.746 192 110.984v316.19z" fill="currentColor"></path>
                                    </svg>
                                </div>
                            ):(
                                <div className='home-icon'>
                                    <svg viewBox="0 0 512 512" width="24" height="24" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M 256.274 60.84 L 84.324 166.237 L 84.324 443.063 L 193.27 443.063 L 193.27 293.73 L 320.228 293.73 L 320.228 443.063 L 428.222 443.063 L 428.222 165.476 L 256.274 60.84 Z M 256.274 35.95 L 448.452 149.145 L 448.452 464.395 L 300 464.395 L 300 315.062 L 213.499 315.062 L 213.499 464.395 L 64.095 464.395 L 64.095 150.161 L 256.274 35.95 Z" fill="currentColor"></path>
                                    </svg>
                                </div>

                            )}
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
