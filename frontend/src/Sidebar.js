import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faUser, faBuilding, faHistory } from '@fortawesome/free-solid-svg-icons';
import './Sidebar.css';
import { useNavigate } from 'react-router';

import admImage from './admin.jpg';

const Sidebar = ({ activeItem, onSidebarItemClick }) => {

  const navigate=useNavigate();
  return (
    <div className="sidebar">
      <div className="profile">
        <div className="profile-image">
          <img src={admImage} alt="Profile" />
        </div>
        <div className="profile-title">Admin</div>
      </div>
      <ul className="sidebar-menu">
        <li className={activeItem === 0 ? 'active' : ''} onClick={() =>{navigate("/")}}>
          <FontAwesomeIcon icon={faHome} />
          <a href="#">Home</a>
        </li>
        <li className={activeItem === 1 ? 'active' : ''} onClick={() => {navigate("/addp")}}>
          <FontAwesomeIcon icon={faUser} />
          <a href="#">Compte</a>
        </li>
        <li className={activeItem === 2 ? 'active' : ''} onClick={() => {navigate("/sal")}}>
          <FontAwesomeIcon icon={faBuilding} />
          <a href="">Salle</a>
        </li>
        
      </ul>
    </div>
  );
};

export default Sidebar;