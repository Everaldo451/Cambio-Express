import axios, { AxiosInstance, AxiosRequestConfig, AxiosStatic } from "axios"
import { SetStateAction } from "react"
import { CSRFType, JWT, UserType } from "./Types"

interface AxiosConfigs {
    instance: () => AxiosInstance|AxiosStatic,
    configs?: AxiosRequestConfig
}

export let customAxios = axios.create()

export async function UpdateAxios (jwt:JWT|null) {
    customAxios = axios.create({
      headers: jwt?{
        'Authorization': `Bearer ${jwt.access_token}`
      }:{}
    })
}

function GenericAPIConsumer<T>(a:AxiosConfigs, url:string) {

    async function NewFunction(setState:React.Dispatch<SetStateAction<T|null>>) {

        try {
            const response = await a.instance().get(url,a.configs)

            const data = response.data
            setState(data?data:null)
        }
        catch (error) {
            setState(null)
            console.log(error)
        }
    }

    return NewFunction
}


export const GetCSRF = GenericAPIConsumer<CSRFType>({
    instance: () => axios,
    configs: {
        withCredentials: true
    }
}, "/api/getcsrf/")


export const GetUser = GenericAPIConsumer<UserType>({
    instance: () => customAxios,
}, "/api/auth/getuser/")


export const GetJWT = GenericAPIConsumer<JWT>({
    instance: () => customAxios,
    configs: {
        withCredentials: true
    }
}, "/api/auth/getjwt/")
