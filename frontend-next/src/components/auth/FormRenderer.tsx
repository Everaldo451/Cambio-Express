"use client";
import React, { ReactNode } from 'react'
import { redirect } from 'next/navigation'

import CommonStyleProps from '@/components/CommonButton'
import { StyledForm } from '@/components/auth/styled-components'

import { UserType, TokenType } from '@/types'
import { apiAxios } from '@/lib/axios/api'

export type FormThemeType = {
    theme: {
        inputStyle: React.CSSProperties,
        submitProps: CommonStyleProps
    }
}

interface AuthenticationFormat {
    user: UserType,
    tokens: {
        refresh_token: TokenType,
        access_token: TokenType
    }
}

export interface FormProps {
    children?: ReactNode,
}

export interface onSubmitType {
    onSubmit: (e:React.FormEvent<HTMLFormElement>) => void
}

export default function FormRenderer(props:React.ComponentProps<typeof StyledForm>) {

    async function onSubmit(e:React.FormEvent<HTMLFormElement>) {
        e.preventDefault()
        try {
            const response = await apiAxios.request({
                url: e.currentTarget.action,
                method: e.currentTarget.method,
                data: new FormData(e.currentTarget),
                withCredentials: true,
            })
            const data = response.data
            if (data instanceof Object && "tokens" in data) {
                const tokens = data["tokens"]
                if ("access_token" in tokens) {
                    const accessToken = tokens["access_token"] as TokenType
                    document.cookie = `access_token=${accessToken.value}`
                }
                if ("refresh_token" in tokens) {
                    const refreshToken = tokens["refresh_token"] as TokenType
                    document.cookie = `refresh_token=${refreshToken.value}`
                }
            }
        } catch (error) {
            console.log(error)
        }
        redirect("/")
    }

    return (
        <StyledForm
            onSubmit={onSubmit}
            {...props}
        >
            {props.children}
        </StyledForm>
    )
}