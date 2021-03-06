import React, { useEffect } from 'react';
import logoText from '../images/logoText.png'
import { useSelector } from 'react-redux';
import { NavLink, useLocation } from 'react-router-dom';
import ProfileButton from './ProfileButton'
import './NavBar.css'

const NavBar = () => {
  const sessionUser = useSelector((state) => state.session.user);
  const location = useLocation();

  useEffect(() => {
    let navBar = document.querySelector('nav')
    if (location.pathname === '/sign-up' || sessionUser) {
      navBar.classList.add('logged-in')
    } else {
      navBar.classList.remove('logged-in')
    }
  })

  let sessionLinks;

  if (sessionUser) {
    sessionLinks = (
      <>
        <div>
          <a href='/discover' className='home-nav'>Home</a>
          <div className='nav-profile-btn__container' >
            <ProfileButton user = {sessionUser} />

          </div>
        </div>
      </>
    );
  } else {
    sessionLinks = (
      <ul className='nav-list'>
        <NavLink to='/sign-up' className='signup-nav nav' style={{ textDecoration: 'none' }}>
          Sign up
        </NavLink>
        <NavLink to='/login' className='login-nav nav' style={{ textDecoration: 'none' }}>
          Log in
        </NavLink>
      </ul>
    )
  }

  return (
    <div className='nav-container'>
      <header className='header-hover'>
        <a className='logo-container' href='/' exact='true' activeclassname='active'>
          <img src={logoText} alt='Jazzify logo' />
        </a>
      </header>
      <div className='bio-links'>
        <div className="github-bio">
          <a className='fav-color' href="https://github.com/miguelalvinflores">
            <i className="fab fa-github fa-3x"></i>
          </a>
        </div>
        <div className="linkedIn-bio">
          <a className='fav-color' href="https://www.linkedin.com/in/miguelalvinflores/">
            <i className="fab fa-linkedin-in fa-3x"></i>
          </a>
        </div>
        <div className="AngelList-bio">
          <a className='fav-color' href="https://angel.co/u/miguel-flores-22">
            <i className="fab fa-angellist fa-3x"></i>
          </a>
        </div>
      </div>
      <nav>
        {sessionLinks}
      </nav>
    </div>
  );
}

export default NavBar;
