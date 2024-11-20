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


export default function WeOffer() {
    return (
        <WeOfferSection>
            <H3>O que oferecemos?</H3>
            <Offerts>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </Offerts>
        </WeOfferSection>
    )
}