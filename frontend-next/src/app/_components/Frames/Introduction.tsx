import Image from "next/image";

function IntroducSection(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <section 
            {...props}
            className="grid grid-cols-[repeat(2,1fr)] h-dvh bg-[#191A24] text-black"
        >
            {props.children}
        </section>
    )
}


function IntroductText(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <section 
            {...props}
            className="flex flex-col text-white justify-center font-instrument-sans p-[15%]"
        >
            {props.children}
        </section>
    )
}


function ImageContainer(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="h-full clip-right-ellipse"
        >
            <Image
                alt="Imagem principal."
                src="/computer.jpg"
                className="object-cover object-center"
            ></Image>
        </div>
    )
}


function P(props:React.HTMLAttributes<HTMLParagraphElement>) {
    return (
        <p {...props} className="text-[20px] animate-slide-in">
            {props.children}
        </p>
    )
}


function H1(props:React.HTMLAttributes<HTMLHeadingElement>) {
    return (
        <h1 {...props} className="text-[32px] animate-slide-in">
            {props.children}
        </h1>
    )
}


export default function Introduction() {
    return (
        <IntroducSection>
            <IntroductText>
                <H1>Câmbio Express</H1>
                <P>A maior agência de câmbio do país.</P>
            </IntroductText>
            <ImageContainer/>

        </IntroducSection>
    )
}