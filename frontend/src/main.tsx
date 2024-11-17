import { StrictMode, createContext, useState, useEffect } from 'react'
import { createRoot } from 'react-dom/client'
import { UserContextType, UserType, CSRFContextType, CSRFType, JWTContextType, JWT } from './Types.ts'
import {GetCSRF, GetUser, GetJWT, UpdateAxios} from './load.tsx'
import App from './App.tsx'
import './index.css'

export const UserContext = createContext<UserContextType>([null, ()=>{}])
export const CSRFContext = createContext<CSRFContextType>([null, ()=>{}])
export const JWTContext = createContext<JWTContextType>([null, () => {}])


function Main() {

  const [csrf, setCSRF] = useState<CSRFType|null>(null)
  const [user,setUser] = useState<UserType|null>(null)
  const [jwt, setJWT] = useState<JWT|null>(null)
  const [loading, setLoaded] = useState<boolean>(true)

  useEffect(() => {
    GetJWT(setJWT)
    UpdateAxios(jwt)
    GetUser(setUser)
    GetCSRF(setCSRF)
    setLoaded(false)
  },[])

  useEffect(() => {
    UpdateAxios(jwt)
    GetUser(setUser)
    console.log(jwt)
  },[jwt])

  if (loading) {
    return (<></>)
  }
  else {
    return (
      <>
        <JWTContext.Provider value={[jwt,setJWT]}>
          <UserContext.Provider value={[user,setUser]}>
            <CSRFContext.Provider value={[csrf,setCSRF]}>
              <App/>
            </CSRFContext.Provider>
          </UserContext.Provider>
        </JWTContext.Provider>
      </>
    )
  }
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Main/>
  </StrictMode>
)
