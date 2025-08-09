import { redirect } from 'next/navigation'
import { cookies } from 'next/headers'

import { TokenType } from '@/types'
import { apiAxios } from '@/lib/server/apiAxios'
import formDataToJson from '@/utils/formDataToJson'

export default function generateSubmitHandler(action:string) {
    async function handleSubmit(formData:FormData) {
        'use server'
        try {
            const response = await apiAxios.request({
                url: action,
                method: "POST",
                data: JSON.stringify(formDataToJson(formData)),
                withCredentials: true,
                headers: {
                    "Content-Type": "application/json"
                }
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