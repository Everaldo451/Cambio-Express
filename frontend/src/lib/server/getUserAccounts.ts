import { authUserAxios } from "@/lib/server/authUserAxios"
import { cache } from "react";
import { AccountType } from "@/types"

export const getUserAccounts = cache(async () => {
    try{
        const response = await authUserAxios.get('/accounts/')
        return response.data
    } catch (error) {
        return null
    }
})

export async function getUserAccount(id:Pick<AccountType, "id">) {
    try{
        const response = await authUserAxios.get(`/accounts/${id}`)
        return response.data
    } catch (error) {
        return null
    }
}