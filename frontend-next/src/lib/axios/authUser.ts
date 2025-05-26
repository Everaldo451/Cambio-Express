import { apiAxios } from "./api";
import { getCookieByName } from "@/utils/cookies";
import { TokenType } from "@/types";

export const authUserAxios = apiAxios.create({})

authUserAxios.interceptors.request.use((config) => {
    const accessToken = getCookieByName("access_token")
    if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`
        return config
    }

    const refreshToken = getCookieByName("refresh_token")
    if (!refreshToken) {
        return config
    }

    const responsePromise = apiAxios.get("/auth/refresh",{
        headers: {
            "Authorization": `Bearer ${refreshToken}`
        }
    })
    responsePromise
    .then((response) => {
        const data = response.data
        if (data instanceof Object && "access_token" in data) {
            const accessToken = data["access_token"] as TokenType

            document.cookie = `access_token=${accessToken.value}`
            config.headers.Authorization = `Bearer ${accessToken}`
        }
    })
    .catch((error) => {})

    return config
})