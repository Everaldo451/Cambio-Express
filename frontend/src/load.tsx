import axios, { AxiosInstance, AxiosRequestConfig, AxiosStatic } from "axios"
import { SetStateAction } from "react"
import { CSRFType, UserType } from "./Types"

interface AxiosConfigs {
    instance: () => AxiosInstance|AxiosStatic,
    configs?: AxiosRequestConfig
}

export let customAxios = axios.create()

export async function updateAxios (csrf_token:CSRFType|null) {
    customAxios = axios.create({
      headers: csrf_token?{
        'X-CSRFToken': csrf_token,
      }:{}
    })
}

function genericAPIConsumer<T>(a:AxiosConfigs, url:string) {

    async function newFunction(setState:React.Dispatch<SetStateAction<T|null>>) {

        try {
            const response = await a.instance().get(url,a.configs)

            const data = response.data
            setState(data?data.data:null)
        }
        catch (error) {
            setState(null)
            console.log(error)
        }
    }

    return newFunction
}


export const getCSRF = genericAPIConsumer<CSRFType>({
    instance: () => axios,
    configs: {
        withCredentials: true
    }
}, "/api/getcsrf/")


export const getUser = genericAPIConsumer<UserType>({
    instance: () => customAxios,
}, "/api/me/")
