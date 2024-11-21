import styled from "styled-components";
import { Substitute } from "styled-components/dist/types";
import React, { DetailedHTMLProps, useState } from "react"

type style = DetailedHTMLProps<React.HTMLAttributes<HTMLInputElement>,HTMLInputElement>

const InputDiv = styled.div`
    position: relative;
    margin-top: 40px;
    display:flex;
    flex-direction:column;
`

export const Label = styled.label<{inputStyle:React.CSSProperties, focused:boolean}>`

    position: absolute;
    font-size: ${(props) => 
        props.inputStyle.fontSize && typeof props.inputStyle.fontSize == "number"?
            props.focused?
                props.inputStyle.fontSize - 3:props.inputStyle.fontSize
            :15}px;
    top: ${(props) => 
        props.inputStyle.fontSize && typeof props.inputStyle.fontSize == "number" && props.focused ?
        `${- (props.inputStyle.fontSize + 4)}px`
        :'50%'};
    left: ${
        (props) => props.inputStyle && !props.focused?props.inputStyle.left:0
    }px;
    transform: ${(props) => props.focused?"none":"translate(0, -50%)"};
    color: ${(props) => props.focused?props.inputStyle.color:"white"};
    transition: all 0.5s;

    &:hover {cursor:text;}
`

export const Input = styled.input<{inputStyle:React.CSSProperties}>`
    font-size: ${(props) => props.inputStyle?props.inputStyle.fontSize:0}px;
    padding: ${(props)=> props.inputStyle?`${props.inputStyle.paddingTop}px ${props.inputStyle.paddingLeft}px`:0};

    &:focus {
        outline: none;
    }
`

interface ContainerProps {

    inputStyle:React.CSSProperties,
    inputAttrs: React.HTMLProps<HTMLInputElement>,
    inputObject:  JSX.Element,
    labelObject: JSX.Element,
}

export function InputContainer({inputStyle,inputAttrs, inputObject, labelObject}:ContainerProps) { 

    const [focused, setFocused] = useState<boolean>(false)

    const LabelStyle:React.CSSProperties = {
        left: inputStyle.paddingLeft,
        fontSize: inputStyle.fontSize,
        top: inputStyle.paddingTop
    }

    function onFocusChange (event:React.FocusEvent<HTMLInputElement, Element>) {
        if (event.currentTarget.value.length == 0) {setFocused(!focused)}
    }

    const Name = inputAttrs.name?inputAttrs.name[0].toUpperCase() + inputAttrs.name.slice(1,inputAttrs.name.length):""
    

    const inputClone = React.cloneElement(inputObject, {
        inputStyle:inputStyle, 
        ...inputAttrs, 
        onFocus:onFocusChange, 
        onBlur:onFocusChange
    })

    const labelClone = React.cloneElement(labelObject, {
        inputStyle:LabelStyle, 
        focused:focused, 
        htmlFor:inputAttrs.id?inputAttrs.id:"", 
        children:<>{focused?Name+":":Name}</>
    })

    return (

        <InputDiv>
            {inputClone}
            {labelClone}
        </InputDiv>
    )
}
