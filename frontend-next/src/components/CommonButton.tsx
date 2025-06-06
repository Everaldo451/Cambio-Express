import React from "react";

interface CommonStyleProps {
    borderColor: React.CSSProperties['borderColor'],
    color: React.CSSProperties['color'],
    hoverColor: React.CSSProperties['color'],
    hoverBg: React.CSSProperties['backgroundColor'],
}

export function StyledButton(
    props:CommonStyleProps & React.DetailedHTMLProps<React.HTMLAttributes<HTMLButtonElement>, HTMLButtonElement>
) {
    return (
        <button 
            {...props}
            className={`bg-inherit p-[5px_10px] border-[1px] border-solid border-[${props.borderColor}] text-[${props.color}] transition-all duration-[0.2s] hover:cursor-pointer hover:border-transparent hover:bg-[${props.hoverBg}] hover:color-[${props.hoverColor}]`}
        >
            {props.children}
        </button>
    )
}


export function StyledInput(
    props:CommonStyleProps & React.DetailedHTMLProps<React.HTMLAttributes<HTMLInputElement>, HTMLInputElement> & React.InputHTMLAttributes<HTMLInputElement>
) {
    return (
        <input
            {...props}
            className={`bg-inherit p-[5px_10px] border-[1px] border-solid border-[${props.borderColor}] text-[${props.color}] transition-all duration-[0.2s] hover:cursor-pointer hover:border-transparent hover:bg-[${props.hoverBg}] hover:color-[${props.hoverColor}]`}
        >
            {props.children}
        </input>
    )
}

export default CommonStyleProps