import React from "react";

function Container(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <section 
            {...props}
            className="grid grid-cols-[auto_1fr] bg-[#EFF2FE] h-dvh p-[40px]"
        >
            {props.children}
        </section>
    )
}


function FeaturesSection(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <section
            {...props}
            className="grid grid-cols-[repeat(4,1fr)] grid-rows-[repeat(2,1fr)] gap-[20px] mt-[20px]"
        >
            {props.children}
        </section>
    )
}

/*
const FeaturesSection = styled.section`

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
*/

function H3(props:React.HTMLAttributes<HTMLHeadingElement>) {
    return (
        <h3
            {...props}
            className="m-[0] text-center text-[24px] font-instrument-sans"
        >
            {props.children}
        </h3>
    )
}


function Feature(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="flex flex-col p-[20px] font-instrument-sans odd:bg-[#D9D9D9] even:bg-[#000000]"
        >
            {props.children}
        </div>
    )
}

function EmptyDiv(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="odd:bg-[#D9D9D9] even:bg-[#000000]"
        >
        </div>
    )
}


function FeatureH4(props:React.HTMLAttributes<HTMLHeadElement>) {
    return (
        <h4
            {...props}
            className=""
        >
            {props.children}
        </h4>
    )
}

function FeatureParagraph(props:React.HTMLAttributes<HTMLParagraphElement>) {
    return (
        <p
            {...props}
            className=""
        >
            {props.children}
        </p>
    )
}

export default function KeyFeatures() {

    return (
        <Container>
            <H3>O que oferecemos?</H3>
            <FeaturesSection>
                <Feature>
                    <FeatureH4>Taxas Competitivas</FeatureH4>
                    <FeatureParagraph>Oferecemos as melhores taxas de câmbio do mercado, garantindo que você obtenha o máximo valor pelo seu dinheiro.</FeatureParagraph>
                </Feature>
                <EmptyDiv/>
                <Feature>
                    <FeatureH4>Transações Seguras</FeatureH4>
                    <FeatureParagraph>Utilizamos tecnologia avançada para garantir a segurança de todas as suas transações e proteger seus dados.</FeatureParagraph>
                </Feature>
                <EmptyDiv/>
                <EmptyDiv/>
                <Feature>
                    <FeatureH4>Plataforma Intuitiva</FeatureH4>
                    <FeatureParagraph>Oferecemos uma plataforma digital fácil de usar para que você possa consultar taxas, fazer transações e monitorar seu saldo a qualquer hora e de qualquer lugar.</FeatureParagraph>
                </Feature>
                <EmptyDiv/>
                <Feature>
                    <FeatureH4>Variedade de Moedas</FeatureH4>
                    <FeatureParagraph>Disponibilizamos uma ampla gama de moedas estrangeiras para que você possa realizar suas operações com facilidade, independentemente do destino.</FeatureParagraph>
                </Feature>
            </FeaturesSection>
        </Container>
    )
}