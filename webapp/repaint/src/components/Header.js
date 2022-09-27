import React from 'react'
import PropTypes from 'prop-types'
import Header from './Header'
import { Link } from 'react-router-dom'

export default function (props) {
  let headerStyle = {
    backgroundColor: '#000000',
    padding: '0em 2em 0em',
    color: 'white',
    display: "flex"
  }


  return (
    <>
      <div className='header' style={headerStyle}>
        <div style={{ fontSize: '2em', width: '8em', alignItems: 'bottom' }}>
          <h3>{props.title}</h3>
        </div>
        <div style={{ width: '104em', textAlign: 'end', marginTop: '5em'}}>
          <Link to="/" style={{ textDecoration: 'None', color: 'white', fontSize: '1.4em', marginRight: '1em' }}>Engine</Link>
          <Link to="/" style={{ textDecoration: 'None', color: 'white', fontSize: '1.4em' }}>Source Code</Link>
        </div>
      </div>
    </>
  )
}

Header.propTypes = {
  title: PropTypes.string,
}

Header.defaultProps = {
  title: "Your title here",
}