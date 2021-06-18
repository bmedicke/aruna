import React from 'react'
import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import Box from './components/Box.js'
import './App.css'

function App () {
  return (
    <div className='App'>
      <Canvas>
        <ambientLight />
        <pointLight position={[0, 0, 3]} />

        <OrbitControls />

        <Box position={[1, 1, 0]} />
        <Box position={[-1, 1, 0]} />
        <Box position={[-1, -1, 0]} />
        <Box position={[1, -1, 0]} />
      </Canvas>
    </div>
  )
}

export default App
