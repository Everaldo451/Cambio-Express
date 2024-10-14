import { SetStateAction } from "react"
import { UserType, CSRFType } from "./Types"

async function GetCSRF() {

    try {

        const response = await fetch("localhost:8000/get_csrf",{
            method:"GET",
            credentials:"include"
        })

        const data = await response.json()

        return data?data:null

    }
    catch(e) {return null}

}

export async function GetUser() {

    try {

        const response = await fetch("localhost:8000/",{
            method:"GET",
            credentials:"include"
        })

        const data = await response.json()

        return data?data:null

    }
    catch(e) {return null}

}

export interface LoadFunctionProps {
    setUser: React.Dispatch<SetStateAction<UserType|null>>,
    setCSRF: React.Dispatch<SetStateAction<CSRFType|null>>
}

async function Load({setUser, setCSRF}:LoadFunctionProps) {

    const [userData, csrfData] = await Promise.all([GetUser(), GetCSRF()])

    setUser(userData)
    setCSRF(csrfData)

}

export default Load