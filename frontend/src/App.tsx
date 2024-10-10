import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { useState } from 'react'
import Header from './components/Head'
import Home from './routes/Home'
import './App.css'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BrowserRouter>
        <Header/>
        <Routes>
          <Route path='/' element={<Home/>}/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
