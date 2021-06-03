import React, { useEffect } from 'react';
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
      <NavLink to='/login' className='login-nav' style={{ textDecoration: 'none' }}>
        <div className='authLinks'>
          <button className='btn-red'>
            Sign In
          </button>

        </div>
          </NavLink>
    )
  }

  return (
    <nav>
      <a className='logo-container' href='/' exact='true' activeclassname='active'>
        <img src='images/Logo_Text.png' alt='Jazzify logo' />
      </a>
      {sessionLinks}
    </nav>
  );
}

export default NavBar;
