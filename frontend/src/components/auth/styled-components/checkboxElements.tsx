export function CheckBoxDiv(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="flex align-center mt-[20px]"
        >
            {props.children}
        </div>
    )
}
export function CheckBoxLabel(props:React.DetailedHTMLProps<React.LabelHTMLAttributes<HTMLLabelElement>, HTMLLabelElement>) {
    return (
        <label
            {...props}
            className="text-white text-[12px] font-instrument-sans"
        >
            {props.children}
        </label>
    )
}