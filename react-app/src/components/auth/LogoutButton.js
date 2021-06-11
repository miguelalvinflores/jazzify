import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";

const LogoutButton = ({profileBtnClick}) => {
  const dispatch = useDispatch();
  const onLogout = async (e) => {
    dispatch(logout());
  };

  return <button className='logout-btn' onClick={onLogout} onBlur={profileBtnClick}>Logout</button>;
};

export default LogoutButton;
