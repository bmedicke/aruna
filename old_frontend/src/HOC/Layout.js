import React from 'react'
import Sidebar from '../components/Sidebar/Sidebar'
import PropTypes from 'prop-types'
const Layout = ({ children }) => {
  return (
    <>
      <Sidebar />
      {children}
    </>
  )
}

Layout.propTypes = {
  children: PropTypes.any,
}

export default Layout
