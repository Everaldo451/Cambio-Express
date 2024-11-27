import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { ThemeProvider } from 'styled-components'
import { commonTheme } from './Theme'
import Header from './components/Head'
import Home from './routes/Home'
import Login from './routes/Login'
import ConfigurationPage from './routes/Configurations'
import './App.css'


function App() {

  return (
    <ThemeProvider theme={commonTheme}>
      <BrowserRouter>
        <Header/>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/login' element={<Login/>}/>
          <Route path='/configurations' element={<ConfigurationPage/>}/>
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  )
}

export default App
