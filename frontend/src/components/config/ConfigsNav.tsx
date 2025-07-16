export default function ConfigsNav(props:React.HTMLAttributes<HTMLDivElement>) {
    const containerStyle = `
        grid relative grid-cols-[1fr] bg-gray-400 auto-rows-auto grid-flow-row bg-[rgb(240,_240,_240)] overflow-auto
    `
    const afterPseudoElementStyle = `
        after:content-[""] after:absolute after:w-[2px] after:h-[100%] after:bg-black after:right-[0]
    `
    return (
        <nav
            {...props}
            className={[containerStyle, afterPseudoElementStyle].join(" ").replace("\n", " ")}
        >
            {props.children}
        </nav>
       
    )
}