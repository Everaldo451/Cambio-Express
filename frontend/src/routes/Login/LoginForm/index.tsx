import styled from 'styled-components'
import React, { ReactNode, useState, useContext } from 'react'
import { useNavigate } from 'react-router-dom'
import { CSRFContext, JWTContext } from '../../../main'
import CommonStyleProps, { StyledInput } from '../../../components/CommonButton'
import axios from 'axios'
import { InputContainer, Label, Input } from '../../../components/StyledInputLabel'

interface InputStyleType {
    top: number,
    left: number,
    fontSize:number,
}

const InputDiv = styled.div`
    position: relative;
    margin-top: 30px;
    display:flex;
    flex-direction:column;
`
/*
    font-size: ${(props) => props.style?props.style.fontSize:0}px;
    padding: ${(props)=> props.style?`${props.style.paddingTop}px ${props.style.paddingLeft}px`:0};

    &:focus {
        outline: none;
    }
*/

const NInput = styled(Input)`
    background-color: transparent;
    border: none;
    border-bottom: 1px solid white;
    color: #BEC1C1;
`

const SubmitInput = styled(StyledInput)`
    margin-top: 40px;
`

interface ContainerProps {
    inputStyle:InputStyleType,
    inputAttrs: React.HTMLProps<HTMLInputElement>
}

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

    const inputStyle:InputStyleType = {
        top: 10,
        left: 15,
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
                inputAttrs={{name:"Full Name",id:"full_name",required: true}}
                InputObject={NInput}
            />
            :null}
            <Ninput/>
            <InputContainer 
                inputStyle={inputStyle} 
                inputAttrs={{name:"email",id:"email",required: true}}
            />
            <InputContainer 
                inputStyle={inputStyle} 
                inputAttrs={{name:"password",id:"password",required: true}}
            />
            <input type="hidden" name='csrfmiddlewaretoken' value={csrf?csrf:""}/>
            <SubmitInput {...submitProps} type='submit' value="Enter"/>
        </StyledForm>
    )

}

export default LoginForm