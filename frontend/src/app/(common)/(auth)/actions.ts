"use server"

import { redirect } from 'next/navigation'
import { cookies } from 'next/headers'

import { TokenType } from '@/types'
import { apiAxios } from '@/lib/server/apiAxios'
import formDataToJson from '@/utils/formDataToJson'

async function createTokenCookies(data: {[key:string]: any}) {
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

export async function registerUser(formData:FormData) {
    try {
        const response = await apiAxios.request({
            url: "/users/",
            method: "POST",
            data: JSON.stringify(formDataToJson(formData)),
            withCredentials: true,
            headers: {
                "Content-Type": "application/json"
            }
        })
        const data = response.data
        if (data instanceof Object && "tokens" in data) {
            await createTokenCookies(data)
        }
    } catch (error) {
        console.log(error)
    }
    redirect("/")
}

export async function loginUser(formData:FormData) {
    try {
        const response = await apiAxios.request({
            url: "/auth/login/",
            method: "POST",
            data: JSON.stringify(formDataToJson(formData)),
            withCredentials: true,
            headers: {
                "Content-Type": "application/json"
            }
        })
        const data = response.data
        if (data instanceof Object && "tokens" in data) {
            await createTokenCookies(data)
        }
    } catch (error) {
        console.log(error)
    }
    redirect("/")
}