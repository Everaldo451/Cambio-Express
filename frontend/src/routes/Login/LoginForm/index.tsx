import styled from 'styled-components'
import React, { ReactNode, useState, useContext, useEffect, act } from 'react'
import { CSRFContext } from '../../../main'
import CommonStyleProps, { StyledInput } from '../../../components/CommonButton'

interface InputStyleType {
    top: number,
    left: number,
    fontSize:number,
}

const InputDiv = styled.div`
    position: relative;
    margin-top: 40px;
    display:flex;
    flex-direction:column;
`

const Label = styled.label<{inputStyle:InputStyleType, focused:boolean}>`
    position: absolute;
    font-size: ${(props) => 
        props.inputStyle?
            props.focused?
                props.inputStyle.fontSize - 3:
                props.inputStyle.fontSize
            :0}px;
    top: ${(props) => props.inputStyle && props.focused?`${- (props.inputStyle.fontSize + 4)}px`:'50%'};
    left: ${
        (props) => props.inputStyle && !props.focused?props.inputStyle.left:0
    }px;
    transform: ${(props) => props.focused?"none":"translate(0, -50%)"};
    color: ${(props) => props.focused?"black":"gray"};
    transition: all 0.5s;

    &:hover {cursor:text;}
`

const Input = styled.input<{inputStyle:InputStyleType}>`
    font-size: ${(props) => props.inputStyle?props.inputStyle.fontSize:0}px;
    padding: ${(props)=> props.inputStyle?`${props.inputStyle.top}px ${props.inputStyle.left}px`:0}
`

const SubmitInput = styled(StyledInput)`
    margin-top: 20px;
`

interface ContainerProps {
    inputStyle:InputStyleType,
    inputAttrs: React.HTMLProps<HTMLInputElement>
}

function InputContainer({inputStyle,inputAttrs}:ContainerProps) { 

    const [focused, setFocused] = useState<boolean>(false)

    function onFocusChange (event:React.FocusEvent<HTMLInputElement, Element>) {
        if (event.currentTarget.value.length == 0) {setFocused(!focused)}
    }

    const Name = inputAttrs.name?inputAttrs.name[0].toUpperCase() + inputAttrs.name.slice(1,inputAttrs.name.length):""

    return (
        <InputDiv>
            <Label inputStyle={inputStyle} focused={focused} htmlFor={inputAttrs.id?inputAttrs.id:""}>{focused?Name+":":Name}</Label>
            <Input inputStyle={inputStyle} {...inputAttrs} onFocus={onFocusChange} onBlur={onFocusChange}/>
        </InputDiv>
    )
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
    console.log(csrf)

    const inputStyle:InputStyleType = {
        top: 10,
        left: 20,
        fontSize:15,
    }

    const submitProps:CommonStyleProps = {
        color:"black",
        hoverBg:"darkorange",
        borderColor:"black",
        hoverColor:"white"
    }

    return (
        <StyledForm action={`api/auth/${url}/`} method='POST'>
            {children}
            {url == "register"?
            <InputContainer 
                inputStyle={inputStyle} 
                inputAttrs={{name:"username",id:"username",required: true}}
            />
            :null}
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