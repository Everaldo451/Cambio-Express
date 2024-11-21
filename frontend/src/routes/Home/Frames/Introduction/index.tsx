import styled, {keyframes} from "styled-components";
import HomeImage from "../../../../assets/HomePageImage.jpg"

const IntroducSection = styled.section`
    display: grid;
    grid-template-columns: repeat(2,1fr);
    color: black;
    background-color: #191A24;
    height: 100vh;

    & * {
        margin: 0;
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

const SlideText = keyframes`

    0% {
        transform: translateX(-200%);
        opacity: 0;
    }

    40% {
        opacity: 0.3;
    }

    100% {
        transform: translateX(0);
        opacity: 1;
    }
`

const P = styled.p`
    font-size: 20px;
    animation-name: ${SlideText};
    animation-duration: 1s
`

const H1 = styled.h1`
    font-size: 32px;
    animation-name: ${SlideText};
    animation-duration: 1s;
`

export default function Introduction() {
    return (
        <IntroducSection>
            <IntroductText>
                <H1>Câmbio Express</H1>
                <P>A maior agência de câmbio do país.</P>
            </IntroductText>
            <ImageContainer>
            </ImageContainer>

        </IntroducSection>
    )
}