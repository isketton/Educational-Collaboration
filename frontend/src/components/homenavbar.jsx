import React, { useState } from "react";
import axios from "axios";
import { NavLink } from "react-router-dom";

export default function HomeNavbar() {
  return (
    <header className="header">
      <nav className="navbar">
      <NavLink to="/home" className="nav_logo">
         Home
       </NavLink>
        <div className="nav_menu">
          <ul className="nav_list">
            <li className="nav_item">
              <NavLink to="/" className="nav_link">
                Home
              </NavLink>
            </li>
          </ul>
        </div>
      </nav>
    </header>
  );
}
