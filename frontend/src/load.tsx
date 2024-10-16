import { SetStateAction } from "react"
import { UserType, CSRFType } from "./Types"
import { useNavigate } from "react-router-dom"

async function GetCSRF() {

    try {

        const response = await fetch("http://localhost:8000/getcsrf",{
            method:"GET",
            credentials:"include"
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

        const response = await fetch("http://localhost:8000/getuser",{
            method:"GET",
            credentials:"include"
        })

        const data = await response.json()

        return data?data:null

    }
    catch(e) {
        console.log(e)
        return null
    }

}

export interface LoadFunctionProps {
    setUser: React.Dispatch<SetStateAction<UserType|null>>,
    setCSRF: React.Dispatch<SetStateAction<CSRFType|null>>
}

async function Load({setUser, setCSRF}:LoadFunctionProps) {

    const [userData, csrfData] = await Promise.all([GetUser(), GetCSRF()])

    console.log(userData,csrfData.csrf)
    setUser(userData)
    setCSRF(csrfData.csrf)

}

export default Load