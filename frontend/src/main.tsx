import { StrictMode, createContext, useState, useEffect, useMemo } from 'react'
import { createRoot } from 'react-dom/client'
import { UserContextType, UserType, CSRFContextType, CSRFType} from './Types.ts'
import {getCSRF, getUser, updateAxios} from './load.tsx'
import App from './App.tsx'
import './index.css'

export const UserContext = createContext<UserContextType>([null, ()=>{}])
export const CSRFContext = createContext<CSRFContextType>([null, ()=>{}])


function Main() {

  const [csrfToken, setCSRFToken] = useState<CSRFType|null>(null)
  const [user,setUser] = useState<UserType|null>(null)
  const [loading, setLoaded] = useState<boolean>(true)

  useEffect(() => {
    updateAxios(csrfToken)
    getUser(setUser)
    getCSRF(setCSRFToken)
    setLoaded(false)
  },[])


  useMemo(() => {
    updateAxios(csrfToken)
    getUser(setUser)
    console.log(csrfToken)
  },[csrfToken])

  if (loading) {
    return (<></>)
  }
  else {
    return (
      <UserContext.Provider value={[user,setUser]}>
        <CSRFContext.Provider value={[csrfToken,setCSRFToken]}>
          <App/>
        </CSRFContext.Provider>
      </UserContext.Provider>
    )
  }
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Main/>
  </StrictMode>
)
