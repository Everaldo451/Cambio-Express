import { SetStateAction, ReactNode } from "react";
import { FormProps } from "./Forms/FormRenderer";

function CustomizedButton(props:React.HTMLAttributes<HTMLButtonElement>) {
    const buttonStyle = `
        relative z-[1] bg-[#8C8A6C] text-white p-[3px] transition-all duration-[0.5s] border-solid border-y-[2px] border-y-white
        hover:cursor-pointer hover:transform-[scale(1.1)]
    `
    const afterPseudoElementStyle = `
        after:content-[""] after:absolute after:bg-white after:w-[2px] after:h-[0] after:top-[calc(100%_+_2px)] after:left-[-2px] after:transition-all after:duration-[0.5s]
        hover:after:h-[calc(100%_+_4px)] hover:after:top-[-2px]
    `
    const beforePseudoElementStyle = `
        before:content-[""] before:absolute before:bg-white before:w-[2px] before:h-[0] before:top-[-2px] before:right-[-2px] before:transition-all before:duration-[0.5s]
        hover:before:h-[calc(100%_+_4px)]
    `
    return (
        <button
            {...props}
            className={
                [buttonStyle, afterPseudoElementStyle, beforePseudoElementStyle].join("\s").replace("\n","\s")
            }
        >
            {props.children}
        </button>
    )
}

function StyledDiv(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="grid w-full grid-rows-[auto] grid-cols-[repeat(2,_1fr)] grid-flow-col gap-[20px]"
        >
            {props.children}
        </div>
    )
}

interface ChangeURLProps {
    children?: ReactNode,
    setURL: React.Dispatch<SetStateAction<FormProps['url']>>,
    url?: FormProps['url']
}


function ChangeURLButton({children,setURL,url}:ChangeURLProps) {

    return <CustomizedButton onClick={(e) => {url?setURL(url):null}}>{children?children:""}</CustomizedButton>
    
}

export default function ChangeFormURL({setURL}:ChangeURLProps) {

    return (
        <StyledDiv>
            <ChangeURLButton setURL={setURL} url="login">Entrar</ChangeURLButton>
            <ChangeURLButton setURL={setURL} url="register">Registrar</ChangeURLButton>
        </StyledDiv>
    )

}