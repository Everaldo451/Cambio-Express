export function StyledForm(props:React.FormHTMLAttributes<HTMLFormElement>) {
    return (
        <form
            {...props}
            className="flex flex-col items-center"
        >
            {props.children}
        </form>
    )
}
export function FormLegend(props:React.HTMLAttributes<HTMLLegendElement>) {
    return (
        <legend
            {...props}
            className="text-center"
        >
            {props.children}
        </legend>
    )
}