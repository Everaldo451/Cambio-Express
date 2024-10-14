import { StrictMode, createContext, useState, useEffect } from 'react'
import { createRoot } from 'react-dom/client'
import { UserContextType, UserType, CSRFContextType, CSRFType } from './Types.ts'
import Load, {LoadFunctionProps} from './load.tsx'
import App from './App.tsx'
import './index.css'

export const UserContext = createContext<UserContextType>([null, ()=>{}])
export const CSRFContext = createContext<CSRFContextType>([null, ()=>{}])

interface MainType {
  loadData: ({}:LoadFunctionProps) => Promise<void>
}

function Main({loadData}:MainType) {

  const [csrf, setCSRF] = useState<CSRFType|null>(null)
  const [user,setUser] = useState<UserType|null>(null)

  useEffect(() => {
    loadData({setUser, setCSRF})
  },[])

  return (
    <>
      <UserContext.Provider value={[user,setUser]}>
        <CSRFContext.Provider value={[csrf,setCSRF]}>
          <App/>
        </CSRFContext.Provider>
      </UserContext.Provider>
    </>
  )
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Main loadData={Load}/>
  </StrictMode>,
)
