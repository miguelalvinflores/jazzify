import React, { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { NavLink, useLocation } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import ProfileButton from './ProfileButton'

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
      <button className='btn-red authLinks'>
        <NavLink to='/login' className='login-nav' style={{ textDecoration: 'none' }}>Sign In</NavLink>
      </button>
    )
  }

  return (
    <nav>
      <a className='logo-container' href='/' exact='true' activeclassname='active'>
        <img src='images/Logo_Text.png' alt='Jazzify logo' />
      </a>

    </nav>
  );
}

export default NavBar;
