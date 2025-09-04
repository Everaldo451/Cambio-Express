export type InputPropsType = {style:React.CSSProperties}

function getInputClassname(
    _props:InputPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLInputElement>, HTMLInputElement>
) {
    return (
        "focus:outline-none"
    )
}
export default function Input(props:InputPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLInputElement>, HTMLInputElement>) {
    const { style, ...nonStyleProps } = props
    return (
        <input 
            {...nonStyleProps}
            style={{
                fontSize: style.fontSize,
                padding: `${style.paddingTop}px ${style.paddingLeft}px`
            }}
            className={props.className?props.className+ " " + getInputClassname(props):getInputClassname(props)}
        >
            {props.children}
        </input>
    )
}
