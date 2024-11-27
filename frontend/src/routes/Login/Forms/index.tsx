import React, { ReactNode,  useContext} from 'react'
import styled from 'styled-components'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { JWTContext } from '../../../main'
import CommonStyleProps, { StyledInput } from '../../../components/CommonButton'
import { Label, Input } from '../../../components/StyledInputLabel'
import LoginForm from './LoginForm'
import RegisterForm from './RegisterForm'


export type FormThemeType = {

    theme: {
        inputStyle: React.CSSProperties,
        submitProps: CommonStyleProps
    }
}


export const NLabel = styled(Label)`
    font-family: ${props => props.theme.fontFamily};
`

export const NInput = styled(Input)`
    background-color: transparent;
    border: none;
    border-bottom: 1px solid white;
    color: #BEC1C1;
    font-family: ${props => props.theme.fontFamily};
`

export const SubmitInput = styled(StyledInput)`
    margin-top: 40px;
`

export const StyledForm = styled.form`
    display: flex;
    flex-direction: column;
    align-items: center;

    & legend {
        text-align: center;
    }
`

export const CheckBoxDiv = styled.div`
    margin-top:20px;
    display: flex;
    align-items: center;

    & label {
        color: white;
        font-family: ${props => props.theme.fontFamily};
        font-size: 12px;
    }

`
export interface FormProps {
    children?: ReactNode,
    url: "login"|"register",
}

export interface onSubmitType {
    onSubmit: (e:React.FormEvent<HTMLFormElement>) => void
}

export default function FormRenderer({url, children}:FormProps) {

    const [_, setJwt] = useContext(JWTContext)
    const navigate = useNavigate()

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

            setJwt(response.data)
            navigate("/")
        } catch (error) {
            console.log(error)
            navigate("/")
        }
    }

    return (
        <>
        {url=="register"?
            <RegisterForm url={url} onSubmit={onSubmit} theme={theme}>
                {children}
            </RegisterForm>
            :
            <LoginForm url={url} onSubmit={onSubmit} theme={theme}>
                {children}
            </LoginForm>
        }
        </>
    )
}