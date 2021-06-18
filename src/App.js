/* eslint-disable react/prop-types */
/* eslint-disable no-unused-vars */
import React, { useRef, Suspense } from 'react'
import { Canvas, useLoader, useFrame } from '@react-three/fiber'
import { MapControls, Text } from '@react-three/drei'
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader'

import './App.css'

function Model ({ url }, props) {
  const mesh = useRef()
  const geom = useLoader(STLLoader, url)

  // useFrame(() => (mesh.current.rotation.x += 0.01))

  return (
    <mesh
      ref={mesh}
      position={[-120, -110, 0]}
      {...props}
    >
      <primitive object={geom} attach='geometry' />
      <meshStandardMaterial color='grey' />
    </mesh>
  )
}

function App () {
  return (
    <div className='App'>
      <Canvas
        orthographic
        camera={{ zoom: 10, position: [0, 0, 200] }}
        style={{ backgroundColor: 'black' }}
      >
        <ambientLight intensity={0.3} />
        <pointLight position={[0, 0, 3]} />

        <MapControls />

        <Suspense fallback={null}>
          <Model url='./models/hexlamp.stl' />
        </Suspense>

        <Text
          color='white'
          anchorX='center'
          anchorY='middle'
          fontSize={10}
          position={[0, 30, 0]}
        >
          Aruna
        </Text>
      </Canvas>
    </div>
  )
}

export default App
