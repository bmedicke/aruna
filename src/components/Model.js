/* eslint-disable react/prop-types */
import React, { useRef, useState } from 'react'
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader'
import { useLoader, useFrame } from '@react-three/fiber'

function Model ({ url }, props) {
  const mesh = useRef()
  const geom = useLoader(STLLoader, url)
  geom.center()
  const [hovered, setHover] = useState(false)
  const [active, setActive] = useState(false)

  useFrame(() => {
    if (active) {
      mesh.current.rotation.y += 0.01
    }
  })

  return (
    <mesh
      {...props}
      ref={mesh}
      position={[0, 0, 0]}
      onClick={(event) => {
        setActive(!active)
        console.log(event)
      }}
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
