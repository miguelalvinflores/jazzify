import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux"
import { Link, Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import logoTextWhite from '../../images/logoTextWhite.png'
import './SignUpForm.css'
const SignUpForm = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [errorArr, setErrorArr] = useState([]);
  const [usernameActive, setUsernameActive] = useState(false)
  const [emailActive, setEmailActive] = useState(false);
  const [passwordActive, setPasswordActive] = useState(false);
  const [repeatPasswordActive, setRepeatPasswordActive] = useState(false);

  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      setErrorArr([]);
      let result = await dispatch(signUp(username, email, password));

      if (result.errors) {
        let errorList = [];
        for (let err in result.errors) {
          errorList.push(result.errors[err].split(':')[1]);
        }
        setErrorArr(errorList);
      }
    } else {
      setErrorArr(['passwords do not match']);
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
    if (e.target.value !== '') {
      setUsernameActive(true)
    } else {
      setUsernameActive(false)
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
    if (e.target.value !== '') {
      setEmailActive(true)
    } else {
      setEmailActive(false)
    }
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
    if (e.target.value !== '') {
      setPasswordActive(true)
    } else {
      setPasswordActive(false)
    }
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
    if (e.target.value !== '') {
      setRepeatPasswordActive(true)
    } else {
      setRepeatPasswordActive(false)
    }
  };

  if (user) {
    return <Redirect to="/discover" />;
  }

  let signupErrors = errorArr.map((err) => {
    return <li ket={err}>{err}</li>
  });

  return (
    <main>
      <div className='encore-light-theme'>
        <div className='index-signup' >
          <div className='signup-header-container'>
            <Link to='/' className='signup-header-logo-container'>
              <img src={logoTextWhite} className='signup-logo-img' alt='Jazzify header logo' />
            </Link>
            <h2 className='signup-type-element signup-header'>
              Sign up for free to start listening.
            </h2>
          </div>
          <form className='signup-form' onSubmit={onSignUp}>
            <ul>{signupErrors}</ul>
            <div className='sign-up-form-input'>
              <div className='form-input-label'>
                <label>What would you prefer we call you?</label>
              </div>
              <div className='form-input-box'>
                <input
                  className='form-input'
                  type="text"
                  name="username"
                  onChange={updateUsername}
                  value={username}
                ></input>
                <label className={ usernameActive ? "active" : ""}>Username</label>
              </div>
            </div>
            <div className='sign-up-form-input'>
              <div className='form-input-label'>
                <label>What is your E-mail?</label>
              </div>
              <div className='form-input-box'>
                <input
                  className='form-input'
                  type="text"
                  name="email"
                  onChange={updateEmail}
                  value={email}
                ></input>
                <label className={ emailActive ? "active" : ""}>E-mail</label>
              </div>
            </div>
            <div className='sign-up-form-input'>
              <div className='form-input-label'>
                <label>Create a Password</label>
              </div>
              <div className='form-input-box'>
                <input
                  className='form-input'
                  type="password"
                  name="password"
                  onChange={updatePassword}
                  value={password}
                ></input>
                <label className={passwordActive ? "active" : ""}>Password</label>
              </div>
            </div>
            <div className='sign-up-form-input'>
              <div className='form-input-label'>
                <label>Confirm your Password</label>
              </div>
              <div className='form-input-box'>
                <input
                  className='form-input'
                  type="password"
                  name="repeat_password"
                  onChange={updateRepeatPassword}
                  value={repeatPassword}
                  required={true}
                ></input>
                <label className={repeatPasswordActive ? "active" : ""}>Confirm Password</label>
              </div>
            </div>
            <div className='signup-form-opts'>
              <div className='signup-btn-container'>
                <button className='sign-up-btn' type="submit">
                  <div className='sign-up-btn-content'>
                    Sign Up
                  </div>
                </button>
              </div>
              <p className='sign-to-log-type-element'>
                <span className='login-link-container'>
                  Have an account?&nbsp;
                  <Link to='/login'>Log in</Link>
                </span>
              </p>
            </div>
          </form>
        </div>
      </div>
    </main>
  );
};

export default SignUpForm;
