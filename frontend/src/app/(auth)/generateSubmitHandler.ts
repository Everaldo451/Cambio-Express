import { redirect } from 'next/navigation'
import { cookies } from 'next/headers'

import { TokenType } from '@/types'
import { apiAxios } from '@/lib/client/apiAxios'

export default function generateSubmitHandler(action:string) {
    async function handleSubmit(formData:FormData) {
        'use server'
        try {
            const response = await apiAxios.request({
                url: action,
                method: "POST",
                data: formData,
                withCredentials: true,
            })
            const data = response.data
            if (data instanceof Object && "tokens" in data) {
                const tokens = data["tokens"]
                const cookiesHandler = await cookies()
                for (const [tokenName, tokenData] of tokens) {
                    cookiesHandler.set(tokenName, (tokenData as TokenType).value, {
                        httpOnly: true,
                        path: "/",
                        maxAge: (tokenData as TokenType).lifetime
                    })
                }
            }
        } catch (error) {
            console.log(error)
        }
        redirect("/")
    }
    return handleSubmit
}