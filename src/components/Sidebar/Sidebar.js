import { React, useState } from 'react'
import SidebarButton from './SidebarButton/SidebarButton'
import './Sidebar.scss'

const Sidebar = () => {
  const [isClosed, setIsClosed] = useState(true)

  let lis = ['Home', 'Editor', 'My Circuits', 'Settings', 'Help']

  let clickHandler = () => {
    setIsClosed(!isClosed)
    console.log('clicked')
  }

  return (
    <div className={`sidebar-wrapper${isClosed ? ' closed' : ''}`}>
      <div className="sidebar">
        <p className="sidebar__logo" onClick={() => clickHandler()}>
          Aruna
        </p>
        {lis.map((li, index) => (
          <SidebarButton key={index} text={li} click={() => clickHandler()} />
        ))}
      </div>
    </div>
  )
}
export default Sidebar
