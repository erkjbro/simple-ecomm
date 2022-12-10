import React from 'react';
import { NavLink } from 'react-router-dom';

const Navbar: React.FC = () => {
  const navLinks = (
    <>
      <li><NavLink to="/details">Pdp</NavLink></li>
      <li><NavLink to="/listing">Plp</NavLink></li>
    </>
  )

  return (
    <nav>
      <NavLink to={'/'}>SEP (tm)</NavLink>
      <ul>
        {navLinks}
      </ul>
    </nav>
  );
};

export { Navbar };
