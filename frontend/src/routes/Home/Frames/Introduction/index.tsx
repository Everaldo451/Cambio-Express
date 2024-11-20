import styled, {ThemeProvider} from "styled-components";
import HomeImage from "../../../../assets/HomePageImage.jpg"
import { useContext } from "react";
import { UserContext } from "../../../../main";

const IntroducSection = styled.section`
    display: grid;
    grid-template-columns: repeat(2,1fr);
    color: black;
    background-color: #191A24;
    height: 100vh;

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

const IntroductText = styled.section`
    display: flex;
    flex-direction: column;
    justify-content: center;
    font-family: InstrumentSans;
    color: white;
    padding: 15%;

    & h1 {
        font-size: 32px;
    }

    & p {
        font-size: 20px;
    }
`

const ImageContainer = styled.div`
    background-repeat: no-repeat;
    background-size: cover;
    background-image: url(${HomeImage});
    height: 100%;
    clip-path: ellipse(100% 100% at right); 
`

export default function Introduction() {
    return (
        <IntroducSection>
            <IntroductText>
                <h1>Câmbio Express</h1>
                <p>A maior agência de câmbio do país.</p>
            </IntroductText>
            <ImageContainer>
            </ImageContainer>

        </IntroducSection>
    )
}