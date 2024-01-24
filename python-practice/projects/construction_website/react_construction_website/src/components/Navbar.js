import React, { useState } from 'react'
import { Link } from 'react-router-dom'

export default function Navbar() {

    const [click, setClick] = useState(false)

    const handleClick = () => setClick(!click)
    const closeMobileMenu = () => setClick(false)

    return (
        <div>
            <nav className='navbar'>
                <div className='navbar-container'>
                    <Link to="/"> <h1 className="store-name">LOGO</h1> </Link>
                    <div className="menu-icon" onClick={handleClick}>
                        <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
                    </div>
                    <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                        <li className="nav-item">
                            <Link to="/" className='nav-links' onClick={closeMobileMenu}>Services</Link>
                        </li>
                        <li className="nav-item">
                            <Link to="/" className='nav-links' onClick={closeMobileMenu}>Portfolio</Link>
                        </li>
                        <li className="nav-item"> 
                            <Link to="/" className='nav-links' onClick={closeMobileMenu}>Contact</Link>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    )
}