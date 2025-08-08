import { TokenType } from "@/types";
import { cookies } from "next/headers"
import { apiAxios } from "./apiAxios";

export const authUserAxios = apiAxios.create({})

authUserAxios.interceptors.request.use(async (config) => {
    const cookieStore = await cookies()
    const accessToken = cookieStore.get("access_token")
    if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`
        return config
    }

    const refreshToken = cookieStore.get("refresh_token")
    if (!refreshToken) {
        return config
    }

    const response = await apiAxios.get("/auth/refresh",{
        headers: {
            "Authorization": `Bearer ${refreshToken}`
        }
    })
    const data = response.data
    if (data instanceof Object && "access_token" in data) {
        const accessToken = data["access_token"] as TokenType

        cookieStore.set('access_token', accessToken.value, {
            httpOnly: true,
            maxAge: accessToken.lifetime
        })
        config.headers.Authorization = `Bearer ${accessToken}`
    }

    return config
}, (error) => Promise.reject(error))