"use client"

import React, { InputHTMLAttributes, useState } from "react"

function InputDiv(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div {...props} className="flex flex-col relative mt-[40px]">{props.children}</div>
    )
}
type InputPropsType = {style:React.CSSProperties}
type LabelPropsType = {style:React.CSSProperties, focused:boolean}

export function getLabelClassname(
    props:LabelPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLLabelElement>, HTMLLabelElement>
) {
    return `absolute transition-all duration-[0.5s] hover:cursor-pointer` + 
        props.focused?
        ` text-[${(props.style.fontSize as number) -3}px] top-[${-((props.style.fontSize as number) + 4)}px] left-[0px] text-[${props.style.color}] transform-none`
        :` text-[${(props.style.fontSize as number)}px] top-[50%] left-[${props.style.left}px] text-white transform-[translate(0,_-50%)]`
}
export function Label(props:LabelPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLLabelElement>, HTMLLabelElement>) {
    return (
        <label 
            {...props}
            className={getLabelClassname(props)}
        >
            {props.children}
        </label>
    )

}


export function getInputClassname(
    props:InputPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLInputElement>, HTMLInputElement>
) {
    return (
        `text-[${props.style.fontSize as number}px] p-[${props.style.paddingTop as number}px_${props.style.paddingLeft as number}px] focus:outline-none`
    )
}
export function Input(props:InputPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLInputElement>, HTMLInputElement>) {
    return (
        <input 
            {...props}
            className={getInputClassname(props)}
        >
            {props.children}
        </input>
    )
}


interface ContainerProps {
    inputStyle:React.CSSProperties,
    inputAttrs: React.HTMLProps<HTMLInputElement>,
    InputObject: (props:InputPropsType & {[key:string]: any}) => React.JSX.Element,
    LabelObject: (props:LabelPropsType & {[key:string]: any}) => React.JSX.Element,
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
            <InputObject style={inputStyle} onFocus={onFocusChange} onBlur={onFocusChange} {...inputAttrs}/>
            <LabelObject style={labelStyle} focused={focused} htmlFor={inputAttrs.id?inputAttrs.id:""}>
                {focused?Name+":":Name}
            </LabelObject>
        </InputDiv>
    )
}
