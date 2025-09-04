export default function InputDiv(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div {...props} className="flex flex-col relative mt-[30px]">{props.children}</div>
    )
}