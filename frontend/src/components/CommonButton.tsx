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
    const {borderColor, color, hoverBg, hoverColor, ...otherProps} = props
    const style = `bg-inherit p-[5px_10px] border-[1px] border-solid border-[${borderColor}] text-[${color}] transition-all duration-[0.2s] hover:cursor-pointer hover:border-transparent hover:bg-[${hoverBg}] hover:text-[${hoverColor}]`
    return (
        <button 
            {...otherProps}
            className={otherProps.className?otherProps.className + " " + style:style}
        >
            {otherProps.children}
        </button>
    )
}


export function StyledInput(
    props:CommonStyleProps & React.DetailedHTMLProps<React.HTMLAttributes<HTMLInputElement>, HTMLInputElement> & React.InputHTMLAttributes<HTMLInputElement>
) {
    const {borderColor, color, hoverBg, hoverColor, ...otherProps} = props
    const style = `bg-inherit p-[5px_10px] border-[1px] border-solid border-[${borderColor}] text-[${color}] transition-all duration-[0.2s] hover:cursor-pointer hover:border-transparent hover:bg-[${hoverBg}] hover:text-[${hoverColor}]`
    return (
        <input
            {...otherProps}
            className={otherProps.className?otherProps.className + " " + style:style}
        >
            {otherProps.children}
        </input>
    )
}

export default CommonStyleProps