"use client"
import React, { useState } from "react"

import InputDiv from "./InputDiv"
import { LabelPropsType } from "./Label"

type InputPropsType = {style:React.CSSProperties}

interface ContainerProps {
    inputStyle:React.CSSProperties,
    inputAttrs: React.HTMLProps<HTMLInputElement>,
    InputObject: (_:InputPropsType & {[key:string]: unknown}) => React.JSX.Element,
    LabelObject: (_:LabelPropsType & {[key:string]: unknown}) => React.JSX.Element,
}
export default function InputContainer({inputStyle,inputAttrs, InputObject, LabelObject}:ContainerProps) { 

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
            <InputObject style={inputStyle} onFocus={onFocusChange} onBlur={onFocusChange} {...inputAttrs}/>
            <LabelObject style={labelStyle} focused={focused} htmlFor={inputAttrs.id?inputAttrs.id:""}>
                {focused?Name+":":Name}
            </LabelObject>
        </InputDiv>
    )
}
