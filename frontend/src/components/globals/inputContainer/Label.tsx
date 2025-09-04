export type LabelPropsType = {style:React.CSSProperties, focused:boolean}

function getLabelClassname(
    _props:LabelPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLLabelElement>, HTMLLabelElement>
) {
    return "absolute transition-all duration-[0.5s] hover:cursor-text"
}
export default function Label(props:LabelPropsType & React.DetailedHTMLProps<React.HTMLAttributes<HTMLLabelElement>, HTMLLabelElement>) {
    const { style, focused, ...nonStyleProps } = props
    return (
        <label 
            {...nonStyleProps}
            style={focused?
                {
                    fontSize: (style.fontSize as number) -3,
                    top: -((style.fontSize as number) + 4),
                    left: 0,
                    color: style.color,
                    transform: "none",
                }:{
                    fontSize: (style.fontSize as number),
                    top: "50%",
                    left: props.style.left,
                    color: "white",
                    transform: "translate(0, -50%)"
                }
            }
            className={props.className?
                props.className+ " " + getLabelClassname(props)
                :getLabelClassname(props)
            }
        >
            {props.children}
        </label>
    )
}