export default function MainContentContainer(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="grid grid-cols-[auto_1fr] grid-rows-[1fr] bg-div w-[80%] max-h-[80%] m-auto p-[20px] rounded-[15px] shadow-[0_6px_10px_var(--box-shadow-theme)] "
        >
            {props.children}
        </div>
    )
}