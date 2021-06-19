import React from 'react'
import Sidebar from '../components/Sidebar/Sidebar'
import PropTypes from 'prop-types'
const Layout = ({ children }) => {
  return (
    <>
      <div>
        <Sidebar />
      </div>
      <main>{children}</main>
    </>
  )
}

Layout.propTypes = {
  children: PropTypes.any,
}

export default Layout
