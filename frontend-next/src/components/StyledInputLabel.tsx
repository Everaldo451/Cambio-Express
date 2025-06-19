"use client"

import React, { useState } from "react"

function InputDiv(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div {...props} className="flex flex-col relative mt-[30px]">{props.children}</div>
    )
}
type InputPropsType = {style:React.CSSProperties}
type LabelPropsType = {style:React.CSSProperties, focused:boolean}

function getLabelClassname(
    props:LabelPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLLabelElement>, HTMLLabelElement>
) {
    return "absolute transition-all duration-[0.5s] hover:cursor-text"
}
export function Label(props:LabelPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLLabelElement>, HTMLLabelElement>) {
    const { style, focused, ...nonStyleProps } = props
    return (
        <label 
            {...nonStyleProps}
            style={focused?
                {
                    fontSize: (style.fontSize as number) -3,
                    top: -((style.fontSize as number) + 4),
                    left: 0,
                    color: style.color,
                    transform: "none",
                }:{
                    fontSize: (style.fontSize as number),
                    top: "50%",
                    left: props.style.left,
                    color: "white",
                    transform: "translate(0, -50%)"
                }
            }
            className={props.className?
                props.className+ " " + getLabelClassname(props)
                :getLabelClassname(props)
            }
        >
            {props.children}
        </label>
    )
}


function getInputClassname(
    props:InputPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLInputElement>, HTMLInputElement>
) {
    return (
        "focus:outline-none"
    )
}
export function Input(props:InputPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLInputElement>, HTMLInputElement>) {
    const { style, ...nonStyleProps } = props
    return (
        <input 
            {...nonStyleProps}
            style={{
                fontSize: style.fontSize,
                padding: `${style.paddingTop}px ${style.paddingLeft}px`
            }}
            className={props.className?props.className+ " " + getInputClassname(props):getInputClassname(props)}
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
