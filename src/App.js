import React, { useRef, Suspense } from 'react'
import { Canvas, useLoader } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader'

import './App.css'

/* eslint-disable react/prop-types */
function Model ({ url }) {
  const geom = useLoader(STLLoader, url)
  const ref = useRef()

  return (
    <mesh ref={ref} position={[-100, -100, 0]}>
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
        camera={{ zoom: 2, position: [0, 0, 100] }}
        style={{ backgroundColor: 'black' }}
      >
        <ambientLight intensity={0.3} />
        <pointLight position={[0, 0, 3]} />

        <OrbitControls />

        <Suspense fallback={null}>
          <Model url='./models/hexlamp.stl' />
        </Suspense>
      </Canvas>
    </div>
  )
}

export default App
