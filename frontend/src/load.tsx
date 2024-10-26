import { SetStateAction } from "react"
import { UserType, CSRFType } from "./Types"
import { useNavigate } from "react-router-dom"

async function GetCSRF() {

    try {

        const response = await fetch("/api/getcsrf/",{
            method:"GET",
            credentials:"include",
        })

        console.log(response.url)

        const data = await response.json()

        return data?data:null

    }
    catch(e) {
        console.log(e)
        return null
    }

}

export async function GetUser() {

    try {

        const response = await fetch("/api/getuser/",{
            method:"GET",
            credentials:"include"
        })

        const data = await response.json()
        console.log(data)

        return data?data:null

    }
    catch(e) {
        console.log(e)
        return null
    }

}

export interface LoadFunctionProps {
    setUser: React.Dispatch<SetStateAction<UserType|null>>,
    setCSRF: React.Dispatch<SetStateAction<CSRFType|null>>,
    setLoaded: React.Dispatch<SetStateAction<boolean>>
}

async function Load({setUser, setCSRF, setLoaded}:LoadFunctionProps) {

    const [userData, csrfData] = await Promise.all([GetUser(), GetCSRF()])

    try {
        console.log(userData,csrfData.csrf)
        setUser(userData?userData.current_user:null)
        setCSRF(csrfData.csrf)
    }catch(e) {}
    
    setLoaded(false)

}

export default Load