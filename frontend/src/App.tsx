import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Header from './components/Head'
import Home from './routes/Home'
import Login from './routes/Login'
import ConfigurationPage from './routes/Configurations'
import './App.css'


function App() {

  return (
    <>
      <BrowserRouter>
        <Header/>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/login' element={<Login/>}/>
          <Route path='/configurations' element={<ConfigurationPage/>}/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
