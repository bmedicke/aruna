/* eslint-disable react/prop-types */
import React, { useRef } from 'react'
import { useFrame } from '@react-three/fiber'

function Dot (props) {
  const mesh = useRef()

  useFrame(() => {
    const ts = new Date().getTime() / 300
    mesh.current.position.y += Math.sin(ts + props.position[0])
    mesh.current.rotation.y += 0.2
  })

  return (
    <mesh
      {...props}
      ref={mesh}
      scale={1}
    >
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color='white' />
    </mesh>
  )
}

export default Dot
