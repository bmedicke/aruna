import React from 'react'
import PropTypes from 'prop-types'
import './SidebarButton.scss'

const SidebarButton = ({ li, click }) => {
  return (
    <div className="sidebar-button" onClick={click}>
      <span className="sidebar-button__logo">
        <li.icon />
      </span>
      {li.text}
    </div>
  )
}

SidebarButton.propTypes = {
  li: PropTypes.node,
  click: PropTypes.func,
}

export default SidebarButton
