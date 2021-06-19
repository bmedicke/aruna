import React, { useRef, useState } from 'react'
import { useFrame } from '@react-three/fiber'

function Box(props) {
  const mesh = useRef()
  const [hovered, setHover] = useState(false)
  const [active, setActive] = useState(false)

  useFrame(() => (mesh.current.rotation.x += 0.01))

  return (
    <mesh
      {...props}
      ref={mesh}
      scale={active ? 1.5 : 1}
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
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color={hovered ? 'red' : 'grey'} />
    </mesh>
  )
}

export default Box
