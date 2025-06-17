"use client"

import { useEffect, useRef, ComponentProps, useState } from 'react'

import {StyledInput} from '@/components/CommonButton'
import { Label, Input} from '@/components/StyledInputLabel'


function omit<T extends object, K extends keyof T>(object:T, keys:K[]) {
    const copy = {...object}
    for (const key of keys) {
        delete copy[key]
    }
    return copy
}


export function AuthLabel(props:ComponentProps<typeof Label>) {
    return (
        <Label {...props} className='font-instrument-sans'/>
    )
}


export function AuthInput(props:ComponentProps<typeof Input>) {
    return (
        <Input {...props} className="bg-transparent text-[#BEC1C1] font-instrument-sans border-solid border-b-[2px] border-b-white"/>
    )
}


export function AuthSubmitInput(props:ComponentProps<typeof StyledInput>) {
    return (
        <StyledInput {...props} className="mt-[40px]"/>
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