import { authUserAxios } from "./authUserAxios";
import { cache } from "react";

export const getUser = cache(async () => {
    try {
        const response = await authUserAxios.get('/users/me')
        return response.data
    } catch (_) {
        return null
    }
})