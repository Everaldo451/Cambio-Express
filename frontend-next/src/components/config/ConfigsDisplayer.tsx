export default function ConfigsDisplayer(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <section
            {...props}
            className="p-[15px] text-black"
        >
            {props.children}
        </section>
    )
}