import styled, {ThemeProvider} from "styled-components";
import { ReactNode, useContext, useState } from "react";
import { UserContext } from "../../main";
import FeedBacks from "../../components/FeedBacks";
import APIConsumer from "./ApiConsume";

const IntroducSection = styled.section`
    padding: 40px 20px;
    display: grid;
    grid-template-columns: 1fr 2fr;
    color: black;
    background-color: white;

    & * {
        margin: 0;
    }
    
    & p {
        font-size: 15px;
    }

    & p span{
        color: orange;
    }

    & ul > li{
        margin-top: 20px;
        list-style: none;
    }
`

const IntroducDiv = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
`

const StyledDetail = styled.details`
    &[open] {

        & summary {

            background-color: ${(props) => props.theme.hover.background};

            &::marker {
                content: "# ";
            }
        }
    }
`

const StyledSummary = styled.summary`
    transition: all 0.5s;
    padding: 5px;
    border-radius: 5px 5px 0 0;

    &::marker {
        content: "> ";
        font-weight: bold;
        font-size: 18px;
        margin-right: 10px;
        writing-mode: vertical-lr;
        transition: all 0.5s;
    }

    &:hover {
        background-color: ${(props) => props.theme.hover.background};
    }

`

const SummaryStyleProvider = {
    hover: {
        background: "red",

        marker: {
            writingMode: "vertical-lr",
            transform: "rotate(90deg)"
        }
    }
}

const DetailsParagraph = styled.p`
    border: 1px solid black;
    border-top: none;
    padding: 5px;
    border-radius: 0 0 5px 5px;
`

function Home() {

    const [user,setUser] = useContext(UserContext)

    return (
            <main>
                <IntroducSection>
                    <IntroducDiv>
                        <h1>Câmbio Express</h1>
                        <p>Bem vindo{user? <span>, {user.username},</span>:null} à maior agência de câmbio do país, onde você encontra:</p>
                        <ul>
                            <ThemeProvider theme={SummaryStyleProvider}>
                            <li>
                                <StyledDetail>
                                    <StyledSummary>Taxas Competitivas</StyledSummary>
                                    <DetailsParagraph>
                                    Oferecemos as melhores taxas de câmbio do mercado, garantindo que você obtenha o máximo valor pelo seu dinheiro.
                                    </DetailsParagraph>
                                </StyledDetail>
                            </li>
                            <li>
                                <StyledDetail>
                                    <StyledSummary>Transações Seguras</StyledSummary>
                                    <DetailsParagraph>
                                    Utilizamos tecnologia avançada para garantir a segurança de todas as suas transações e proteger seus dados.
                                    </DetailsParagraph>
                                </StyledDetail>
                            </li>
                            <li>
                                <StyledDetail>
                                    <StyledSummary>Plataforma Online Intuitiva</StyledSummary>
                                    <DetailsParagraph>
                                    Oferecemos uma plataforma digital fácil de usar para que você possa consultar taxas, fazer transações e monitorar seu saldo a qualquer hora e de qualquer lugar.
                                    </DetailsParagraph>
                                </StyledDetail>
                            </li>
                            <li>
                                <StyledDetail>
                                    <StyledSummary>Variedade de Moedas</StyledSummary>
                                    <DetailsParagraph>
                                    Disponibilizamos uma ampla gama de moedas estrangeiras para que você possa realizar suas operações com facilidade, independentemente do destino.
                                    </DetailsParagraph>
                                </StyledDetail>
                            </li>
                            </ThemeProvider>
                        </ul>
                    </IntroducDiv>
                    <APIConsumer/>
                </IntroducSection>

                <FeedBacks/>
        </main>
    )
}


export default Home
