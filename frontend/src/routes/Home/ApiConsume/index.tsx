import { ReactNode, useState } from "react";
import styled from "styled-components";
import CommonStyleProps, { StyledButton } from "../../../components/CommonButton";

const IntroducDiv = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
`

const ImgContainer = styled(IntroducDiv)`
    align-items: center;

    &> img {
        width: 100%;
        max-height: 80%;
    }
`

const Button = styled(StyledButton)`
    margin: 0 5px;
`

interface ButtonProps {
    children: ReactNode,
    money: string,
    func:(money:string) => void
}

function ConvertionButton({children,money,func}:ButtonProps) {

    const styleProps:CommonStyleProps = {
        borderColor: "rgb(202, 132, 2)",
        color: "black",
        hoverColor: "white",
        hoverBg: "rgb(202, 132, 2)"
    }

    return <Button {...styleProps} onClick={(e) => {func(money)}}>{children}</Button>
    
}


function APIConsumer() {

    const [src, setSrc] = useState("")


    async function GetImageWithMoney(money:string) {
        try {
            const response = await fetch(`/api/graphs/get/${money}`)
            const data = await response.json()
    
            if (data) {setSrc(data.image)}
    
            return
        }
        catch (error) {}
    }

    return (
        <ImgContainer>
            <img src={src}/>
            <section>
                <ConvertionButton money="USD" func={GetImageWithMoney}>Dólar</ConvertionButton>
                <ConvertionButton money="EUR" func={GetImageWithMoney}>Euro</ConvertionButton>
                <ConvertionButton money="BTC" func={GetImageWithMoney}>Bitcoin</ConvertionButton>
            </section>
        </ImgContainer>
    )
}


export default APIConsumer