import styled from "styled-components";
import React, { useState } from "react"

const InputDiv = styled.div`
    position: relative;
    margin-top: 40px;
    display:flex;
    flex-direction:column;
`
type inputPropsType = {Style:React.CSSProperties}
type labelPropsType = {Style:React.CSSProperties, focused:boolean}


export const Label = styled.label<labelPropsType>`

    position: absolute;
    font-size: ${(props) => 
        props.Style.fontSize && typeof props.Style.fontSize == "number"?
            props.focused?
                props.Style.fontSize - 3:props.Style.fontSize
            :15}px;
    top: ${(props) => 
        props.Style.fontSize && typeof props.Style.fontSize == "number" && props.focused?
        `${- (props.Style.fontSize + 4)}px`
        :'50%'};
    left: ${
        (props) => props.Style && !props.focused?props.Style.left:0
    }px;
    transform: ${(props) => props.focused?"none":"translate(0, -50%)"};
    color: ${(props) => props.focused?props.Style.color:"white"};
    transition: all 0.5s;

    &:hover {cursor:text;}
`

export const Input = styled.input<inputPropsType>`
    font-size: ${(props) => props.Style?props.Style.fontSize:0}px;
    padding: ${(props)=> props.Style?`${props.Style.paddingTop}px ${props.Style.paddingLeft}px`:0};

    &:focus {
        outline: none;
    }
`


interface ContainerProps {
    inputStyle:React.CSSProperties,
    inputAttrs: React.HTMLProps<HTMLInputElement>,
    InputObject: (props:inputPropsType & {[key:string]: any}) => JSX.Element,
    LabelObject: (props:labelPropsType & {[key:string]: any}) => JSX.Element,
}

export function InputContainer({inputStyle,inputAttrs, InputObject, LabelObject}:ContainerProps) { 

    const [focused, setFocused] = useState<boolean>(false)

    const labelStyle:React.CSSProperties = {
        left: inputStyle.paddingLeft,
        fontSize: inputStyle.fontSize,
        color: "white"
    }

    function onFocusChange (event:React.FocusEvent<HTMLInputElement, Element>) {
        if (event.currentTarget.value.length == 0) {setFocused(!focused)}
    }

    
    let Name = inputAttrs.name?inputAttrs.name:""
    if (Name.includes("_")) {
        console.log(true)
        let n = ""
        for (const v of Name.split("_")) {
            console.log(Name.split("_"))
            n += v[0].toUpperCase() + v.slice(1,v.length) + " "
        }
        Name = n
    } else {
        Name = Name[0].toUpperCase() + Name.slice(1,Name.length)
    }
        
    return (

        <InputDiv>
            <InputObject Style={inputStyle} onFocus={onFocusChange} onBlur={onFocusChange} {...inputAttrs}/>
            <LabelObject Style={labelStyle} focused={focused} htmlFor={inputAttrs.id?inputAttrs.id:""}>
                {focused?Name+":":Name}
            </LabelObject>
        </InputDiv>
    )
}
