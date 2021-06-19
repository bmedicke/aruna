import React from 'react'
import PropTypes from 'prop-types'
import './SidebarButton.scss'

const SidebarButton = ({ text, click }) => {
  return (
    <div className="sidebar-button" onClick={click}>
      {text}
    </div>
  )
}

SidebarButton.propTypes = {
  text: PropTypes.string,
  click: PropTypes.func,
}

export default SidebarButton
