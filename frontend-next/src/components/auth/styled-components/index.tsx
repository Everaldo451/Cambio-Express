"use client"

import { useEffect, useRef, ComponentProps, useState } from 'react'

import {StyledInput} from '@/components/CommonButton'
import { Label, Input } from '@/components/StyledInputLabel'


export function NLabel(props:ComponentProps<typeof Label>) {
    const labelRef = useRef<HTMLLabelElement|null>(null)
    const labelElement = <Label {...props} ref={labelRef}></Label>
    const [currentStyle, setCurrentStyle] = useState<string|null>(null)

    useEffect(() => {
        setCurrentStyle(prev => labelRef.current?labelRef.current.className:prev)
    }, [labelRef])

    return (
        <label
            {...props}
            className={"font-instrument-sans" + currentStyle}
        >
            {props.children}
        </label>
    )
}


export function NInput(props:ComponentProps<typeof Input>) {
    const inputRef = useRef<HTMLInputElement|null>(null)
    const inputElement = <Input {...props} ref={inputRef}></Input>
    const [currentStyle, setCurrentStyle] = useState<string|null>(null)

    useEffect(() => {
        setCurrentStyle(prev => inputRef.current?inputRef.current.className:prev)
    }, [inputRef])

    return (
        <input
            {...props}
            className={
                "bg-transparent text-[#BEC1C1] font-instrument-sans border-solid border-b-[2px] border-b-white" + currentStyle
            }
        >
            {props.children}
        </input>
    )
}


export function SubmitInput(props:ComponentProps<typeof StyledInput>) {
    const submitInputRef = useRef<HTMLInputElement|null>(null)
    const submitInputElement = <StyledInput {...props} ref={submitInputRef}></StyledInput>
    const [currentStyle, setCurrentStyle] = useState<string|null>(null)

    useEffect(() => {
        setCurrentStyle(prev => submitInputRef.current?submitInputRef.current.className:prev)
    }, [submitInputRef])

    return (
        <input
            {...props}
            className={
                "mt-[40px]" + currentStyle
            }
        >
            {props.children}
        </input>
    )
}

//Form Elements
export function StyledForm(props:React.FormHTMLAttributes<HTMLFormElement>) {
    return (
        <form
            {...props}
            className="flex flex-col align-center"
        >
            {props.children}
        </form>
    )
}
export function FormLegend(props:React.HTMLAttributes<HTMLLegendElement>) {
    return (
        <legend
            {...props}
            className="text-center"
        >
            {props.children}
        </legend>
    )
}

//Checkbox Elements
export function CheckBoxDiv(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="flex align-center mt-[20px]"
        >
            {props.children}
        </div>
    )
}
export function CheckBoxLabel(props:React.DetailedHTMLProps<React.LabelHTMLAttributes<HTMLLabelElement>, HTMLLabelElement>) {
    return (
        <label
            {...props}
            className="text-white text-[12px] font-instrument-sans"
        >
            {props.children}
        </label>
    )
}