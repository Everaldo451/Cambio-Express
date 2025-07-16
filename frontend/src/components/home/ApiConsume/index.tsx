import { ComponentProps, ReactNode, useEffect, useState, useRef} from "react";
import CommonStyleProps, { StyledButton } from "../../CommonButton";

function GraphImageContainer(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="flex flex-col justify-center align-center"
        >
            {props.children}
        </div>
    )
}


function GraphImage(props:React.ImgHTMLAttributes<HTMLImageElement>) {
    return (
        <img
            {...props}
            className="w-[60%]"
        >
            {props.children}
        </img>
    )
}


function Button (props:ComponentProps<typeof StyledButton>) {
    const styledButtonRef = useRef<HTMLButtonElement|null>(null)
    const styledButtonElement = <StyledButton {...props} ref={styledButtonRef}/>
    const [style, setStyle] = useState<string|null>(null)

    useEffect(() => {
        setStyle(
            prev => styledButtonRef.current?styledButtonRef.current.className:prev
        )
    },[styledButtonRef])

    return (
        <StyledButton
            {...props}
            className={`m-[0_5px] `+style}
        >
            {props.children}
        </StyledButton>
    )

}

interface ButtonProps {
    children: ReactNode,
    money: string,
    onClick:(money:string) => void
}

function ConvertionButton({children,money,onClick}:ButtonProps) {

    const styleProps:CommonStyleProps = {
        borderColor: "rgb(202, 132, 2)",
        color: "black",
        hoverColor: "white",
        hoverBg: "rgb(202, 132, 2)"
    }

    return (
        <Button 
            {...styleProps} 
            onClick={(_:React.MouseEvent<HTMLButtonElement>) => {onClick(money)}}
        >
            {children}
        </Button>
    )
    
}


export default function APIConsumer() {
    const [src, setSrc] = useState("")

    async function getImageWithMoney(money:string) {
        try {
            const response = await fetch(`/api/graphs/get/${money}`)
            const data = await response.json()
    
            if (data) {
                setSrc(data.image)
            }
        }
        catch (error) {}
    }

    useEffect(() => {
        getImageWithMoney("USD")
    }, [])

    return (
        <GraphImageContainer>
            <GraphImage src={src}/>
            <section>
                <ConvertionButton money="USD" onClick={getImageWithMoney}>Dólar</ConvertionButton>
                <ConvertionButton money="EUR" onClick={getImageWithMoney}>Euro</ConvertionButton>
                <ConvertionButton money="BTC" onClick={getImageWithMoney}>Bitcoin</ConvertionButton>
            </section>
        </GraphImageContainer>
    )
}