import React from 'react'
import { Link } from 'react-router-dom'

export default function Navbar() {
    return (
        <div className='div-container'>
            <nav>
                <Link to="/"> <h1 className="store-name">LOGO</h1> </Link>
                <ul className="tabs">
                    <li>Services</li>
                    <li>Portfolio</li>
                    <li>Contact</li>
                </ul>
            </nav>
        </div>
    )
}