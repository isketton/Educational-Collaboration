import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import { IoClose, IoMenu } from "react-icons/io5";
import "../styles/navbar.css";

export default function Navbar() {
  const [showMenu, setShowMenu] = useState(false);

  const toggleMenu = () => {
    setShowMenu(!showMenu);
  };

  const closeMenuOnMobile = () => {
    if (window.innerWidth <= 1150) {
      setShowMenu(false);
    }
  };
  return (
    <header className="header">
      <nav className="nav container">
        <NavLink to="/" className="nav_logo">
          SchoolConnection
        </NavLink>

        <div
          className={`nav_menu ${showMenu ? "show-menu" : ""}`}
          id="nav-menu"
        >
          <ul className="nav_list">
            <li className="nav_item">
              <NavLink to="/" className="nav_link" onClick={closeMenuOnMobile}>
                Home
              </NavLink>
            </li>
            <li className="nav_item">
              <NavLink
                to="/sign-in"
                className="nav_link nav_cta"
                onClick={closeMenuOnMobile}
              >
                Sign In
              </NavLink>
            </li>
          </ul>
          <div className="nav_close" id="nav-close" onClick={toggleMenu}>
            <IoClose />
          </div>
        </div>

        <div className="nav_toggle" id="nav-toggle" onClick={toggleMenu}>
          <IoMenu />
        </div>
      </nav>
    </header>
  );
};
