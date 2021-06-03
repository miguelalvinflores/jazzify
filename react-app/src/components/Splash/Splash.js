import React, { useState } from 'react';
import { useHistory } from 'react-router';
import { useDispatch, useSelector } from 'react-redux';
import { checkEmail } from '../../store/session';
import './Splash.css'

const Splash = () => {
    const user = useSelector((state) => state.session.user);
    const [email, setEmail] = useState('');
    const [errorArr, setErrorArr] = useState([]);
    const [isActive, setIsActive] = useState(false);
    const dispath = useDispatch();
    const history = useHistory();

    const handleTextChange = (text) => {
        setEmail(text);

        if (text !== '') {
            setIsActive(true);
        } else {
            setIsActive(false);
        }
    }

    const onGetStartedClick = async (e) => {
        e.preventDefault();
        let result = await dispath(checkEmail(email));

        if (result.errors) {
            let errorList = [];

            for (let err in result.errors) {
                errorList.push(result.errors[err].split(':'[1]));
            }
            setErrorArr(errorList);
        } else {
            if (result.email) {
                history.push({
                    pathname: '/login',
                    state: {
                        userEmail: result.email,
                    },
                });
            } else {
                history.push({
                    pathname: '/sign-up',
                    state: {
                        userEmail: email,
                    },
                });
            }
        }

    };

    let emailCheckErrors = errorArr.map((err) => {
        return <li key={err}>{err}</li>
    })

    if (user) {
        history.push('/browse')
    }

    return (
        <div className="story-cards">
            <div className="hero-card">
                <div className="hero-card-background">
                    <div className='hero-card-img'></div>
                    {/* <div className="concord-img-gradient"></div> */}
                </div>
                <div className="hero-story-card-text">
                    <h1 className="story-card-title">
                        Jazz Music delivered to you for free.
                    </h1>
                    <h2 className="story-card-subtitle">
                        Enjoy the greatest hits from Jazz's heaviest hitters such as Louie Armstrong, Duke Ellington, and more.
                    </h2>
                    <div className="story-signup-button">
                        <h3 className="story-signup-text">Ready listen? Enter your email to create your account.</h3>
                        <form className='email-form' onSubmit={onGetStartedClick}>
                            <ul>{emailCheckErrors}</ul>
                            <div className='email-form-lookup'>
                                <div id='float-label'>
                                    <input
                                        type="email"
                                        name="email"
                                        id='email_hero'
                                        onChange={(e) => handleTextChange(e.target.value)}
                                        required
                                    />
                                    <label className={ isActive ? "Active" : ""} htmlFor='email_hero'>Email address</label>
                                </div>
                                <button className='hero-btn-red' type='submit'>Get Started {'>'}</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <div className='card-spacer'></div>
            <div className='story-card watchOnPC'>
                <div className='story-card-container'>
                    <div className='story-card-text'>
                        <h1 className='story-card-title'>Enjoy your favorite jazz content.</h1>
                        <h2 className='story-card-subtitle'>Dont be a square join up today!</h2>
                    </div>
                    <div className='story-card-img-container'>
                        <img className='-card-img' src='images/Splash-Device_Screens.png' alt="Example Movie title panel" />
                    </div>
                </div>
            </div>
            <div className='splashfooter'>
                {/* <Footer /> */}
            </div>
        </div>
    )
};
export default Splash;
