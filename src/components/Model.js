/* eslint-disable react/prop-types */
import React, { useRef, useState } from 'react'
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader'
import { useLoader } from '@react-three/fiber'

function Model ({ url }, props) {
  const mesh = useRef()
  const geom = useLoader(STLLoader, url)
  geom.center()
  const [hovered, setHover] = useState(false)

  return (
    <mesh
      {...props}
      ref={mesh}
      position={[0, 0, 0]}
      onPointerOver={(event) => {
        setHover(true)
        console.log(event)
      }}
      onPointerOut={(event) => {
        setHover(false)
        console.log(event)
      }}
    >
      <primitive object={geom} attach='geometry' />
      <meshStandardMaterial color={hovered ? 'red' : 'grey'} />
    </mesh>
  )
}

export default Model
