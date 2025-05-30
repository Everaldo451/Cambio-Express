import { AxiosInstance, AxiosRequestConfig, AxiosStatic } from "axios"
import { SetStateAction } from "react"
import { authUserAxios } from "@/lib/axios/authUser";
import { UserType } from "@/types"

interface AxiosConfigs {
    instance: () => AxiosInstance|AxiosStatic,
    configs?: AxiosRequestConfig
}

export function genericAPIConsumer<T>(a:AxiosConfigs, url:string) {

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


export const getUser = genericAPIConsumer<UserType>({
    instance: () => authUserAxios,
}, "/me/")
