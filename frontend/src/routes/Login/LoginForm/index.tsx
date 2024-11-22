import styled from 'styled-components'
import React, { ReactNode, useState, useContext } from 'react'
import { useNavigate } from 'react-router-dom'
import { CSRFContext, JWTContext } from '../../../main'
import CommonStyleProps, { StyledInput } from '../../../components/CommonButton'
import axios from 'axios'
import { InputContainer, Label, Input } from '../../../components/StyledInputLabel'

const InputDiv = styled.div`
    position: relative;
    margin-top: 30px;
    display:flex;
    flex-direction:column;
`

const NInput = styled(Input)`
    background-color: transparent;
    border: none;
    border-bottom: 1px solid white;
    color: #BEC1C1;
`

const SubmitInput = styled(StyledInput)`
    margin-top: 40px;
`

const StyledForm = styled.form`
    display: flex;
    flex-direction: column;
    align-items: center;

    & legend {
        text-align: center;
    }
`

export interface FormProps {
    children?: ReactNode,
    url: "login"|"register",
}

function LoginForm ({children,url}:FormProps) {

    const [csrf] = useContext(CSRFContext)
    const [_, setJwt] = useContext(JWTContext)
    const navigate = useNavigate()

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

    const inputStyle:React.CSSProperties= {
        paddingTop: 10,
        paddingLeft: 15,
        fontSize:15,
    }

    const submitProps:CommonStyleProps = {
        color:"white",
        hoverBg:"#2C2D52",
        borderColor:"white",
        hoverColor:"white"
    }

    return (
        <StyledForm action={`api/auth/${url}/`} method='POST' onSubmit={onSubmit}>
            {children}
                {url == "register"?
                    <InputContainer 
                        inputStyle={inputStyle} 
                        inputAttrs={{name:"full_name",id:"full_name",required: true}}
                        InputObject={NInput}
                        LabelObject={Label}
                    />
                :null
                }
            <InputContainer 
                inputStyle={inputStyle} 
                inputAttrs={{name:"email",id:"email",required: true}}
                InputObject={NInput}
                LabelObject={Label}
            />
            <InputContainer 
                inputStyle={inputStyle} 
                inputAttrs={{name:"password",id:"password",required: true}}
                InputObject={NInput}
                LabelObject={Label}
            />
            <input type="hidden" name='csrfmiddlewaretoken' value={csrf?csrf:""}/>
            <SubmitInput {...submitProps} type='submit' value="Enter"/>
        </StyledForm>
    )

}

export default LoginForm