import React, { useState, useEffect } from "react";
import { BrowserRouter, Redirect, Route, Switch } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import Splash from './components/Splash/Splash'
import Discover from './components/Discover/Discover';
import { authenticate } from "./store/session";
import PlayingBar from './components/Discover/PlayingBar/PlayingBar';

function App() {
  const user = useSelector(state => state.session.user)
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();
  const tracksQueue = useSelector((state) => state.tracks.trackQueue)
  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  let loggedIn = false;
  if (user) {
    loggedIn = true;
  }
  return (

    <BrowserRouter>
      <Switch>
        <Route path="/" exact={true} >
          { loggedIn ? <Redirect to='/discover' /> : <Splash /> }
        </Route>
        <Route path="/login" exact={true}>
          { loggedIn ? <Redirect to='/discover' /> : <LoginForm /> }
        </Route>
        <Route path="/sign-up" exact={true}>
          { loggedIn ? <Redirect to='/discover' /> : <SignUpForm /> }
        </Route>
        <ProtectedRoute path='/discover' >
          <Discover />
        </ProtectedRoute>
        {/* <ProtectedRoute path="/users" exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute> */}
      </Switch>
      {tracksQueue && (
                        <PlayingBar
                        tracksQueue={tracksQueue} />
                    )}
    </BrowserRouter>
  );
}

export default App;
