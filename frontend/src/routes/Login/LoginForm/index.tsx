import styled from 'styled-components'
import { ReactNode, useState, useContext, useEffect } from 'react'
import { CSRFContext } from '../../../main'

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
`

const Input = styled.input<{inputStyle:InputStyleType}>`
    font-size: ${(props) => props.inputStyle?props.inputStyle.fontSize:0}px;
    padding: ${(props)=> props.inputStyle?`${props.inputStyle.top}px ${props.inputStyle.left}px`:0}
`

interface ContainerProps {
    inputStyle:InputStyleType,
    name:string,
}

function InputContainer({inputStyle,name}:ContainerProps) { 

    const [focused, setFocused] = useState<boolean>(false)

    function onFocusChange (event:React.FocusEvent<HTMLInputElement, Element>) {
        if (event.currentTarget.value.length == 0) {setFocused(!focused)}
    }

    const Name = name[0].toUpperCase() + name.slice(1,name.length)

    return (
        <InputDiv>
            <Label inputStyle={inputStyle} focused={focused} htmlFor={name}>{focused?Name+":":Name}</Label>
            <Input inputStyle={inputStyle} name={name} id={name} onFocus={onFocusChange} onBlur={onFocusChange}/>
        </InputDiv>
    )
}

const StyledForm = styled.form`
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

    const inputStyle:InputStyleType = {
        top: 10,
        left: 20,
        fontSize:15,
    }

    return (
        <StyledForm action={`http://localhost:8000/auth/${url}`} method='POST'>
            {children}
            {url == "register"?
            <InputContainer inputStyle={inputStyle} name='username'/>
            :null}
            <InputContainer inputStyle={inputStyle} name='email'/>
            <InputContainer inputStyle={inputStyle} name='password'/>
            <input type="hidden" name='csrfmiddlewaretoken' value={csrf?csrf:""}/>
        </StyledForm>
    )

}

export default LoginForm