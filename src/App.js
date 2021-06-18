import './App.css'
import Dot from './components/Dot.js'
import Model from './components/Model.js'
import React, { Suspense } from 'react'
import { Canvas } from '@react-three/fiber'
import { MapControls, Text } from '@react-three/drei'

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

        <Text
          color='white'
          anchorX='center'
          anchorY='middle'
          fontSize={10}
          position={[0, 30, 0]}
        >
          Aruna
        </Text>

        {[...Array(500)].map((x, i) =>
          <Dot key={i} position={[i * 0.2 - 100 / 2, -10, -20]} />
        )}

        <Suspense fallback={null}>
          <Model url='./models/hexlamp.stl' />
        </Suspense>
      </Canvas>
    </div>
  )
}

export default App
