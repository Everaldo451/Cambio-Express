import { ComponentProps } from "react";
import Link from "next/link";

function CustomizedLink(props:ComponentProps<typeof Link>) {
    const linkStyle = `
        relative z-[1] bg-[#8C8A6C] text-white text-[14px] text-center p-[3px_10px] transition-all duration-[0.5s] border-solid border-y-[2px] border-y-white
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
        <Link
            {...props}
            className={
                [linkStyle, afterPseudoElementStyle, beforePseudoElementStyle].join(" ").replace("\n"," ")
            }
        >
            {props.children}
        </Link>
    )
}

function StyledDiv(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="grid grid-rows-[auto] grid-cols-[repeat(2,_1fr)] grid-flow-col gap-[20px]"
        >
            {props.children}
        </div>
    )
}


export default function ChangeRouteButtons() {

    return (
        <StyledDiv>
            <CustomizedLink href={"/login"}>Entrar</CustomizedLink>
            <CustomizedLink href={"/signup"}>Registrar</CustomizedLink>
        </StyledDiv>
    )
}