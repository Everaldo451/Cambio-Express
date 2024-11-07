import axios from "axios"
import { customAxios } from "./main"

export async function GetCSRF() {

    try {

        const response = await axios.get("/api/getcsrf/",{
            withCredentials: true
        })

        return response.data?response.data:null

    }
    catch (error) {

        console.log(error)
        return null
    }

}

export async function GetUser() {

    try {

        const response = await customAxios.get("/api/getuser/",)

        return response.data?response.data:null
    }
    catch (error) {
        console.log(error)
        return null
    }

}
