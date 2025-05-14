import styled from "styled-components";

const WeOfferSection = styled.section`
    display: grid;
    grid-template-rows: auto 1fr;
    background-color: #EFF2FE;
    height: 100vh;
    padding: 40px;
`

const Offerts = styled.section`
    display: grid;
    grid-template-columns: repeat(4,1fr);
    grid-template-rows: repeat(2,1fr);
    gap: 20px;
    margin-top: 20px;

    & > div:nth-child(odd) {
        background-color: #D9D9D9
    }

    & > div:nth-child(even) {
        background-color: #000000
    }

    & > div:nth-child(2n+5) {
        background-color: #000000
    }
    
    & > div:nth-child(2n+6) {
        background-color: #D9D9D9
    }
` 

const H3 = styled.h3`
    margin: 0;
    text-align: center;
    font-family: InstrumentSans;
    font-size: 24px;
`

const Div = styled.div`
    font-family: InstrumentSans;
    display: flex;
    flex-direction: column;
    padding: 20px;

    & h4 {
        font-size: 15px;
        font-family: InstrumentSans;
        text-align: center;
        margin: 0;
    }
    
    & p {
        font-size: 12px;
        font-family: InstrumentSans;
        text-wrap: wrap;
        margin: auto 0;
    }
`


export default function WeOffer() {

    return (
        <WeOfferSection>
            <H3>O que oferecemos?</H3>
            <Offerts>
                <Div>
                    <h4>Taxas Competitivas</h4>
                    <p>Oferecemos as melhores taxas de câmbio do mercado, garantindo que você obtenha o máximo valor pelo seu dinheiro.</p>
                </Div>
                <div></div>
                <Div>
                    <h4>Transações Seguras</h4>
                    <p>Utilizamos tecnologia avançada para garantir a segurança de todas as suas transações e proteger seus dados.</p>
                </Div>
                <div></div>
                <div></div>
                <Div>
                    <h4>Plataforma Intuitiva</h4>
                    <p>Oferecemos uma plataforma digital fácil de usar para que você possa consultar taxas, fazer transações e monitorar seu saldo a qualquer hora e de qualquer lugar.</p>
                </Div>
                <div></div>
                <Div>
                    <h4>Variedade de Moedas</h4>
                    <p>Disponibilizamos uma ampla gama de moedas estrangeiras para que você possa realizar suas operações com facilidade, independentemente do destino.</p>
                </Div>
            </Offerts>
        </WeOfferSection>
    )
}