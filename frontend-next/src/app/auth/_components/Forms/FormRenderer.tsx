import React, { ReactNode,  useContext} from 'react'
import { useRouter } from 'next/router'

import CommonStyleProps, {StyledInput} from '@/components/CommonButton'
import LoginForm from './LoginForm'
import RegisterForm from './RegisterForm'
import GoogleButton from '../OAuth/GoogleButton'

import { UserType, TokenType } from '@/types'
import { apiAxios } from '@/axios/api'

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
    url: "login"|"register",
}

export interface onSubmitType {
    onSubmit: (e:React.FormEvent<HTMLFormElement>) => void
}

export default function FormRenderer({url, children}:FormProps) {
    const router = useRouter()

    const theme:FormThemeType["theme"] = {
        inputStyle: {
            paddingTop: 10,
            paddingLeft: 15,
            fontSize:15,
        },
        submitProps: {
            color:"white",
            hoverBg:"#2C2D52",
            borderColor:"white",
            hoverColor:"white"
        }
    }

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
        router.push("/")
    }

    return (
        <>
        {url=="register"?
            <RegisterForm onSubmit={onSubmit} theme={theme}>
                {children}
            </RegisterForm>
            :
            <LoginForm onSubmit={onSubmit} theme={theme}>
                {children}
            </LoginForm>
        }
        <GoogleButton/>
        </>
    )
}