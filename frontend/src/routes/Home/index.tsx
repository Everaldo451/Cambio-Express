import styled from "styled-components";
import { ReactNode, useContext, useState } from "react";
import { UserContext } from "../../main";
import FeedBacks from "../../components/FeedBacks";

const IntroducSection = styled.section`
    padding: 40px 20px;
    display: grid;
    grid-template-columns: repeat(2,1fr);
    color: black;
    background-color: white;

    & * {
        margin: 0;
    }
    
    & p {
        font-size: 15px;
        margin-top: 10px;
    }

    & p span{
        color: orange;
    }

    & ul > li{
        margin-top: 20px;
    }
`

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

const StyledButton = styled.button`
    padding: 5px 10px;
    border: 1px solid rgb(202, 132, 2);
    background-color: inherit;
    color:black;
    margin: 0 5px;
    transition: all 0.5s;

    &:hover {
        cursor: pointer;
        border: 1px solid transparent;
        background-color: rgb(202, 132, 2);
        color:white;
    }
`

interface ButtonProps {
    children: ReactNode,
    money: string,
    func:(money:string) => void
}

function ConvertionButton({children,money,func}:ButtonProps) {

    return <StyledButton onClick={(e) => {func(money)}}>{children}</StyledButton>
    
}


function Home() {

    const [src, setSrc] = useState("")
    const [user,setUser] = useContext(UserContext)

    async function GetImageWithMoney(money:string) {
        try {
            const response = await fetch(`127.0.0.1:8000/graphs/get/${money}`)
            const data = await response.json()
    
            if (data) {setSrc(data.image)}
    
            return
        }
        catch (error) {}
    }

    GetImageWithMoney("USD")

    return (
            <main>
                <IntroducSection>
                    <IntroducDiv>
                        <h1>Câmbio Express</h1>
                        <p>Bem vindo{user? <span>{user.username}</span>:null} à maior agência de câmbio do país, onde você encontra:</p>
                        <ul>
                            <li>
                                <strong>Taxas Competitivas:</strong>
                                <p>
                                Oferecemos as melhores taxas de câmbio do mercado, garantindo que você obtenha o máximo valor pelo seu dinheiro.
                                </p>
                            </li>
                            <li>
                                <strong>Transações Seguras:</strong>
                                <p>
                                Utilizamos tecnologia avançada para garantir a segurança de todas as suas transações e proteger seus dados.
                                </p>
                            </li>
                            <li>
                                <strong>Plataforma Online Intuitiva:</strong>
                                <p>
                                Oferecemos uma plataforma digital fácil de usar para que você possa consultar taxas, fazer transações e monitorar seu saldo a qualquer hora e de qualquer lugar.
                                </p>
                            </li>
                            <li>
                                <strong>Variedade de Moedas:</strong>
                                <p>
                                Disponibilizamos uma ampla gama de moedas estrangeiras para que você possa realizar suas operações com facilidade, independentemente do destino.
                                </p>
                            </li>
                        </ul>
                    </IntroducDiv>
                    <ImgContainer>
                        <img src={src}/>
                        <section>
                            <ConvertionButton money="USD" func={GetImageWithMoney}>Dólar</ConvertionButton>
                            <ConvertionButton money="EUR" func={GetImageWithMoney}>Euro</ConvertionButton>
                            <ConvertionButton money="BTC" func={GetImageWithMoney}>Bitcoin</ConvertionButton>
                        </section>
                    </ImgContainer>
                </IntroducSection>

                <FeedBacks/>
        </main>
    )
}


export default Home
