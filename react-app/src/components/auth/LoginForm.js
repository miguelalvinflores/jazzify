import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect, Link } from "react-router-dom";

import { login } from "../../store/session";
import logoTextWhite from '../../images/logoTextWhite.png'
import "./LoginForm.css"
const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();


  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data.errors) {
      setErrors(data.errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);

  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <main>
      <div className='header-container'>
        <div className='header'>
          <Link
            to='/'
            title="Spotify"
            className='jazzify-logo'
          >
            <img src={logoTextWhite} className='login-logo-img' alt='Jazzify header logo' />
          </Link>
        </div>
      </div>
      <div className='login-container-fluid' >
        <div className='login-content'>
          <div className='login-row'>
            <div className='login-txt-center col-12'>
              <h1 id='login-to-continue'>To continue, log in to Jazzify</h1>
            </div>
          </div>

          <form onSubmit={onLogin}>
            <div className='login-row'>
              {errors.map((error) => (
                <div className='error-row'>{error}</div>
              ))}
            </div>
            <div className='login-row'>
              <div className='col-12'>
                <label className='login-label' htmlFor="email">Email address</label>
                <input
                  className='login-form-control'
                  name="email"
                  type="text"
                  placeholder="Email"
                  value={email}
                  onChange={updateEmail}
                />
              </div>
            </div>
            <div className='login-row'>
              <div className='col-12'>
                <label className='login-label' htmlFor="password">Password</label>
                <input
                  className='login-form-control'
                  name="password"
                  type="password"
                  placeholder="Password"
                  value={password}
                  onChange={updatePassword}
                />
              </div>
            </div >
            <div className='login-row row-submit'>
              <div className='col-12'>
                <button className='login-btn' type="submit">Login</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </main>
  );
};

export default LoginForm;
