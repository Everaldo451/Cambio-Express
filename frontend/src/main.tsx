import { StrictMode, createContext, useState, useEffect } from 'react'
import { createRoot } from 'react-dom/client'
import axios, { AxiosInstance } from 'axios'
import { UserContextType, UserType, CSRFContextType, CSRFType, JWTContextType, JWT } from './Types.ts'
import {GetCSRF, GetUser} from './load.tsx'
import App from './App.tsx'
import './index.css'

export const UserContext = createContext<UserContextType>([null, ()=>{}])
export const CSRFContext = createContext<CSRFContextType>([null, ()=>{}])
export const JWTContext = createContext<JWTContextType>([null, () => {}])
export let customAxios:AxiosInstance


function Main() {

  const [csrf, setCSRF] = useState<CSRFType|null>(null)
  const [user,setUser] = useState<UserType|null>(null)
  const [jwt, setJWT] = useState<JWT|null>(null)
  const [loading, setLoaded] = useState<boolean>(true)

  async function CSRFLoad() {
    const csrfData = await GetCSRF()

    try {
        console.log(csrfData.csrf)
        setCSRF(csrfData.csrf)
    }catch(e) {}
  
    setLoaded(false)
  }

  async function UpdateAxiosAndUser () {
    customAxios = axios.create({
      headers: jwt?{
        'Authorization': `Bearer ${jwt}`
      }:{}
    })

    const userData = await GetUser()
    try {
        console.log(userData)
        setUser(userData?userData:null)
    }catch(e) {}
  }

  useEffect(() => {
    UpdateAxiosAndUser()
    CSRFLoad()
  },[])

  useEffect(() => {
    UpdateAxiosAndUser()
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
