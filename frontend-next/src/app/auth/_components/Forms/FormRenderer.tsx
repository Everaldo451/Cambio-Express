import React, { ReactNode,  useContext} from 'react'
import { useRouter } from 'next/router'

import CommonStyleProps, {StyledInput} from '@/components/CommonButton'
import LoginForm from './LoginForm'
import RegisterForm from './RegisterForm'
import GoogleButton from '../OAuth/GoogleButton'

import { UserType } from '@/types'

import axios from 'axios'

export type FormThemeType = {
    theme: {
        inputStyle: React.CSSProperties,
        submitProps: CommonStyleProps
    }
}

interface TokenType {
    value: string,
    lifetime: number
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
            const response = await axios.request({
                url: e.currentTarget.action,
                method: e.currentTarget.method,
                data: new FormData(e.currentTarget),
                withCredentials: true,
            })
            const data = response.data
            const tokens = data.get("tokens")
            if (data satisfies AuthenticationFormat) {
                const tokens = data["tokens"]
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