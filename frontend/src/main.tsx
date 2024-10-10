import { StrictMode, createContext, useState } from 'react'
import { createRoot } from 'react-dom/client'
import { UserContextType, UserType } from './Types.ts'
import App from './App.tsx'
import './index.css'

export const UserContext = createContext<UserContextType>([null, ()=>{}])

function Main() {
  return (
    <>
      <UserContext.Provider value={useState<UserType|null>(null)}>
        <App/>
      </UserContext.Provider>
    </>
  )
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Main/>
  </StrictMode>,
)
