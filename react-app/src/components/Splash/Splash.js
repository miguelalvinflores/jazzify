import React from 'react';
import { useHistory } from 'react-router';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

import { login } from "../../store/session";
import './Splash.css'
import NavBar from "../NavBar";
const Splash = () => {
    const user = useSelector((state) => state.session.user);
    const history = useHistory();
    const dispatch = useDispatch();

    if (user) {
        history.push('/discover')
    }

    const demoLogin = async (e) => {
        e.preventDefault();
        const data = await dispatch(login("demo@aa.io", "password"));
        // if (data.errors) {
        //   setErrors(data.errors);
        // }
      };

    return (
        <main>
            <NavBar />
            <div className="story-cards">
                <section color='#9bf0e1' className='hero-section'>
                    <article color='#2d46b9' className='hero-article'>
                        <div className="hero-card">
                            <div className="hero-story-card-text">
                                <p className='type-element'>FOR NEW USERS</p>
                                <div className='hero-card-title-container'>
                                    <h1 className="hero-card-title">
                                        Jazz Music delivered to you for free.
                                    </h1>
                                </div>
                                <h2 className="hero-card-subtitle">
                                    Enjoy the greatest hits from Jazz's heaviest hitters at your comfort. Cancel anytime.
                                </h2>
                                <div className="story-signup-button">
                                    <h3 className="story-signup-text">Ready to listen? Click below to create your account.</h3>
                                    <div className='signup-container'>
                                        <div className='signup-btn-container'>
                                            <Link to='/sign-up' className='signup-card'>
                                                <div className='signup-btn'>
                                                    <span>
                                                        Sign up now
                                                    </span>
                                                </div>
                                                <div className='btn-focus'></div>
                                            </Link>
                                        </div>
                                        <div className='signup-btn-container demo' >
                                            <button className='signup-card' on onClick={demoLogin}>
                                                <div className='signup-btn'>
                                                    Demo the site
                                                </div>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className='hero-img-container'>
                                <div data-in-view="true" className='hero-image'></div>
                            </div>
                        </div>
                    </article>
                </section>
                {/* <div className='card-spacer'></div> */}
                <section dir='ltr' className='story-section'>
                    <article color='#1ed760' className='story-article'>
                        <div className='story-card'>
                            <p className='story-type-element'>FOR RETURNING USERS</p>
                            <h1 className='story-card-title'>Enjoy your favorite jazz content.</h1>
                            <div className='story-card-subheader'>
                                <h2 className='story-card-subtitle'>Get back to your favorite playlists</h2>
                            </div>
                            <div className='login-container'>
                                <div className='login-btn-container'>
                                    <Link to='/login' className='login-card'>
                                        <div className='login-btn'>
                                            <span>
                                                Login to Jazzify
                                            </span>
                                        </div>
                                    </Link>
                                </div>
                            </div>
                        </div>
                    </article>
                    <div className='splashfooter'>
                        {/* <Footer /> */}
                    </div>
                </section>
            </div>
        </main>
    )
};
export default Splash;
