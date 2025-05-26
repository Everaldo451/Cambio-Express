import Link from "next/link"

export function ConfigSection(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="grid grid-cols-[auto_1fr] grid-rows-[1fr] bg-div w-[80%] max-h-[80%] m-auto p-[20px] rounded-[15px] shadow-[0_6px_10px_var(--box-shadow-theme)] "
        >
            {props.children}
        </div>
    )
}


export function MenuButtonsContainer(props:React.HTMLAttributes<HTMLDivElement>) {
    const containerStyle = `
        grid relative grid-cols-[1fr] auto-rows-auto grid-flow-row bg-[rgb(240,_240,_240)] overflow-auto
    `
    const afterPseudoElementStyle = `
        after:content-[""] after:absolute after:w-[2px] h-[100%] bg-black right-[0];
    `
    return (
        <section
            {...props}
            className={[containerStyle, afterPseudoElementStyle].join("\s").replace("\n", "\s")}
        >
            {props.children}
        </section>
    )
}


export function ConfigRoute(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <section
            {...props}
            className="p-[15px]"
        >
            {props.children}
        </section>
    )
}


export function StyledLink(props:React.ComponentProps<typeof Link>) {
    return (
        <Link
            {...props}
            className="relative bg-inherit p-[10px] text-[15px] hover:bg-[lightgray] hover:cursor-pointer"
        >
            {props.children}
        </Link>
    )
}