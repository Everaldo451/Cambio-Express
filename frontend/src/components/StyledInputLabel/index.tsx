import styled from "styled-components";
import { Substitute } from "styled-components/dist/types";
import React, { DetailedHTMLProps, useState } from "react"
import { IStyledComponentBase, FastOmit } from "styled-components/dist/types";

type style = DetailedHTMLProps<React.HTMLAttributes<HTMLInputElement>,HTMLInputElement>

const InputDiv = styled.div`
    position: relative;
    margin-top: 40px;
    display:flex;
    flex-direction:column;
`

export const Label = styled.label<{style:React.CSSProperties, focused:boolean}>`

    position: absolute;
    font-size: ${(props) => 
        props.style.fontSize && typeof props.style.fontSize == "number"?
            props.focused?
                props.style.fontSize - 3:props.style.fontSize
            :15}px;
    top: ${(props) => 
        props.style.fontSize && typeof props.style.fontSize == "number" && props.focused ?
        `${- (props.style.fontSize + 4)}px`
        :'50%'};
    left: ${
        (props) => props.style && !props.focused?props.style.left:0
    }px;
    transform: ${(props) => props.focused?"none":"translate(0, -50%)"};
    color: ${(props) => props.focused?props.style.color:"white"};
    transition: all 0.5s;

    &:hover {cursor:text;}
`

export const Input = styled.input<{style:React.CSSProperties}>`
    font-size: ${(props) => props.style?props.style.fontSize:0}px;
    padding: ${(props)=> props.style?`${props.style.paddingTop}px ${props.style.paddingLeft}px`:0};

    &:focus {
        outline: none;
    }
`


type inputType = IStyledComponentBase<"web", 
    FastOmit<
        Omit<
            FastOmit<
                React.DetailedHTMLProps<
                    React.InputHTMLAttributes<HTMLInputElement>, 
                    HTMLInputElement
                >, 
                "style"
            > & {
                    ...;
                }, "ref"> & {
    ...;
}, never>> & string

interface ContainerProps {
    inputStyle:React.CSSProperties,
    inputAttrs: React.HTMLProps<HTMLInputElement>,

    InputObject:  IStyledComponentBase<
        "web", 
        Substitute<React.DetailedHTMLProps<React.InputHTMLAttributes<HTMLInputElement>, HTMLInputElement>, {
            style: React.CSSProperties;
        }>
    > & string,

    LabelObject: IStyledComponentBase<
        "web", 
        Substitute<React.DetailedHTMLProps<React.LabelHTMLAttributes<HTMLLabelElement>, HTMLLabelElement>, {
            style: React.CSSProperties;
            focused: boolean;
        }>
    > & string,
}

export function InputContainer({inputStyle,inputAttrs, InputObject, LabelObject}:ContainerProps) { 

    const [focused, setFocused] = useState<boolean>(false)

    const labelStyle:React.CSSProperties = {
        left: inputStyle.paddingLeft,
        fontSize: inputStyle.fontSize,
        top: inputStyle.paddingTop
    }

    function onFocusChange (event:React.FocusEvent<HTMLInputElement, Element>) {
        if (event.currentTarget.value.length == 0) {setFocused(!focused)}
    }

    const Name = inputAttrs.name?inputAttrs.name[0].toUpperCase() + inputAttrs.name.slice(1,inputAttrs.name.length):""
    
    return (

        <InputDiv>
            <InputObject style={inputStyle} onFocus={onFocusChange} onBlur={onFocusChange} {...inputAttrs}/>
            <LabelObject style={labelStyle} focused={focused} htmlFor={inputAttrs.id?inputAttrs.id:""}>
                {focused?Name+":":Name}
            </LabelObject>
        </InputDiv>
    )
}
